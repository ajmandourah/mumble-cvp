# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidSessionException(ServerException):
    """
    This is thrown when you specify an invalid session. This may happen if the user has disconnected since your last call to ``Server.getUsers``. See ``User.session``
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidSessionException``.
    """

    _ice_id = "::MumbleServer::InvalidSessionException"

_MumbleServer_InvalidSessionException_t = IcePy.defineException(
    "::MumbleServer::InvalidSessionException",
    InvalidSessionException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidSessionException, '_ice_type', _MumbleServer_InvalidSessionException_t)

__all__ = ["InvalidSessionException", "_MumbleServer_InvalidSessionException_t"]
