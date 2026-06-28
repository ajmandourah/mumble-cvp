#!/usr/bin/env python3
"""Minimal ICE bridge server for mumble-cvp.

Uses the zeroc-ice Python library to talk to Murmur's ICE protocol,
exposes a simple HTTP API for the Go server to consume.
"""
from __future__ import annotations

import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import Ice
import MumbleServer


class BridgeHandler(BaseHTTPRequestHandler):
    """HTTP handler that proxies ICE calls to Murmur."""

    def log_message(self, format, *args):  # noqa: A002
        pass  # suppress logs

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
                        params[k] = v

            try:
                result = self._call_ice(endpoint, params)
                self._respond(200, result)
            except Exception as exc:
                self._respond(500, {"error": str(exc)})
            return

        self._respond(404, {"error": "not found"})

    def _call_ice(self, endpoint: str, params: dict[str, str]):
        import MumbleServer  # noqa: F811

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
        "ip": _serialize_ip(user.address),
        "cert_dns": [],
        "context": {},
        "strong_text": "",
        "groups": {},
        "permissions": 0,
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


def _serialize_ip(addr):
    if not addr:
        return None
    if isinstance(addr, bytes):
        import socket
        try:
            if len(addr) == 4:
                return socket.inet_ntoa(addr)
            elif len(addr) == 16:
                return socket.inet_ntop(socket.AF_INET6, addr)
        except Exception:
            return addr.hex()
    return str(addr)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4001
    server = HTTPServer(("127.0.0.1", port), BridgeHandler)
    print(f"Bridge listening on 127.0.0.1:{port}", file=sys.stderr)
    server.serve_forever()


if __name__ == "__main__":
    main()
