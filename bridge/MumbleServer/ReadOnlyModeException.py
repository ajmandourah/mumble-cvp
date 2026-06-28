# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class ReadOnlyModeException(ServerException):
    """
    This is thrown when the server has its database in read-only mode and whatever you requested is incompatible with that.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::ReadOnlyModeException``.
    """

    _ice_id = "::MumbleServer::ReadOnlyModeException"

_MumbleServer_ReadOnlyModeException_t = IcePy.defineException(
    "::MumbleServer::ReadOnlyModeException",
    ReadOnlyModeException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(ReadOnlyModeException, '_ice_type', _MumbleServer_ReadOnlyModeException_t)

__all__ = ["ReadOnlyModeException", "_MumbleServer_ReadOnlyModeException_t"]
