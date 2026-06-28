# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.IntList import _MumbleServer_IntList_t

from dataclasses import dataclass
from dataclasses import field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Buffer


@dataclass
class Group:
    """
    A group. Groups are defined per channel, and can inherit members from parent channels.
    
    Attributes
    ----------
    name : str
        Group name
    inherited : bool
        Is this group inherited from a parent channel? Read-only.
    inherit : bool
        Does this group inherit members from parent channels?
    inheritable : bool
        Can subchannels inherit members from this group?
    add : list[int]
        List of users to add to the group.
    remove : list[int]
        List of inherited users to remove from the group.
    members : list[int]
        Current members of the group, including inherited members. Read-only.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::Group``.
    """
    name: str = ""
    inherited: bool = False
    inherit: bool = False
    inheritable: bool = False
    add: list[int] = field(default_factory=list)
    remove: list[int] = field(default_factory=list)
    members: list[int] = field(default_factory=list)

_MumbleServer_Group_t = IcePy.defineStruct(
    "::MumbleServer::Group",
    Group,
    (),
    (
        ("name", (), IcePy._t_string),
        ("inherited", (), IcePy._t_bool),
        ("inherit", (), IcePy._t_bool),
        ("inheritable", (), IcePy._t_bool),
        ("add", (), _MumbleServer_IntList_t),
        ("remove", (), _MumbleServer_IntList_t),
        ("members", (), _MumbleServer_IntList_t)
    ))

__all__ = ["Group", "_MumbleServer_Group_t"]
