# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InternalErrorException(ServerException):
    """
    Thrown if the server encounters an internal error while processing the request
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InternalErrorException``.
    """

    _ice_id = "::MumbleServer::InternalErrorException"

_MumbleServer_InternalErrorException_t = IcePy.defineException(
    "::MumbleServer::InternalErrorException",
    InternalErrorException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InternalErrorException, '_ice_type', _MumbleServer_InternalErrorException_t)

__all__ = ["InternalErrorException", "_MumbleServer_InternalErrorException_t"]
