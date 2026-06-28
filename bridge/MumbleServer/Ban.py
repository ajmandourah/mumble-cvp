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
class Ban:
    """
    A single ip mask for a ban.
    
    Attributes
    ----------
    address : bytes
        Address to ban.
    bits : int
        Number of bits in ban to apply.
    name : str
        Username associated with ban.
    hash : str
        Hash of banned user.
    reason : str
        Reason for ban.
    start : int
        Date ban was applied in unix time format.
    duration : int
        Duration of ban.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::Ban``.
    """
    address: bytes = field(default_factory=bytes)
    bits: int = 0
    name: str = ""
    hash: str = ""
    reason: str = ""
    start: int = 0
    duration: int = 0

_MumbleServer_Ban_t = IcePy.defineStruct(
    "::MumbleServer::Ban",
    Ban,
    (),
    (
        ("address", (), _MumbleServer_NetAddress_t),
        ("bits", (), IcePy._t_int),
        ("name", (), IcePy._t_string),
        ("hash", (), IcePy._t_string),
        ("reason", (), IcePy._t_string),
        ("start", (), IcePy._t_int),
        ("duration", (), IcePy._t_int)
    ))

__all__ = ["Ban", "_MumbleServer_Ban_t"]
