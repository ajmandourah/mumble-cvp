# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ACL import _MumbleServer_ACL_t

_MumbleServer_ACLList_t = IcePy.defineSequence("::MumbleServer::ACLList", (), _MumbleServer_ACL_t)

__all__ = ["_MumbleServer_ACLList_t"]
