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
class Channel:
    """
    A channel.
    
    Attributes
    ----------
    id : int
        Channel ID. This is unique per channel, and the root channel is always id 0.
    name : str
        Name of the channel. There can not be two channels with the same parent that has the same name.
    parent : int
        ID of parent channel, or -1 if this is the root channel.
    links : list[int]
        List of id of linked channels.
    description : str
        Description of channel. Shown as tooltip for this channel.
    temporary : bool
        Channel is temporary, and will be removed when the last user leaves it. Read-only.
    position : int
        Position of the channel which is used in Client for sorting.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::Channel``.
    """
    id: int = 0
    name: str = ""
    parent: int = 0
    links: list[int] = field(default_factory=list)
    description: str = ""
    temporary: bool = False
    position: int = 0

_MumbleServer_Channel_t = IcePy.defineStruct(
    "::MumbleServer::Channel",
    Channel,
    (),
    (
        ("id", (), IcePy._t_int),
        ("name", (), IcePy._t_string),
        ("parent", (), IcePy._t_int),
        ("links", (), _MumbleServer_IntList_t),
        ("description", (), IcePy._t_string),
        ("temporary", (), IcePy._t_bool),
        ("position", (), IcePy._t_int)
    ))

__all__ = ["Channel", "_MumbleServer_Channel_t"]
