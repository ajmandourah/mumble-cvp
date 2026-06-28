# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidListenerException(ServerException):
    """
    This is thrown when the referenced channel listener does not actually exist
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidListenerException``.
    """

    _ice_id = "::MumbleServer::InvalidListenerException"

_MumbleServer_InvalidListenerException_t = IcePy.defineException(
    "::MumbleServer::InvalidListenerException",
    InvalidListenerException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidListenerException, '_ice_type', _MumbleServer_InvalidListenerException_t)

__all__ = ["InvalidListenerException", "_MumbleServer_InvalidListenerException_t"]
