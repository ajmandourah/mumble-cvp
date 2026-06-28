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

from Ice.SliceChecksumDict import _Ice_SliceChecksumDict_t

from MumbleServer.ConfigMap import _MumbleServer_ConfigMap_t

from MumbleServer.DBState import _MumbleServer_DBState_t

from MumbleServer.InvalidCallbackException import _MumbleServer_InvalidCallbackException_t

from MumbleServer.InvalidSecretException import _MumbleServer_InvalidSecretException_t

from MumbleServer.MetaCallback_forward import _MumbleServer_MetaCallbackPrx_t

from MumbleServer.Meta_forward import _MumbleServer_MetaPrx_t

from MumbleServer.ReadOnlyModeException import _MumbleServer_ReadOnlyModeException_t

from MumbleServer.ServerList import _MumbleServer_ServerList_t

from MumbleServer.Server_forward import _MumbleServer_ServerPrx_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.DBState import DBState
    from MumbleServer.MetaCallback import MetaCallbackPrx
    from MumbleServer.Server import ServerPrx
    from collections.abc import Awaitable
    from collections.abc import Mapping
    from collections.abc import Sequence


class MetaPrx(ObjectPrx):
    """
    This is the meta interface. It is primarily used for retrieving the :class:`MumbleServer.ServerPrx` interfaces for each individual server.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::Meta``.
    """

    def getServer(self, id: int, context: dict[str, str] | None = None) -> ServerPrx | None:
        """
        Fetch interface to specific server.
        
        Parameters
        ----------
        id : int
            Server ID. See ``Server.getId``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        ServerPrx | None
            Interface for specified server, or a null proxy if id is invalid.
        """
        return Meta._op_getServer.invoke(self, ((id, ), context))

    def getServerAsync(self, id: int, context: dict[str, str] | None = None) -> Awaitable[ServerPrx | None]:
        """
        Fetch interface to specific server.
        
        Parameters
        ----------
        id : int
            Server ID. See ``Server.getId``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[ServerPrx | None]
            Interface for specified server, or a null proxy if id is invalid.
        """
        return Meta._op_getServer.invokeAsync(self, ((id, ), context))

    def newServer(self, context: dict[str, str] | None = None) -> ServerPrx | None:
        """
        Create a new server. Call ``Server.getId`` on the returned interface to find it's ID.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        ServerPrx | None
            Interface for new server.
        """
        return Meta._op_newServer.invoke(self, ((), context))

    def newServerAsync(self, context: dict[str, str] | None = None) -> Awaitable[ServerPrx | None]:
        """
        Create a new server. Call ``Server.getId`` on the returned interface to find it's ID.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[ServerPrx | None]
            Interface for new server.
        """
        return Meta._op_newServer.invokeAsync(self, ((), context))

    def getBootedServers(self, context: dict[str, str] | None = None) -> list[ServerPrx | None]:
        """
        Fetch list of all currently running servers.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[ServerPrx | None]
            List of interfaces for running servers.
        """
        return Meta._op_getBootedServers.invoke(self, ((), context))

    def getBootedServersAsync(self, context: dict[str, str] | None = None) -> Awaitable[list[ServerPrx | None]]:
        """
        Fetch list of all currently running servers.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[ServerPrx | None]]
            List of interfaces for running servers.
        """
        return Meta._op_getBootedServers.invokeAsync(self, ((), context))

    def getAllServers(self, context: dict[str, str] | None = None) -> list[ServerPrx | None]:
        """
        Fetch list of all defined servers.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[ServerPrx | None]
            List of interfaces for all servers.
        """
        return Meta._op_getAllServers.invoke(self, ((), context))

    def getAllServersAsync(self, context: dict[str, str] | None = None) -> Awaitable[list[ServerPrx | None]]:
        """
        Fetch list of all defined servers.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[ServerPrx | None]]
            List of interfaces for all servers.
        """
        return Meta._op_getAllServers.invokeAsync(self, ((), context))

    def getDefaultConf(self, context: dict[str, str] | None = None) -> dict[str, str]:
        """
        Fetch default configuration. This returns the configuration items that were set in the configuration file, or
        the built-in default. The individual servers will use these values unless they have been overridden in the
        server specific configuration. The only special case is the port, which defaults to the value defined here +
        the servers ID - 1 (so that virtual server #1 uses the defined port, server #2 uses port+1 etc).
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[str, str]
            Default configuration of the servers.
        """
        return Meta._op_getDefaultConf.invoke(self, ((), context))

    def getDefaultConfAsync(self, context: dict[str, str] | None = None) -> Awaitable[dict[str, str]]:
        """
        Fetch default configuration. This returns the configuration items that were set in the configuration file, or
        the built-in default. The individual servers will use these values unless they have been overridden in the
        server specific configuration. The only special case is the port, which defaults to the value defined here +
        the servers ID - 1 (so that virtual server #1 uses the defined port, server #2 uses port+1 etc).
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[str, str]]
            Default configuration of the servers.
        """
        return Meta._op_getDefaultConf.invokeAsync(self, ((), context))

    def getVersion(self, context: dict[str, str] | None = None) -> tuple[int, int, int, str]:
        """
        Fetch version of the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        tuple[int, int, int, str]
        
            A tuple containing:
                - int Major version.
                - int Minor version.
                - int Patchlevel.
                - str Textual representation of version. Note that this may not match the ``major``, ``minor`` and ``patch`` levels, as it
                  may be simply the compile date or the SVN revision. This is usually the text you want to present to users.
        """
        return Meta._op_getVersion.invoke(self, ((), context))

    def getVersionAsync(self, context: dict[str, str] | None = None) -> Awaitable[tuple[int, int, int, str]]:
        """
        Fetch version of the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[tuple[int, int, int, str]]
        
            A tuple containing:
                - int Major version.
                - int Minor version.
                - int Patchlevel.
                - str Textual representation of version. Note that this may not match the ``major``, ``minor`` and ``patch`` levels, as it
                  may be simply the compile date or the SVN revision. This is usually the text you want to present to users.
        """
        return Meta._op_getVersion.invokeAsync(self, ((), context))

    def addCallback(self, cb: MetaCallbackPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Add a callback. The callback will receive notifications when servers are started or stopped.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface which will receive notifications.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Meta._op_addCallback.invoke(self, ((cb, ), context))

    def addCallbackAsync(self, cb: MetaCallbackPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Add a callback. The callback will receive notifications when servers are started or stopped.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface which will receive notifications.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Meta._op_addCallback.invokeAsync(self, ((cb, ), context))

    def removeCallback(self, cb: MetaCallbackPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface to be removed.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Meta._op_removeCallback.invoke(self, ((cb, ), context))

    def removeCallbackAsync(self, cb: MetaCallbackPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface to be removed.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Meta._op_removeCallback.invokeAsync(self, ((cb, ), context))

    def getUptime(self, context: dict[str, str] | None = None) -> int:
        """
        Get the server's uptime.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            Uptime of the server in seconds
        """
        return Meta._op_getUptime.invoke(self, ((), context))

    def getUptimeAsync(self, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Get the server's uptime.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            Uptime of the server in seconds
        """
        return Meta._op_getUptime.invokeAsync(self, ((), context))

    def getSlice(self, context: dict[str, str] | None = None) -> str:
        """
        Get slice file.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        str
            Contents of the slice file server compiled with.
        """
        return Meta._op_getSlice.invoke(self, ((), context))

    def getSliceAsync(self, context: dict[str, str] | None = None) -> Awaitable[str]:
        """
        Get slice file.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[str]
            Contents of the slice file server compiled with.
        """
        return Meta._op_getSlice.invokeAsync(self, ((), context))

    def getSliceChecksums(self, context: dict[str, str] | None = None) -> dict[str, str]:
        """
        Returns a checksum dict for the slice file.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[str, str]
            Checksum dict
        """
        return Meta._op_getSliceChecksums.invoke(self, ((), context))

    def getSliceChecksumsAsync(self, context: dict[str, str] | None = None) -> Awaitable[dict[str, str]]:
        """
        Returns a checksum dict for the slice file.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[str, str]]
            Checksum dict
        """
        return Meta._op_getSliceChecksums.invokeAsync(self, ((), context))

    def getAssumedDatabaseState(self, context: dict[str, str] | None = None) -> DBState:
        return Meta._op_getAssumedDatabaseState.invoke(self, ((), context))

    def getAssumedDatabaseStateAsync(self, context: dict[str, str] | None = None) -> Awaitable[DBState]:
        return Meta._op_getAssumedDatabaseState.invokeAsync(self, ((), context))

    def setAssumedDatabaseState(self, state: DBState, context: dict[str, str] | None = None) -> None:
        """
        Sets the assumed state of the underlying database
        
        Parameters
        ----------
        state : DBState
        context : dict[str, str]
            The request context for the invocation.
        """
        return Meta._op_setAssumedDatabaseState.invoke(self, ((state, ), context))

    def setAssumedDatabaseStateAsync(self, state: DBState, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Sets the assumed state of the underlying database
        
        Parameters
        ----------
        state : DBState
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Meta._op_setAssumedDatabaseState.invokeAsync(self, ((state, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> MetaPrx | None:
        return checkedCast(MetaPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[MetaPrx | None ]:
        return checkedCastAsync(MetaPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> MetaPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> MetaPrx | None:
        return uncheckedCast(MetaPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::Meta"

IcePy.defineProxy("::MumbleServer::Meta", MetaPrx)

class Meta(Object, ABC):
    """
    This is the meta interface. It is primarily used for retrieving the :class:`MumbleServer.ServerPrx` interfaces for each individual server.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::Meta``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::Meta", )
    _op_getServer: IcePy.Operation
    _op_newServer: IcePy.Operation
    _op_getBootedServers: IcePy.Operation
    _op_getAllServers: IcePy.Operation
    _op_getDefaultConf: IcePy.Operation
    _op_getVersion: IcePy.Operation
    _op_addCallback: IcePy.Operation
    _op_removeCallback: IcePy.Operation
    _op_getUptime: IcePy.Operation
    _op_getSlice: IcePy.Operation
    _op_getSliceChecksums: IcePy.Operation
    _op_getAssumedDatabaseState: IcePy.Operation
    _op_setAssumedDatabaseState: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::Meta"

    @abstractmethod
    def getServer(self, id: int, current: Current) -> ServerPrx | None | Awaitable[ServerPrx | None]:
        """
        Fetch interface to specific server.
        
        Parameters
        ----------
        id : int
            Server ID. See ``Server.getId``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        ServerPrx | None | Awaitable[ServerPrx | None]
            Interface for specified server, or a null proxy if id is invalid.
        """
        pass

    @abstractmethod
    def newServer(self, current: Current) -> ServerPrx | None | Awaitable[ServerPrx | None]:
        """
        Create a new server. Call ``Server.getId`` on the returned interface to find it's ID.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        ServerPrx | None | Awaitable[ServerPrx | None]
            Interface for new server.
        """
        pass

    @abstractmethod
    def getBootedServers(self, current: Current) -> Sequence[ServerPrx | None] | Awaitable[Sequence[ServerPrx | None]]:
        """
        Fetch list of all currently running servers.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[ServerPrx | None] | Awaitable[Sequence[ServerPrx | None]]
            List of interfaces for running servers.
        """
        pass

    @abstractmethod
    def getAllServers(self, current: Current) -> Sequence[ServerPrx | None] | Awaitable[Sequence[ServerPrx | None]]:
        """
        Fetch list of all defined servers.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[ServerPrx | None] | Awaitable[Sequence[ServerPrx | None]]
            List of interfaces for all servers.
        """
        pass

    @abstractmethod
    def getDefaultConf(self, current: Current) -> Mapping[str, str] | Awaitable[Mapping[str, str]]:
        """
        Fetch default configuration. This returns the configuration items that were set in the configuration file, or
        the built-in default. The individual servers will use these values unless they have been overridden in the
        server specific configuration. The only special case is the port, which defaults to the value defined here +
        the servers ID - 1 (so that virtual server #1 uses the defined port, server #2 uses port+1 etc).
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[str, str] | Awaitable[Mapping[str, str]]
            Default configuration of the servers.
        """
        pass

    @abstractmethod
    def getVersion(self, current: Current) -> tuple[int, int, int, str] | Awaitable[tuple[int, int, int, str]]:
        """
        Fetch version of the server.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        tuple[int, int, int, str] | Awaitable[tuple[int, int, int, str]]
        
            A tuple containing:
                - int Major version.
                - int Minor version.
                - int Patchlevel.
                - str Textual representation of version. Note that this may not match the ``major``, ``minor`` and ``patch`` levels, as it
                  may be simply the compile date or the SVN revision. This is usually the text you want to present to users.
        """
        pass

    @abstractmethod
    def addCallback(self, cb: MetaCallbackPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Add a callback. The callback will receive notifications when servers are started or stopped.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface which will receive notifications.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def removeCallback(self, cb: MetaCallbackPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : MetaCallbackPrx | None
            Callback interface to be removed.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getUptime(self, current: Current) -> int | Awaitable[int]:
        """
        Get the server's uptime.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            Uptime of the server in seconds
        """
        pass

    @abstractmethod
    def getSlice(self, current: Current) -> str | Awaitable[str]:
        """
        Get slice file.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        str | Awaitable[str]
            Contents of the slice file server compiled with.
        """
        pass

    @abstractmethod
    def getSliceChecksums(self, current: Current) -> Mapping[str, str] | Awaitable[Mapping[str, str]]:
        """
        Returns a checksum dict for the slice file.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[str, str] | Awaitable[Mapping[str, str]]
            Checksum dict
        """
        pass

    @abstractmethod
    def getAssumedDatabaseState(self, current: Current) -> DBState | Awaitable[DBState]:
        pass

    @abstractmethod
    def setAssumedDatabaseState(self, state: DBState, current: Current) -> None | Awaitable[None]:
        """
        Sets the assumed state of the underlying database
        
        Parameters
        ----------
        state : DBState
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

Meta._op_getServer = IcePy.Operation(
    "getServer",
    "getServer",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_ServerPrx_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_newServer = IcePy.Operation(
    "newServer",
    "newServer",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ServerPrx_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_getBootedServers = IcePy.Operation(
    "getBootedServers",
    "getBootedServers",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ServerList_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_getAllServers = IcePy.Operation(
    "getAllServers",
    "getAllServers",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ServerList_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_getDefaultConf = IcePy.Operation(
    "getDefaultConf",
    "getDefaultConf",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ConfigMap_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_getVersion = IcePy.Operation(
    "getVersion",
    "getVersion",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)),
    None,
    (),
    False)

Meta._op_addCallback = IcePy.Operation(
    "addCallback",
    "addCallback",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_MetaCallbackPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Meta._op_removeCallback = IcePy.Operation(
    "removeCallback",
    "removeCallback",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_MetaCallbackPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Meta._op_getUptime = IcePy.Operation(
    "getUptime",
    "getUptime",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

Meta._op_getSlice = IcePy.Operation(
    "getSlice",
    "getSlice",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_string, False, 0),
    (),
    False)

Meta._op_getSliceChecksums = IcePy.Operation(
    "getSliceChecksums",
    "getSliceChecksums",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _Ice_SliceChecksumDict_t, False, 0),
    (),
    False)

Meta._op_getAssumedDatabaseState = IcePy.Operation(
    "getAssumedDatabaseState",
    "getAssumedDatabaseState",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_DBState_t, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Meta._op_setAssumedDatabaseState = IcePy.Operation(
    "setAssumedDatabaseState",
    "setAssumedDatabaseState",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_DBState_t, False, 0),),
    (),
    None,
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

__all__ = ["Meta", "MetaPrx", "_MumbleServer_MetaPrx_t"]
