# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from enum import Enum

class DBState(Enum):
    """
    Different states of the underlying database
    
    Notes
    -----
        The Slice compiler generated this enum class from Slice enumeration ``::MumbleServer::DBState``.
    """

    Normal = 0

    ReadOnly = 1

_MumbleServer_DBState_t = IcePy.defineEnum(
    "::MumbleServer::DBState",
    DBState,
    (),
    {
        0: DBState.Normal,
        1: DBState.ReadOnly,
    }
)

__all__ = ["DBState", "_MumbleServer_DBState_t"]
