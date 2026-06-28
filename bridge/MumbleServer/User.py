# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.NetAddress import _MumbleServer_NetAddress_t

from dataclasses import dataclass
from dataclasses import field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Buffer


@dataclass
class User:
    """
    A connected user.
    
    Attributes
    ----------
    session : int
        Session ID. This identifies the connection to the server.
    userid : int
        User ID. -1 if the user is anonymous.
    mute : bool
        Is user muted by the server?
    deaf : bool
        Is user deafened by the server? If true, this implies mute.
    suppress : bool
        Is the user suppressed by the server? This means the user is not muted, but does not have speech privileges in the current channel.
    prioritySpeaker : bool
        Is the user a priority speaker?
    selfMute : bool
        Is the user self-muted?
    selfDeaf : bool
        Is the user self-deafened? If true, this implies mute.
    recording : bool
        Is the User recording? (This flag is read-only and cannot be changed using setState().)
    channel : int
        Channel ID the user is in. Matches ``Channel.id``.
    name : str
        The name of the user.
    onlinesecs : int
        Seconds user has been online.
    bytespersec : int
        Average transmission rate in bytes per second over the last few seconds.
    version : int
        Legacy client version.
    version2 : int
        New client version. (See https://github.com/mumble-voip/mumble/issues/5827)
    release : str
        Client release. For official releases, this equals the version. For snapshots and git compiles, this will be something else.
    os : str
        Client OS.
    osversion : str
        Client OS Version.
    identity : str
        Plugin Identity. This will be the user's unique ID inside the current game.
    context : str
        Base64-encoded Plugin context. This is a binary blob identifying the game and team the user is on.
        
        The used Base64 alphabet is the one specified in RFC 2045.
        
        Before Mumble 1.3.0, this string was not Base64-encoded. This could cause problems for some Ice
        implementations, such as the .NET implementation.
        
        If you need the exact string that is used by Mumble, you can get it by Base64-decoding this string.
        
        If you simply need to detect whether two users are in the same game world, string comparisons will
        continue to work as before.
    comment : str
        User comment. Shown as tooltip for this user.
    address : bytes
        Client address.
    tcponly : bool
        TCP only. True until UDP connectivity is established.
    idlesecs : int
        Idle time. This is how many seconds it is since the user last spoke. Other activity is not counted.
    udpPing : float
        UDP Ping Average. This is the average ping for the user via UDP over the duration of the connection.
    tcpPing : float
        TCP Ping Average. This is the average ping for the user via TCP over the duration of the connection.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::User``.
    """
    session: int = 0
    userid: int = 0
    mute: bool = False
    deaf: bool = False
    suppress: bool = False
    prioritySpeaker: bool = False
    selfMute: bool = False
    selfDeaf: bool = False
    recording: bool = False
    channel: int = 0
    name: str = ""
    onlinesecs: int = 0
    bytespersec: int = 0
    version: int = 0
    version2: int = 0
    release: str = ""
    os: str = ""
    osversion: str = ""
    identity: str = ""
    context: str = ""
    comment: str = ""
    address: bytes = field(default_factory=bytes)
    tcponly: bool = False
    idlesecs: int = 0
    udpPing: float = 0.0
    tcpPing: float = 0.0

_MumbleServer_User_t = IcePy.defineStruct(
    "::MumbleServer::User",
    User,
    (),
    (
        ("session", (), IcePy._t_int),
        ("userid", (), IcePy._t_int),
        ("mute", (), IcePy._t_bool),
        ("deaf", (), IcePy._t_bool),
        ("suppress", (), IcePy._t_bool),
        ("prioritySpeaker", (), IcePy._t_bool),
        ("selfMute", (), IcePy._t_bool),
        ("selfDeaf", (), IcePy._t_bool),
        ("recording", (), IcePy._t_bool),
        ("channel", (), IcePy._t_int),
        ("name", (), IcePy._t_string),
        ("onlinesecs", (), IcePy._t_int),
        ("bytespersec", (), IcePy._t_int),
        ("version", (), IcePy._t_int),
        ("version2", (), IcePy._t_long),
        ("release", (), IcePy._t_string),
        ("os", (), IcePy._t_string),
        ("osversion", (), IcePy._t_string),
        ("identity", (), IcePy._t_string),
        ("context", (), IcePy._t_string),
        ("comment", (), IcePy._t_string),
        ("address", (), _MumbleServer_NetAddress_t),
        ("tcponly", (), IcePy._t_bool),
        ("idlesecs", (), IcePy._t_int),
        ("udpPing", (), IcePy._t_float),
        ("tcpPing", (), IcePy._t_float)
    ))

__all__ = ["User", "_MumbleServer_User_t"]
