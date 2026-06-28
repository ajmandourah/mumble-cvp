# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from Ice import UserException

from dataclasses import dataclass


@dataclass
class ServerException(UserException):
    """
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::MumbleServer::ServerException``.
    """

    _ice_id = "::MumbleServer::ServerException"

_MumbleServer_ServerException_t = IcePy.defineException(
    "::MumbleServer::ServerException",
    ServerException,
    (),
    None,
    ())

setattr(ServerException, '_ice_type', _MumbleServer_ServerException_t)

__all__ = ["ServerException", "_MumbleServer_ServerException_t"]
