# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidUserException(ServerException):
    """
    This is thrown when you specify an invalid userid.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidUserException``.
    """

    _ice_id = "::MumbleServer::InvalidUserException"

_MumbleServer_InvalidUserException_t = IcePy.defineException(
    "::MumbleServer::InvalidUserException",
    InvalidUserException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidUserException, '_ice_type', _MumbleServer_InvalidUserException_t)

__all__ = ["InvalidUserException", "_MumbleServer_InvalidUserException_t"]
