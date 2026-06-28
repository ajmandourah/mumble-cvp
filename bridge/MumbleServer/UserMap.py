# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.User import _MumbleServer_User_t

_MumbleServer_UserMap_t = IcePy.defineDictionary("::MumbleServer::UserMap", (), IcePy._t_int, _MumbleServer_User_t)

__all__ = ["_MumbleServer_UserMap_t"]
