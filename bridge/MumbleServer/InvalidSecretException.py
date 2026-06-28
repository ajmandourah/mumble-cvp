# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidSecretException(ServerException):
    """
    This is thrown when you supply the wrong secret in the calling context.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidSecretException``.
    """

    _ice_id = "::MumbleServer::InvalidSecretException"

_MumbleServer_InvalidSecretException_t = IcePy.defineException(
    "::MumbleServer::InvalidSecretException",
    InvalidSecretException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidSecretException, '_ice_type', _MumbleServer_InvalidSecretException_t)

__all__ = ["InvalidSecretException", "_MumbleServer_InvalidSecretException_t"]
