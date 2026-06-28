# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from enum import Enum

class UserInfo(Enum):
    """
    Notes
    -----
        The Slice compiler generated this enum class from Slice enumeration ``::MumbleServer::UserInfo``.
    """

    UserName = 0

    UserEmail = 1

    UserComment = 2

    UserHash = 3

    UserPassword = 4

    UserLastActive = 5

    UserKDFIterations = 6

_MumbleServer_UserInfo_t = IcePy.defineEnum(
    "::MumbleServer::UserInfo",
    UserInfo,
    (),
    {
        0: UserInfo.UserName,
        1: UserInfo.UserEmail,
        2: UserInfo.UserComment,
        3: UserInfo.UserHash,
        4: UserInfo.UserPassword,
        5: UserInfo.UserLastActive,
        6: UserInfo.UserKDFIterations,
    }
)

__all__ = ["UserInfo", "_MumbleServer_UserInfo_t"]
