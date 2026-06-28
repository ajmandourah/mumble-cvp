# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.ServerException import ServerException
from MumbleServer.ServerException import _MumbleServer_ServerException_t

from dataclasses import dataclass


@dataclass
class InvalidInputDataException(ServerException):
    """
    This is thrown when invalid input data was specified.
    
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::InvalidInputDataException``.
    """

    _ice_id = "::MumbleServer::InvalidInputDataException"

_MumbleServer_InvalidInputDataException_t = IcePy.defineException(
    "::MumbleServer::InvalidInputDataException",
    InvalidInputDataException,
    (),
    _MumbleServer_ServerException_t,
    ())

setattr(InvalidInputDataException, '_ice_type', _MumbleServer_InvalidInputDataException_t)

__all__ = ["InvalidInputDataException", "_MumbleServer_InvalidInputDataException_t"]
