# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.Group import _MumbleServer_Group_t

_MumbleServer_GroupList_t = IcePy.defineSequence("::MumbleServer::GroupList", (), _MumbleServer_Group_t)

__all__ = ["_MumbleServer_GroupList_t"]
