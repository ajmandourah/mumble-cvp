# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.UserInfo import _MumbleServer_UserInfo_t

_MumbleServer_UserInfoMap_t = IcePy.defineDictionary("::MumbleServer::UserInfoMap", (), _MumbleServer_UserInfo_t, IcePy._t_string)

__all__ = ["_MumbleServer_UserInfoMap_t"]
