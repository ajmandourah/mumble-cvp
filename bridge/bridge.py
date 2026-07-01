#!/usr/bin/env python3
"""ICE bridge server for mumble-cvp.

Uses the zeroc-ice Python library to talk to Murmur's ICE protocol,
exposes a simple HTTP API for the Go server to consume.
"""

from __future__ import annotations

import base64
import json
import os
import socket
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import Ice
import MumbleServer

# Permission bitflag constants from Mumble.proto
PERMISSION_NAMES = {
    1 << 0: "Write",
    1 << 1: "Traverse",
    1 << 2: "Enter",
    1 << 3: "Speak",
    1 << 4: "Whisper",
    1 << 5: "MuteDeafen",
    1 << 6: "Move",
    1 << 7: "MakeChannel",
    1 << 8: "MakeTempChannel",
    1 << 9: "LinkChannel",
    1 << 10: "TextMessage",
    1 << 11: "Kick",
    1 << 12: "Ban",
    1 << 13: "Register",
    1 << 14: "RegisterSelf",
    1 << 15: "ResetUserContent",
}


class BridgeHandler(BaseHTTPRequestHandler):
    """HTTP handler that proxies ICE calls to Murmur."""

    def log_message(self, format, *args):  # noqa: A002
        print(f"[bridge] {args[0]}", file=sys.stderr)

    def do_GET(self):  # noqa: N802
        if self.path == "/health":
            self._respond(200, {"status": "ok"})
            return

        if self.path.startswith("/ice/"):
            endpoint = self.path[5:]
            params: dict[str, str] = {}
            if "?" in endpoint:
                endpoint, qs = endpoint.split("?", 1)
                for pair in qs.split("&"):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        params[k] = unquote(v)

            try:
                result = self._call_ice(endpoint, params)
                self._respond(200, result)
            except Exception as exc:
                self._respond(500, {"error": str(exc)})
            return

        self._respond(404, {"error": "not found"})

    def do_POST(self):  # noqa: N802
        if self.path.startswith("/ice/"):
            endpoint = self.path[5:]
            params: dict[str, str] = {}
            if "?" in endpoint:
                endpoint, qs = endpoint.split("?", 1)
                for pair in qs.split("&"):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        params[k] = unquote(v)

            content_length = int(self.headers.get("Content-Length", 0))
            body = {}
            if content_length > 0:
                raw = self.rfile.read(content_length)
                body = json.loads(raw)
            params.update(body)

            try:
                result = self._call_ice(endpoint, params)
                self._respond(200, result)
            except Exception as exc:
                self._respond(500, {"error": str(exc)})
            return

        self._respond(404, {"error": "not found"})

    def _call_ice(self, endpoint: str, params: dict[str, str]):
        secret = params.get("secret", "")
        host = params.get("host", "127.0.0.1")
        port = params.get("port", "6502")

        comm = Ice.initialize()

        def with_ctx(proxy):
            if secret:
                return proxy.ice_context({"secret": secret})
            return proxy

        def get_meta():
            proxy = with_ctx(comm.stringToProxy(f"Meta:tcp -h {host} -p {port}"))
            return MumbleServer.MetaPrx.uncheckedCast(proxy)

        def get_server(sid):
            meta = get_meta()
            for s in meta.getBootedServers():
                s = with_ctx(s)
                if s.id() == sid:
                    return s
            raise Exception(f"server ID {sid} not found")

        try:
            if endpoint == "booted":
                meta = get_meta()
                servers = meta.getBootedServers()
                result = []
                for s in servers:
                    s = with_ctx(s)
                    result.append(s.id())
                return {"servers": result}

            if endpoint == "tree":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                tree = server.getTree()
                return {"tree": _serialize_tree(tree)}

            if endpoint == "users":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                users = server.getUsers() or {}
                return {"users": [_serialize_user(u) for u in users.values()]}

            if endpoint == "channels":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                channels = server.getChannels() or {}
                return {"channels": [_serialize_channel(c) for c in channels.values()]}

            if endpoint == "server_name":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                conf = server.getConf("registername")
                return {"name": conf}

            if endpoint == "stats":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                meta = get_meta()
                version = meta.getVersion()
                uptime = server.getUptime()
                max_users = int(server.getConf("maxusers") or "200")
                return {
                    "stats": {
                        "version": f"{version[0]}.{version[1]}.{version[2]}",
                        "uptime": uptime,
                        "max_users": max_users,
                    }
                }

            if endpoint == "log":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                first = int(params.get("first", "0"))
                last = int(params.get("last", "100"))
                entries = server.getLog(first, last) or []
                return {
                    "entries": [
                        {"timestamp": e.timestamp, "text": e.txt} for e in entries
                    ]
                }

            if endpoint == "bans":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                bans = server.getBans() or []
                return {"bans": [_serialize_ban(b) for b in bans]}

            if endpoint == "listening":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                users = server.getUsers() or {}
                channels = server.getChannels() or {}
                listening = []
                for u in users.values():
                    chans = server.getListeningChannels(u.session) or []
                    if chans:
                        listening.append(
                            {
                                "user_session": u.session,
                                "user_name": u.name,
                                "channels": [
                                    {"id": c.id, "name": c.name}
                                    for c in chans
                                    if c in channels
                                ],
                            }
                        )
                return {"listening": listening}

            # --- Admin write endpoints ---

            if endpoint == "kick":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                session = int(params.get("session", "0"))
                reason = params.get("reason", "kicked by admin")
                server.kickUser(session, reason)
                return {"status": "ok"}

            if endpoint == "set_state":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                session = int(params.get("session", "0"))
                channel = int(params.get("channel", "0"))
                mute = _to_bool(params.get("mute", False))
                deaf = _to_bool(params.get("deaf", False))
                suppress = _to_bool(params.get("suppress", False))
                priority = _to_bool(params.get("priority", False))
                users = server.getUsers() or {}
                existing = users.get(session)
                user = MumbleServer.User()
                user.session = session
                user.channel = channel
                user.name = existing.name if existing else ""
                user.mute = mute
                user.deaf = deaf
                user.suppress = suppress
                user.prioritySpeaker = priority
                server.setState(user)
                return {"status": "ok"}

            if endpoint == "add_channel":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                name = params.get("name", "New Channel")
                parent = int(params.get("parent", "0"))
                chid = server.addChannel(name, parent)
                return {"id": chid}

            if endpoint == "remove_channel":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                chid = int(params.get("id", "0"))
                server.removeChannel(chid)
                return {"status": "ok"}

            if endpoint == "set_channel_state":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                ch = MumbleServer.Channel()
                ch.id = int(params.get("id", "0"))
                ch.name = params.get("name", ch.name)
                ch.description = params.get("description", "")
                ch.position = int(params.get("position", "0"))
                links_str = params.get("links", "[]")
                ch.links = (
                    json.loads(links_str) if isinstance(links_str, str) else links_str
                )
                server.setChannelState(ch)
                return {"status": "ok"}

            if endpoint == "send_message":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                session = int(params.get("session", "0"))
                text = params.get("text", "")
                server.sendMessage(session, text)
                return {"status": "ok"}

            if endpoint == "send_message_channel":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                channel_id = int(params.get("channel_id", "0"))
                tree = _to_bool(params.get("tree", False))
                text = params.get("text", "")
                server.sendMessageChannel(channel_id, tree, text)
                return {"status": "ok"}

            if endpoint == "add_ban":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                bans = server.getBans() or []
                ban = MumbleServer.Ban()
                ban.address = params.get("address", "0.0.0.0")
                ban.bits = int(params.get("bits", "32"))
                ban.name = params.get("name", "")
                ban.reason = params.get("reason", "")
                ban.duration = int(params.get("duration", "0"))
                bans.append(ban)
                server.setBans(bans)
                return {"status": "ok"}

            if endpoint == "remove_ban":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                bans = server.getBans() or []
                addr = params.get("address", "")
                bits = int(params.get("bits", "32"))
                filtered = [
                    b
                    for b in bans
                    if _serialize_ip(b.address) != addr or b.bits != bits
                ]
                server.setBans(filtered)
                return {"status": "ok"}

            if endpoint == "acl":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                channel_id = int(params.get("channel_id", "0"))
                acls = []
                groups = []
                inherit = False
                try:
                    server.getACL(channel_id, acls, groups, inherit)
                except Exception:
                    pass
                return {
                    "acls": [_serialize_acl(a) for a in acls],
                    "groups": [_serialize_group(g) for g in groups],
                    "inherit": inherit,
                }

            if endpoint == "effective_permissions":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                session = int(params.get("session", "0"))
                channel_id = int(params.get("channel_id", "0"))
                perms = server.effectivePermissions(session, channel_id)
                return {"permissions": _decode_permissions(perms)}

            if endpoint == "registered_users":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                filt = params.get("filter", "")
                name_map = server.getRegisteredUsers(filt) or {}
                return {
                    "users": [
                        {"name": name, "user_id": uid} for uid, name in name_map.items()
                    ]
                }

            if endpoint == "registration":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                user_id = int(params.get("user_id", "0"))
                info = server.getRegistration(user_id) or {}
                result = {}
                for k, v in info.items():
                    if isinstance(v, bytes):
                        result[k] = base64.b64encode(v).decode()
                    else:
                        result[k] = str(v)
                return result

            if endpoint == "all_conf":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                conf = server.getAllConf() or {}
                return dict(conf)

            if endpoint == "set_conf":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                key = params.get("key", "")
                value = params.get("value", "")
                server.setConf(key, value)
                return {"status": "ok"}

            if endpoint == "certificate_list":
                sid = int(params.get("server_id", "1"))
                server = get_server(sid)
                session = int(params.get("session", "0"))
                certs = server.getCertificateList(session) or []
                return {"certificates": [base64.b64encode(c).decode() for c in certs]}

            return {"error": f"unknown endpoint: {endpoint}"}
        finally:
            comm.destroy()

    def _respond(self, status: int, data: dict):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def _serialize_tree(tree):
    return {
        "channel": _serialize_channel(tree.c),
        "children": [_serialize_tree(t) for t in (tree.children or [])],
        "users": [_serialize_user(u) for u in (tree.users or [])],
    }


