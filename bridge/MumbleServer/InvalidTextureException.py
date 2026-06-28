# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidTextureException(ServerException):
    """
    This is thrown when you try to set an invalid texture.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidTextureException``.
    """

    _ice_id = "::MumbleServer::InvalidTextureException"

_MumbleServer_InvalidTextureException_t = IcePy.defineException(
    "::MumbleServer::InvalidTextureException",
    InvalidTextureException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidTextureException, '_ice_type', _MumbleServer_InvalidTextureException_t)

__all__ = ["InvalidTextureException", "_MumbleServer_InvalidTextureException_t"]
