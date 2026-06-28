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

from MumbleServer.MetaCallback_forward import _MumbleServer_MetaCallbackPrx_t

from MumbleServer.Server_forward import _MumbleServer_ServerPrx_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.Server import ServerPrx
    from collections.abc import Awaitable
    from collections.abc import Sequence


class MetaCallbackPrx(ObjectPrx):
    """
    Callback interface for Meta. You can supply an implementation of this to receive notifications
    when servers are stopped or started.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::MetaCallback``.
    
    See Also
    --------
        :class:`MumbleServer.ServerCallbackPrx`
        ``Meta.addCallback``
    """

    def started(self, srv: ServerPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Called when a server is started. The server is up and running when this event is sent, so all methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        context : dict[str, str]
            The request context for the invocation.
        """
        return MetaCallback._op_started.invoke(self, ((srv, ), context))

    def startedAsync(self, srv: ServerPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a server is started. The server is up and running when this event is sent, so all methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return MetaCallback._op_started.invokeAsync(self, ((srv, ), context))

    def stopped(self, srv: ServerPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Called when a server is stopped. The server is already stopped when this event is sent, so no methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        context : dict[str, str]
            The request context for the invocation.
        """
        return MetaCallback._op_stopped.invoke(self, ((srv, ), context))

    def stoppedAsync(self, srv: ServerPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Called when a server is stopped. The server is already stopped when this event is sent, so no methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return MetaCallback._op_stopped.invokeAsync(self, ((srv, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> MetaCallbackPrx | None:
        return checkedCast(MetaCallbackPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[MetaCallbackPrx | None ]:
        return checkedCastAsync(MetaCallbackPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> MetaCallbackPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> MetaCallbackPrx | None:
        return uncheckedCast(MetaCallbackPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::MetaCallback"

IcePy.defineProxy("::MumbleServer::MetaCallback", MetaCallbackPrx)

class MetaCallback(Object, ABC):
    """
    Callback interface for Meta. You can supply an implementation of this to receive notifications
    when servers are stopped or started.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that all callbacks are done asynchronously; the server does not wait for the callback to
    complete before continuing processing.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::MetaCallback``.
    
    See Also
    --------
        :class:`MumbleServer.ServerCallbackPrx`
        ``Meta.addCallback``
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::MetaCallback", )
    _op_started: IcePy.Operation
    _op_stopped: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::MetaCallback"

    @abstractmethod
    def started(self, srv: ServerPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Called when a server is started. The server is up and running when this event is sent, so all methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def stopped(self, srv: ServerPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Called when a server is stopped. The server is already stopped when this event is sent, so no methods that
        need a running server will work.
        
        Parameters
        ----------
        srv : ServerPrx | None
            Interface for started server.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

MetaCallback._op_started = IcePy.Operation(
    "started",
    "started",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerPrx_t, False, 0),),
    (),
    None,
    (),
    False)

MetaCallback._op_stopped = IcePy.Operation(
    "stopped",
    "stopped",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerPrx_t, False, 0),),
    (),
    None,
    (),
    False)

__all__ = ["MetaCallback", "MetaCallbackPrx", "_MumbleServer_MetaCallbackPrx_t"]