def _serialize_user(user):
    ip = _serialize_ip(user.address)
    online_secs = getattr(user, "onlinesecs", 0)
    idle_secs = getattr(user, "idlesecs", 0)
    bytes_per_sec = getattr(user, "bytespersec", 0)
    udp_ping = getattr(user, "udpping", 0)
    tcp_ping = getattr(user, "tcpping", 0)
    tcp_only = getattr(user, "tcponly", False)
    user_id = getattr(user, "userID", 0)
    identity = getattr(user, "identity", "")
    context_raw = getattr(user, "context", None)
    version2 = getattr(user, "version2", "")
    if isinstance(version2, int):
        version2 = str(version2)

    # Decode context map
    context = {}
    if context_raw:
        for k, v in context_raw.items():
            try:
                context[k.decode() if isinstance(k, bytes) else k] = (
                    v.decode() if isinstance(v, bytes) else str(v)
                )
            except Exception:
                context[str(k)] = str(v)

    # Compute display fields
    ping_ms = udp_ping if udp_ping > 0 else tcp_ping
    online_formatted = _format_duration(online_secs)
    bw = bytes_per_sec / 1024
    bw_formatted = f"{bw:.1f} kB/s" if bw >= 1 else f"{bytes_per_sec} B/s"

    return {
        "name": user.name,
        "session": user.session,
        "channel_id": user.channel,
        "comment": user.comment,
        "registered": False,
        "mute": user.mute,
        "deaf": user.deaf,
        "self_mute": user.selfMute,
        "self_deaf": user.selfDeaf,
        "suppress": user.suppress,
        "priority_speaker": user.prioritySpeaker,
        "recording": user.recording,
        "flags": 0,
        "on_line": True,
        "last_seen": 0,
        "version": user.release or "",
        "platform": (user.os or "") + " " + (user.osversion or ""),
        "ip": ip,
        "online_secs": online_secs,
        "idle_secs": idle_secs,
        "bytes_per_sec": bytes_per_sec,
        "udp_ping": udp_ping,
        "tcp_ping": tcp_ping,
        "tcp_only": tcp_only,
        "user_id": user_id,
        "identity": identity,
        "context": context,
        "version2": version2,
        "online_formatted": online_formatted,
        "ping_ms": ping_ms,
        "bandwidth_formatted": bw_formatted,
    }


