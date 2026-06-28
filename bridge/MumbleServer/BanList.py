# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.Ban import _MumbleServer_Ban_t

_MumbleServer_BanList_t = IcePy.defineSequence("::MumbleServer::BanList", (), _MumbleServer_Ban_t)

__all__ = ["_MumbleServer_BanList_t"]
