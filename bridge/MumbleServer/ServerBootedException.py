# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class ServerBootedException(ServerException):
    """
    This happens if you try to fetch user or channel state on a stopped server, if you try to stop an already stopped server or start an already started server.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::ServerBootedException``.
    """

    _ice_id = "::MumbleServer::ServerBootedException"

_MumbleServer_ServerBootedException_t = IcePy.defineException(
    "::MumbleServer::ServerBootedException",
    ServerBootedException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(ServerBootedException, '_ice_type', _MumbleServer_ServerBootedException_t)

__all__ = ["ServerBootedException", "_MumbleServer_ServerBootedException_t"]