def _serialize_channel(channel):
    return {
        "id": channel.id,
        "parent": channel.parent,
        "name": channel.name,
        "description": channel.description,
        "temporary": channel.temporary,
        "position": channel.position,
        "links": channel.links or [],
        "max_users": 0,
        "password_set": False,
    }


def _serialize_ban(ban):
    addr = _serialize_ip(ban.address)
    start = getattr(ban, "start", 0)
    duration = getattr(ban, "duration", 0)
    expires = start + duration if duration > 0 else 0
    return {
        "address": addr,
        "bits": ban.bits,
        "name": ban.name,
        "hash": base64.b64encode(ban.hash).decode() if ban.hash else "",
        "reason": ban.reason,
        "start": start,
        "duration": duration,
        "expires": expires,
    }


def _serialize_acl(acl):
    return {
        "user_id": acl.userID,
        "group": acl.group,
        "allow": _decode_permissions(acl.allow),
        "deny": _decode_permissions(acl.deny),
        "apply_here": acl.applyHere,
        "apply_subs": acl.applySubs,
        "inherited": acl.inherited,
    }


def _serialize_group(group):
    return {
        "name": group.name,
        "inherit": group.inherit,
        "inheritable": group.inheritable,
        "members": [
            m.decode() if isinstance(m, bytes) else m for m in (group.members or [])
        ],
        "in_channel": group.inChannel,
    }


def _decode_permissions(bitmask):
    names = []
    for bit, name in PERMISSION_NAMES.items():
        if bitmask & bit:
            names.append(name)
    return names


def _serialize_ip(addr):
    if not addr:
        return None
    if isinstance(addr, bytes):
        try:
            if len(addr) == 4:
                return socket.inet_ntoa(addr)
            elif len(addr) == 16:
                return socket.inet_ntop(socket.AF_INET6, addr)
        except Exception:
            return addr.hex()
    return str(addr)


def _to_bool(val):
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.lower() in ("true", "1", "yes")
    return bool(val)


def _format_duration(secs):
    if secs < 60:
        return f"{secs}s"
    mins = secs // 60
    if mins < 60:
        return f"{mins}m"
    hours = mins // 60
    if hours < 24:
        return f"{hours}h {mins % 60}m"
    days = hours // 24
    return f"{days}d {hours % 24}h"


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4001
    server = ThreadingHTTPServer(("127.0.0.1", port), BridgeHandler)
    print(f"Bridge listening on 127.0.0.1:{port}", file=sys.stderr)
    server.serve_forever()


if __name__ == "__main__":
    main()
