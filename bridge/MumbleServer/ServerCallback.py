# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from Ice.Object import Object

from Ice.ObjectPrx import ObjectPrx
from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from MumbleServer.Channel import _MumbleServer_Channel_t

from MumbleServer.ServerCallback_forward import _MumbleServer_ServerCallbackPrx_t

from MumbleServer.TextMessage import _MumbleServer_TextMessage_t

from MumbleServer.User import _MumbleServer_User_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.Channel import Channel
    from MumbleServer.TextMessage import TextMessage
    from MumbleServer.User import User
    from collections.abc import Awaitable
    from collections.abc import Sequence


class ServerCallbackPrx(ObjectPrx):
    """
    Callback interface for servers. You can supply an implementation of this to receive notification
    messages from the server.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    Note that callbacks are removed when a server is stopped, so you should have a callback for
    ``MetaCallback.started`` which calls ``Server.addCallback``.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::ServerCallback``.
    
    See Also
    --------
        :class:`MumbleServer.MetaCallbackPrx`
        ``Server.addCallback``
    """

    def userConnected(self, state: User, context: dict[str, str] | None = None) -> None:
        """
        Called when a user connects to the server.
        
        Parameters
        ----------
        state : User
            State of connected user.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_userConnected.invoke(self, ((state, ), context))

    def userConnectedAsync(self, state: User, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a user connects to the server.
        
        Parameters
        ----------
        state : User
            State of connected user.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_userConnected.invokeAsync(self, ((state, ), context))

    def userDisconnected(self, state: User, context: dict[str, str] | None = None) -> None:
        """
        Called when a user disconnects from the server. The user has already been removed, so you can no longer use methods like ``Server.getState``
        to retrieve the user's state.
        
        Parameters
        ----------
        state : User
            State of disconnected user.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_userDisconnected.invoke(self, ((state, ), context))

    def userDisconnectedAsync(self, state: User, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a user disconnects from the server. The user has already been removed, so you can no longer use methods like ``Server.getState``
        to retrieve the user's state.
        
        Parameters
        ----------
        state : User
            State of disconnected user.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_userDisconnected.invokeAsync(self, ((state, ), context))

    def userStateChanged(self, state: User, context: dict[str, str] | None = None) -> None:
        """
        Called when a user state changes. This is called if the user moves, is renamed, is muted, deafened etc.
        
        Parameters
        ----------
        state : User
            New state of user.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_userStateChanged.invoke(self, ((state, ), context))

    def userStateChangedAsync(self, state: User, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a user state changes. This is called if the user moves, is renamed, is muted, deafened etc.
        
        Parameters
        ----------
        state : User
            New state of user.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_userStateChanged.invokeAsync(self, ((state, ), context))

    def userTextMessage(self, state: User, message: TextMessage, context: dict[str, str] | None = None) -> None:
        """
        Called when user writes a text message
        
        Parameters
        ----------
        state : User
            the User sending the message
        message : TextMessage
            the TextMessage the user has sent
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_userTextMessage.invoke(self, ((state, message), context))

    def userTextMessageAsync(self, state: User, message: TextMessage, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when user writes a text message
        
        Parameters
        ----------
        state : User
            the User sending the message
        message : TextMessage
            the TextMessage the user has sent
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_userTextMessage.invokeAsync(self, ((state, message), context))

    def channelCreated(self, state: Channel, context: dict[str, str] | None = None) -> None:
        """
        Called when a new channel is created.
        
        Parameters
        ----------
        state : Channel
            State of new channel.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_channelCreated.invoke(self, ((state, ), context))

    def channelCreatedAsync(self, state: Channel, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a new channel is created.
        
        Parameters
        ----------
        state : Channel
            State of new channel.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_channelCreated.invokeAsync(self, ((state, ), context))

    def channelRemoved(self, state: Channel, context: dict[str, str] | None = None) -> None:
        """
        Called when a channel is removed. The channel has already been removed, you can no longer use methods like ``Server.getChannelState``
        
        Parameters
        ----------
        state : Channel
            State of removed channel.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_channelRemoved.invoke(self, ((state, ), context))

    def channelRemovedAsync(self, state: Channel, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a channel is removed. The channel has already been removed, you can no longer use methods like ``Server.getChannelState``
        
        Parameters
        ----------
        state : Channel
            State of removed channel.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_channelRemoved.invokeAsync(self, ((state, ), context))

    def channelStateChanged(self, state: Channel, context: dict[str, str] | None = None) -> None:
        """
        Called when a new channel state changes. This is called if the channel is moved, renamed or if new links are added.
        
        Parameters
        ----------
        state : Channel
            New state of channel.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerCallback._op_channelStateChanged.invoke(self, ((state, ), context))

    def channelStateChangedAsync(self, state: Channel, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a new channel state changes. This is called if the channel is moved, renamed or if new links are added.
        
        Parameters
        ----------
        state : Channel
            New state of channel.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerCallback._op_channelStateChanged.invokeAsync(self, ((state, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ServerCallbackPrx | None:
        return checkedCast(ServerCallbackPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ServerCallbackPrx | None ]:
        return checkedCastAsync(ServerCallbackPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ServerCallbackPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ServerCallbackPrx | None:
        return uncheckedCast(ServerCallbackPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerCallback"

IcePy.defineProxy("::MumbleServer::ServerCallback", ServerCallbackPrx)

class ServerCallback(Object, ABC):
    """
    Callback interface for servers. You can supply an implementation of this to receive notification
    messages from the server.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    Note that callbacks are removed when a server is stopped, so you should have a callback for
    ``MetaCallback.started`` which calls ``Server.addCallback``.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::ServerCallback``.
    
    See Also
    --------
        :class:`MumbleServer.MetaCallbackPrx`
        ``Server.addCallback``
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::ServerCallback", )
    _op_userConnected: IcePy.Operation
    _op_userDisconnected: IcePy.Operation
    _op_userStateChanged: IcePy.Operation
    _op_userTextMessage: IcePy.Operation
    _op_channelCreated: IcePy.Operation
    _op_channelRemoved: IcePy.Operation
    _op_channelStateChanged: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerCallback"

    @abstractmethod
    def userConnected(self, state: User, current: Current) -> None | Awaitable[None]:
        """
        Called when a user connects to the server.
        
        Parameters
        ----------
        state : User
            State of connected user.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def userDisconnected(self, state: User, current: Current) -> None | Awaitable[None]:
        """
        Called when a user disconnects from the server. The user has already been removed, so you can no longer use methods like ``Server.getState``
        to retrieve the user's state.
        
        Parameters
        ----------
        state : User
            State of disconnected user.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def userStateChanged(self, state: User, current: Current) -> None | Awaitable[None]:
        """
        Called when a user state changes. This is called if the user moves, is renamed, is muted, deafened etc.
        
        Parameters
        ----------
        state : User
            New state of user.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def userTextMessage(self, state: User, message: TextMessage, current: Current) -> None | Awaitable[None]:
        """
        Called when user writes a text message
        
        Parameters
        ----------
        state : User
            the User sending the message
        message : TextMessage
            the TextMessage the user has sent
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def channelCreated(self, state: Channel, current: Current) -> None | Awaitable[None]:
        """
        Called when a new channel is created.
        
        Parameters
        ----------
        state : Channel
            State of new channel.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def channelRemoved(self, state: Channel, current: Current) -> None | Awaitable[None]:
        """
        Called when a channel is removed. The channel has already been removed, you can no longer use methods like ``Server.getChannelState``
        
        Parameters
        ----------
        state : Channel
            State of removed channel.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def channelStateChanged(self, state: Channel, current: Current) -> None | Awaitable[None]:
        """
        Called when a new channel state changes. This is called if the channel is moved, renamed or if new links are added.
        
        Parameters
        ----------
        state : Channel
            New state of channel.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

ServerCallback._op_userConnected = IcePy.Operation(
    "userConnected",
    "userConnected",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_User_t, False, 0),),
    (),
    None,
    (),
    False)

ServerCallback._op_userDisconnected = IcePy.Operation(
    "userDisconnected",
    "userDisconnected",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_User_t, False, 0),),
    (),
    None,
    (),
    False)

ServerCallback._op_userStateChanged = IcePy.Operation(
    "userStateChanged",
    "userStateChanged",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_User_t, False, 0),),
    (),
    None,
    (),
    False)

ServerCallback._op_userTextMessage = IcePy.Operation(
    "userTextMessage",
    "userTextMessage",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_User_t, False, 0), ((), _MumbleServer_TextMessage_t, False, 0)),
    (),
    None,
    (),
    False)

ServerCallback._op_channelCreated = IcePy.Operation(
    "channelCreated",
    "channelCreated",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_Channel_t, False, 0),),
    (),
    None,
    (),
    False)

ServerCallback._op_channelRemoved = IcePy.Operation(
    "channelRemoved",
    "channelRemoved",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_Channel_t, False, 0),),
    (),
    None,
    (),
    False)

ServerCallback._op_channelStateChanged = IcePy.Operation(
    "channelStateChanged",
    "channelStateChanged",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_Channel_t, False, 0),),
    (),
    None,
    (),
    False)

__all__ = ["ServerCallback", "ServerCallbackPrx", "_MumbleServer_ServerCallbackPrx_t"]
