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

from MumbleServer.ServerContextCallback_forward import _MumbleServer_ServerContextCallbackPrx_t

from MumbleServer.User import _MumbleServer_User_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.User import User
    from collections.abc import Awaitable
    from collections.abc import Sequence


class ServerContextCallbackPrx(ObjectPrx):
    """
    Callback interface for context actions. You need to supply one of these for ``Server.addContext``.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::ServerContextCallback``.
    """

    def contextAction(self, action: str, usr: User, session: int, channelid: int, context: dict[str, str] | None = None) -> None:
        """
        Called when a context action is performed.
        
        Parameters
        ----------
        action : str
            Action to be performed.
        usr : User
            User which initiated the action.
        session : int
            If nonzero, session of target user.
        channelid : int
            If not -1, id of target channel.
        context : dict[str, str]
            The request context for the invocation.
        """
        return ServerContextCallback._op_contextAction.invoke(self, ((action, usr, session, channelid), context))

    def contextActionAsync(self, action: str, usr: User, session: int, channelid: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a context action is performed.
        
        Parameters
        ----------
        action : str
            Action to be performed.
        usr : User
            User which initiated the action.
        session : int
            If nonzero, session of target user.
        channelid : int
            If not -1, id of target channel.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return ServerContextCallback._op_contextAction.invokeAsync(self, ((action, usr, session, channelid), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ServerContextCallbackPrx | None:
        return checkedCast(ServerContextCallbackPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ServerContextCallbackPrx | None ]:
        return checkedCastAsync(ServerContextCallbackPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ServerContextCallbackPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ServerContextCallbackPrx | None:
        return uncheckedCast(ServerContextCallbackPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerContextCallback"

IcePy.defineProxy("::MumbleServer::ServerContextCallback", ServerContextCallbackPrx)

class ServerContextCallback(Object, ABC):
    """
    Callback interface for context actions. You need to supply one of these for ``Server.addContext``.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::ServerContextCallback``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::ServerContextCallback", )
    _op_contextAction: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerContextCallback"

    @abstractmethod
    def contextAction(self, action: str, usr: User, session: int, channelid: int, current: Current) -> None | Awaitable[None]:
        """
        Called when a context action is performed.
        
        Parameters
        ----------
        action : str
            Action to be performed.
        usr : User
            User which initiated the action.
        session : int
            If nonzero, session of target user.
        channelid : int
            If not -1, id of target channel.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

ServerContextCallback._op_contextAction = IcePy.Operation(
    "contextAction",
    "contextAction",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), _MumbleServer_User_t, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    None,
    (),
    False)

__all__ = ["ServerContextCallback", "ServerContextCallbackPrx", "_MumbleServer_ServerContextCallbackPrx_t"]
