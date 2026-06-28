# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from Ice.Value import Value

from MumbleServer.Channel import Channel
from MumbleServer.Channel import _MumbleServer_Channel_t

from MumbleServer.TreeList import _MumbleServer_TreeList_t

from MumbleServer.Tree_forward import _MumbleServer_Tree_t

from MumbleServer.UserList import _MumbleServer_UserList_t

from dataclasses import dataclass
from dataclasses import field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MumbleServer.User import User

@dataclass(eq=False)
class Tree(Value):
    """
    User and subchannel state. Read-only.
    
    Attributes
    ----------
    c : Channel
        Channel definition of current channel.
    children : list[Tree | None]
        List of subchannels.
    users : list[User]
        Users in this channel.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice class ``::MumbleServer::Tree``.
    """
    c: Channel = field(default_factory=Channel)
    children: list[Tree | None] = field(default_factory=list)
    users: list[User] = field(default_factory=list)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::Tree"

_MumbleServer_Tree_t = IcePy.defineValue(
    "::MumbleServer::Tree",
    Tree,
    -1,
    (),
    False,
    None,
    (
        ("c", (), _MumbleServer_Channel_t, False, 0),
        ("children", (), _MumbleServer_TreeList_t, False, 0),
        ("users", (), _MumbleServer_UserList_t, False, 0)
    ))

setattr(Tree, '_ice_type', _MumbleServer_Tree_t)

__all__ = ["Tree", "_MumbleServer_Tree_t"]
