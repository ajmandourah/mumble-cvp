# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidCallbackException(ServerException):
    """
    This is thrown when you supply an invalid callback.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidCallbackException``.
    """

    _ice_id = "::MumbleServer::InvalidCallbackException"

_MumbleServer_InvalidCallbackException_t = IcePy.defineException(
    "::MumbleServer::InvalidCallbackException",
    InvalidCallbackException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidCallbackException, '_ice_type', _MumbleServer_InvalidCallbackException_t)

__all__ = ["InvalidCallbackException", "_MumbleServer_InvalidCallbackException_t"]
