# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.Server_forward import _MumbleServer_ServerPrx_t

_MumbleServer_ServerList_t = IcePy.defineSequence("::MumbleServer::ServerList", (), _MumbleServer_ServerPrx_t)

__all__ = ["_MumbleServer_ServerList_t"]
