# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.IntList import _MumbleServer_IntList_t

from dataclasses import dataclass
from dataclasses import field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Buffer


@dataclass
class TextMessage:
    """
    A text message between users.
    
    Attributes
    ----------
    sessions : list[int]
        Sessions (connected users) who were sent this message.
    channels : list[int]
        Channels who were sent this message.
    trees : list[int]
        Trees of channels who were sent this message.
    text : str
        The contents of the message.
    
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::MumbleServer::TextMessage``.
    """
    sessions: list[int] = field(default_factory=list)
    channels: list[int] = field(default_factory=list)
    trees: list[int] = field(default_factory=list)
    text: str = ""

_MumbleServer_TextMessage_t = IcePy.defineStruct(
    "::MumbleServer::TextMessage",
    TextMessage,
    (),
    (
        ("sessions", (), _MumbleServer_IntList_t),
        ("channels", (), _MumbleServer_IntList_t),
        ("trees", (), _MumbleServer_IntList_t),
        ("text", (), IcePy._t_string)
    ))

__all__ = ["TextMessage", "_MumbleServer_TextMessage_t"]
