# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from dataclasses import dataclass


@dataclass(order=True, unsafe_hash=True)
class ACL:
    """
    Access Control List for a channel. ACLs are defined per channel, and can be inherited from parent channels.
    
    Attributes
    ----------
    applyHere : bool
        Does the ACL apply to this channel?
    applySubs : bool
        Does the ACL apply to subchannels?
    inherited : bool
        Is this ACL inherited from a parent channel? Read-only.
    userid : int
        ID of user this ACL applies to. -1 if using a group name.
    group : str
        Group this ACL applies to. Blank if using userid.
    allow : int
        Binary mask of privileges to allow.
    deny : int
        Binary mask of privileges to deny.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::ACL``.
    """
    applyHere: bool = False
    applySubs: bool = False
    inherited: bool = False
    userid: int = 0
    group: str = ""
    allow: int = 0
    deny: int = 0

_MumbleServer_ACL_t = IcePy.defineStruct(
    "::MumbleServer::ACL",
    ACL,
    (),
    (
        ("applyHere", (), IcePy._t_bool),
        ("applySubs", (), IcePy._t_bool),
        ("inherited", (), IcePy._t_bool),
        ("userid", (), IcePy._t_int),
        ("group", (), IcePy._t_string),
        ("allow", (), IcePy._t_int),
        ("deny", (), IcePy._t_int)
    ))

__all__ = ["ACL", "_MumbleServer_ACL_t"]
