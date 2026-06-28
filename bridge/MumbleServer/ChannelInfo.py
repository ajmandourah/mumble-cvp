# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from enum import Enum

class ChannelInfo(Enum):
    """
    Notes
    -----
        The Slice compiler generated this enum class from Slice enumeration ``::MumbleServer::ChannelInfo``.
    """

    ChannelDescription = 0

    ChannelPosition = 1

_MumbleServer_ChannelInfo_t = IcePy.defineEnum(
    "::MumbleServer::ChannelInfo",
    ChannelInfo,
    (),
    {
        0: ChannelInfo.ChannelDescription,
        1: ChannelInfo.ChannelPosition,
    }
)

__all__ = ["ChannelInfo", "_MumbleServer_ChannelInfo_t"]
