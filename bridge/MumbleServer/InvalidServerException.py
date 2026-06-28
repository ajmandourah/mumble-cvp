# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidServerException(ServerException):
    """
    This is thrown when you try to do an operation on a server that does not exist. This may happen if someone has removed the server.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidServerException``.
    """

    _ice_id = "::MumbleServer::InvalidServerException"

_MumbleServer_InvalidServerException_t = IcePy.defineException(
    "::MumbleServer::InvalidServerException",
    InvalidServerException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidServerException, '_ice_type', _MumbleServer_InvalidServerException_t)

__all__ = ["InvalidServerException", "_MumbleServer_InvalidServerException_t"]
