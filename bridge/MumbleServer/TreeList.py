# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.Tree_forward import _MumbleServer_Tree_t

_MumbleServer_TreeList_t = IcePy.defineSequence("::MumbleServer::TreeList", (), _MumbleServer_Tree_t)

__all__ = ["_MumbleServer_TreeList_t"]
