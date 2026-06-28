# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class ServerFailureException(ServerException):
    """
    This is thrown if ``Server.start`` fails, and should generally be the cause for some concern.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::ServerFailureException``.
    """

    _ice_id = "::MumbleServer::ServerFailureException"

_MumbleServer_ServerFailureException_t = IcePy.defineException(
    "::MumbleServer::ServerFailureException",
    ServerFailureException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(ServerFailureException, '_ice_type', _MumbleServer_ServerFailureException_t)

__all__ = ["ServerFailureException", "_MumbleServer_ServerFailureException_t"]
