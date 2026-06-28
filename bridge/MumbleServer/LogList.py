# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.LogEntry import _MumbleServer_LogEntry_t

_MumbleServer_LogList_t = IcePy.defineSequence("::MumbleServer::LogList", (), _MumbleServer_LogEntry_t)

__all__ = ["_MumbleServer_LogList_t"]
