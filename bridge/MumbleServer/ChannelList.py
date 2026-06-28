# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.Channel import _MumbleServer_Channel_t

_MumbleServer_ChannelList_t = IcePy.defineSequence("::MumbleServer::ChannelList", (), _MumbleServer_Channel_t)

__all__ = ["_MumbleServer_ChannelList_t"]
