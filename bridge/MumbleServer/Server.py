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

from MumbleServer.ACLList import _MumbleServer_ACLList_t

from MumbleServer.BanList import _MumbleServer_BanList_t

from MumbleServer.CertificateList import _MumbleServer_CertificateList_t

from MumbleServer.Channel import _MumbleServer_Channel_t

from MumbleServer.ChannelMap import _MumbleServer_ChannelMap_t

from MumbleServer.ConfigMap import _MumbleServer_ConfigMap_t

from MumbleServer.GroupList import _MumbleServer_GroupList_t

from MumbleServer.IdList import _MumbleServer_IdList_t

from MumbleServer.IdMap import _MumbleServer_IdMap_t

from MumbleServer.IntList import _MumbleServer_IntList_t

from MumbleServer.InvalidCallbackException import _MumbleServer_InvalidCallbackException_t

from MumbleServer.InvalidChannelException import _MumbleServer_InvalidChannelException_t

from MumbleServer.InvalidInputDataException import _MumbleServer_InvalidInputDataException_t

from MumbleServer.InvalidSecretException import _MumbleServer_InvalidSecretException_t

from MumbleServer.InvalidSessionException import _MumbleServer_InvalidSessionException_t

from MumbleServer.InvalidTextureException import _MumbleServer_InvalidTextureException_t

from MumbleServer.InvalidUserException import _MumbleServer_InvalidUserException_t

from MumbleServer.LogList import _MumbleServer_LogList_t

from MumbleServer.NameList import _MumbleServer_NameList_t

from MumbleServer.NameMap import _MumbleServer_NameMap_t

from MumbleServer.NestingLimitException import _MumbleServer_NestingLimitException_t

from MumbleServer.ReadOnlyModeException import _MumbleServer_ReadOnlyModeException_t

from MumbleServer.ServerAuthenticator_forward import _MumbleServer_ServerAuthenticatorPrx_t

from MumbleServer.ServerBootedException import _MumbleServer_ServerBootedException_t

from MumbleServer.ServerCallback_forward import _MumbleServer_ServerCallbackPrx_t

from MumbleServer.ServerContextCallback_forward import _MumbleServer_ServerContextCallbackPrx_t

from MumbleServer.ServerFailureException import _MumbleServer_ServerFailureException_t

from MumbleServer.Server_forward import _MumbleServer_ServerPrx_t

from MumbleServer.Texture import _MumbleServer_Texture_t

from MumbleServer.Tree_forward import _MumbleServer_Tree_t

from MumbleServer.User import _MumbleServer_User_t

from MumbleServer.UserInfoMap import _MumbleServer_UserInfoMap_t

from MumbleServer.UserMap import _MumbleServer_UserMap_t

from MumbleServer.WriteOnlyException import _MumbleServer_WriteOnlyException_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.ACL import ACL
    from MumbleServer.Ban import Ban
    from MumbleServer.Channel import Channel
    from MumbleServer.Group import Group
    from MumbleServer.LogEntry import LogEntry
    from MumbleServer.ServerAuthenticator import ServerAuthenticatorPrx
    from MumbleServer.ServerCallback import ServerCallbackPrx
    from MumbleServer.ServerContextCallback import ServerContextCallbackPrx
    from MumbleServer.Tree import Tree
    from MumbleServer.User import User
    from MumbleServer.UserInfo import UserInfo
    from collections.abc import Awaitable
    from collections.abc import Buffer
    from collections.abc import Mapping
    from collections.abc import Sequence


class ServerPrx(ObjectPrx):
    """
    Per-server interface. This includes all methods for configuring and altering
    the state of a single virtual server. You can retrieve a pointer to this interface
    from one of the methods in :class:`MumbleServer.MetaPrx`.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::Server``.
    """

    def isRunning(self, context: dict[str, str] | None = None) -> bool:
        """
        Shows if the server currently running (accepting users).
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        bool
            Run-state of server.
        """
        return Server._op_isRunning.invoke(self, ((), context))

    def isRunningAsync(self, context: dict[str, str] | None = None) -> Awaitable[bool]:
        """
        Shows if the server currently running (accepting users).
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[bool]
            Run-state of server.
        """
        return Server._op_isRunning.invokeAsync(self, ((), context))

    def start(self, context: dict[str, str] | None = None) -> None:
        """
        Start server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_start.invoke(self, ((), context))

    def startAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Start server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_start.invokeAsync(self, ((), context))

    def stop(self, context: dict[str, str] | None = None) -> None:
        """
        Stop server.
        Note: Server will be restarted on application restart unless explicitly disabled
        with setConf("boot", false)
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_stop.invoke(self, ((), context))

    def stopAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Stop server.
        Note: Server will be restarted on application restart unless explicitly disabled
        with setConf("boot", false)
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_stop.invokeAsync(self, ((), context))

    def delete(self, context: dict[str, str] | None = None) -> None:
        """
        Delete server and all it's configuration.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_delete.invoke(self, ((), context))

    def deleteAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Delete server and all it's configuration.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_delete.invokeAsync(self, ((), context))

    def id(self, context: dict[str, str] | None = None) -> int:
        """
        Fetch the server id.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            Unique server id.
        """
        return Server._op_id.invoke(self, ((), context))

    def idAsync(self, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Fetch the server id.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            Unique server id.
        """
        return Server._op_id.invokeAsync(self, ((), context))

    def addCallback(self, cb: ServerCallbackPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Add a callback. The callback will receive notifications about changes to users and channels.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface which will receive notifications.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeCallbackAsync`
        """
        return Server._op_addCallback.invoke(self, ((cb, ), context))

    def addCallbackAsync(self, cb: ServerCallbackPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Add a callback. The callback will receive notifications about changes to users and channels.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface which will receive notifications.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeCallbackAsync`
        """
        return Server._op_addCallback.invokeAsync(self, ((cb, ), context))

    def removeCallback(self, cb: ServerCallbackPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface to be removed.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addCallbackAsync`
        """
        return Server._op_removeCallback.invoke(self, ((cb, ), context))

    def removeCallbackAsync(self, cb: ServerCallbackPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface to be removed.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addCallbackAsync`
        """
        return Server._op_removeCallback.invokeAsync(self, ((cb, ), context))

    def setAuthenticator(self, auth: ServerAuthenticatorPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Set external authenticator. If set, all authentications from clients are forwarded to this
        proxy.
        
        Parameters
        ----------
        auth : ServerAuthenticatorPrx | None
            Authenticator object to perform subsequent authentications.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setAuthenticator.invoke(self, ((auth, ), context))

    def setAuthenticatorAsync(self, auth: ServerAuthenticatorPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set external authenticator. If set, all authentications from clients are forwarded to this
        proxy.
        
        Parameters
        ----------
        auth : ServerAuthenticatorPrx | None
            Authenticator object to perform subsequent authentications.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setAuthenticator.invokeAsync(self, ((auth, ), context))

    def getConf(self, key: str, context: dict[str, str] | None = None) -> str:
        """
        Retrieve configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        str
            Configuration value. If this is empty, see ``Meta.getDefaultConf``
        """
        return Server._op_getConf.invoke(self, ((key, ), context))

    def getConfAsync(self, key: str, context: dict[str, str] | None = None) -> Awaitable[str]:
        """
        Retrieve configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[str]
            Configuration value. If this is empty, see ``Meta.getDefaultConf``
        """
        return Server._op_getConf.invokeAsync(self, ((key, ), context))

    def getAllConf(self, context: dict[str, str] | None = None) -> dict[str, str]:
        """
        Retrieve all configuration items.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[str, str]
            All configured values. If a value isn't set here, the value from ``Meta.getDefaultConf`` is used.
        """
        return Server._op_getAllConf.invoke(self, ((), context))

    def getAllConfAsync(self, context: dict[str, str] | None = None) -> Awaitable[dict[str, str]]:
        """
        Retrieve all configuration items.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[str, str]]
            All configured values. If a value isn't set here, the value from ``Meta.getDefaultConf`` is used.
        """
        return Server._op_getAllConf.invokeAsync(self, ((), context))

    def setConf(self, key: str, value: str, context: dict[str, str] | None = None) -> None:
        """
        Set a configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        value : str
            Configuration value.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setConf.invoke(self, ((key, value), context))

    def setConfAsync(self, key: str, value: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set a configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        value : str
            Configuration value.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setConf.invokeAsync(self, ((key, value), context))

    def setSuperuserPassword(self, pw: str, context: dict[str, str] | None = None) -> None:
        """
        Set superuser password. This is just a convenience for using :meth:`MumbleServer.ServerPrx.updateRegistrationAsync` on user id 0.
        
        Parameters
        ----------
        pw : str
            Password.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setSuperuserPassword.invoke(self, ((pw, ), context))

    def setSuperuserPasswordAsync(self, pw: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set superuser password. This is just a convenience for using :meth:`MumbleServer.ServerPrx.updateRegistrationAsync` on user id 0.
        
        Parameters
        ----------
        pw : str
            Password.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setSuperuserPassword.invokeAsync(self, ((pw, ), context))

    def getLog(self, first: int, last: int, context: dict[str, str] | None = None) -> list[LogEntry]:
        """
        Fetch log entries.
        
        Parameters
        ----------
        first : int
            Lowest numbered entry to fetch. 0 is the most recent item.
        last : int
            Last entry to fetch.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[LogEntry]
            List of log entries.
        """
        return Server._op_getLog.invoke(self, ((first, last), context))

    def getLogAsync(self, first: int, last: int, context: dict[str, str] | None = None) -> Awaitable[list[LogEntry]]:
        """
        Fetch log entries.
        
        Parameters
        ----------
        first : int
            Lowest numbered entry to fetch. 0 is the most recent item.
        last : int
            Last entry to fetch.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[LogEntry]]
            List of log entries.
        """
        return Server._op_getLog.invokeAsync(self, ((first, last), context))

    def getLogLen(self, context: dict[str, str] | None = None) -> int:
        """
        Fetch length of log
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            Number of entries in log
        """
        return Server._op_getLogLen.invoke(self, ((), context))

    def getLogLenAsync(self, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Fetch length of log
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            Number of entries in log
        """
        return Server._op_getLogLen.invokeAsync(self, ((), context))

    def getUsers(self, context: dict[str, str] | None = None) -> dict[int, User]:
        """
        Fetch all users. This returns all currently connected users on the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[int, User]
            List of connected users.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        return Server._op_getUsers.invoke(self, ((), context))

    def getUsersAsync(self, context: dict[str, str] | None = None) -> Awaitable[dict[int, User]]:
        """
        Fetch all users. This returns all currently connected users on the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[int, User]]
            List of connected users.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        return Server._op_getUsers.invokeAsync(self, ((), context))

    def getChannels(self, context: dict[str, str] | None = None) -> dict[int, Channel]:
        """
        Fetch all channels. This returns all defined channels on the server. The root channel is always channel 0.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[int, Channel]
            List of defined channels.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        return Server._op_getChannels.invoke(self, ((), context))

    def getChannelsAsync(self, context: dict[str, str] | None = None) -> Awaitable[dict[int, Channel]]:
        """
        Fetch all channels. This returns all defined channels on the server. The root channel is always channel 0.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[int, Channel]]
            List of defined channels.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        return Server._op_getChannels.invokeAsync(self, ((), context))

    def getCertificateList(self, session: int, context: dict[str, str] | None = None) -> list[bytes]:
        """
        Fetch certificate of user. This returns the complete certificate chain of a user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[bytes]
            Certificate list of user.
        """
        return Server._op_getCertificateList.invoke(self, ((session, ), context))

    def getCertificateListAsync(self, session: int, context: dict[str, str] | None = None) -> Awaitable[list[bytes]]:
        """
        Fetch certificate of user. This returns the complete certificate chain of a user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[bytes]]
            Certificate list of user.
        """
        return Server._op_getCertificateList.invokeAsync(self, ((session, ), context))

    def getTree(self, context: dict[str, str] | None = None) -> Tree | None:
        """
        Fetch all channels and connected users as a tree. This retrieves an easy-to-use representation of the server
        as a tree. This is primarily used for viewing the state of the server on a webpage.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Tree | None
            Recursive tree of all channels and connected users.
        """
        return Server._op_getTree.invoke(self, ((), context))

    def getTreeAsync(self, context: dict[str, str] | None = None) -> Awaitable[Tree | None]:
        """
        Fetch all channels and connected users as a tree. This retrieves an easy-to-use representation of the server
        as a tree. This is primarily used for viewing the state of the server on a webpage.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[Tree | None]
            Recursive tree of all channels and connected users.
        """
        return Server._op_getTree.invokeAsync(self, ((), context))

    def getBans(self, context: dict[str, str] | None = None) -> list[Ban]:
        """
        Fetch all current IP bans on the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[Ban]
            List of bans.
        """
        return Server._op_getBans.invoke(self, ((), context))

    def getBansAsync(self, context: dict[str, str] | None = None) -> Awaitable[list[Ban]]:
        """
        Fetch all current IP bans on the server.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[Ban]]
            List of bans.
        """
        return Server._op_getBans.invokeAsync(self, ((), context))

    def setBans(self, bans: Sequence[Ban], context: dict[str, str] | None = None) -> None:
        """
        Set all current IP bans on the server. This will replace any bans already present, so if you want to add a ban, be sure to call :meth:`MumbleServer.ServerPrx.getBansAsync` and then
        append to the returned list before calling this method.
        
        Parameters
        ----------
        bans : Sequence[Ban]
            List of bans.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setBans.invoke(self, ((bans, ), context))

    def setBansAsync(self, bans: Sequence[Ban], context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set all current IP bans on the server. This will replace any bans already present, so if you want to add a ban, be sure to call :meth:`MumbleServer.ServerPrx.getBansAsync` and then
        append to the returned list before calling this method.
        
        Parameters
        ----------
        bans : Sequence[Ban]
            List of bans.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setBans.invokeAsync(self, ((bans, ), context))

    def kickUser(self, session: int, reason: str, context: dict[str, str] | None = None) -> None:
        """
        Kick a user. The user is not banned, and is free to rejoin the server.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        reason : str
            Text message to show when user is kicked.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_kickUser.invoke(self, ((session, reason), context))

    def kickUserAsync(self, session: int, reason: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Kick a user. The user is not banned, and is free to rejoin the server.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        reason : str
            Text message to show when user is kicked.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_kickUser.invokeAsync(self, ((session, reason), context))

    def getState(self, session: int, context: dict[str, str] | None = None) -> User:
        """
        Get state of a single connected user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        User
            State of connected user.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setStateAsync`
            :meth:`MumbleServer.ServerPrx.getUsersAsync`
        """
        return Server._op_getState.invoke(self, ((session, ), context))

    def getStateAsync(self, session: int, context: dict[str, str] | None = None) -> Awaitable[User]:
        """
        Get state of a single connected user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[User]
            State of connected user.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setStateAsync`
            :meth:`MumbleServer.ServerPrx.getUsersAsync`
        """
        return Server._op_getState.invokeAsync(self, ((session, ), context))

    def setState(self, state: User, context: dict[str, str] | None = None) -> None:
        """
        Set user state. You can use this to move, mute and deafen users.
        
        Parameters
        ----------
        state : User
            User state to set.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        return Server._op_setState.invoke(self, ((state, ), context))

    def setStateAsync(self, state: User, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set user state. You can use this to move, mute and deafen users.
        
        Parameters
        ----------
        state : User
            User state to set.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        return Server._op_setState.invokeAsync(self, ((state, ), context))

    def sendMessage(self, session: int, text: str, context: dict[str, str] | None = None) -> None:
        """
        Send text message to a single user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        text : str
            Message to send.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageChannelAsync`
        """
        return Server._op_sendMessage.invoke(self, ((session, text), context))

    def sendMessageAsync(self, session: int, text: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Send text message to a single user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        text : str
            Message to send.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageChannelAsync`
        """
        return Server._op_sendMessage.invokeAsync(self, ((session, text), context))

    def hasPermission(self, session: int, channelid: int, perm: int, context: dict[str, str] | None = None) -> bool:
        """
        Check if user is permitted to perform action.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        perm : int
            Permission bits to check.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        bool
            true if any of the permissions in perm were set for the user.
        """
        return Server._op_hasPermission.invoke(self, ((session, channelid, perm), context))

    def hasPermissionAsync(self, session: int, channelid: int, perm: int, context: dict[str, str] | None = None) -> Awaitable[bool]:
        """
        Check if user is permitted to perform action.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        perm : int
            Permission bits to check.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[bool]
            true if any of the permissions in perm were set for the user.
        """
        return Server._op_hasPermission.invokeAsync(self, ((session, channelid, perm), context))

    def effectivePermissions(self, session: int, channelid: int, context: dict[str, str] | None = None) -> int:
        """
        Return users effective permissions
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            bitfield of allowed actions
        """
        return Server._op_effectivePermissions.invoke(self, ((session, channelid), context))

    def effectivePermissionsAsync(self, session: int, channelid: int, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Return users effective permissions
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            bitfield of allowed actions
        """
        return Server._op_effectivePermissions.invokeAsync(self, ((session, channelid), context))

    def addContextCallback(self, session: int, action: str, text: str, cb: ServerContextCallbackPrx | None, ctx: int, context: dict[str, str] | None = None) -> None:
        """
        Add a context callback. This is done per user, and will add a context menu action for the user.
        
        Parameters
        ----------
        session : int
            Session of user which should receive context entry.
        action : str
            Action string, a unique name to associate with the action.
        text : str
            Name of action shown to user.
        cb : ServerContextCallbackPrx | None
            Callback interface which will receive notifications.
        ctx : int
            Context this should be used in. Needs to be one or a combination of :class:`MumbleServer.ContextServer`, :class:`MumbleServer.ContextChannel` and :class:`MumbleServer.ContextUser`.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeContextCallbackAsync`
        """
        return Server._op_addContextCallback.invoke(self, ((session, action, text, cb, ctx), context))

    def addContextCallbackAsync(self, session: int, action: str, text: str, cb: ServerContextCallbackPrx | None, ctx: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Add a context callback. This is done per user, and will add a context menu action for the user.
        
        Parameters
        ----------
        session : int
            Session of user which should receive context entry.
        action : str
            Action string, a unique name to associate with the action.
        text : str
            Name of action shown to user.
        cb : ServerContextCallbackPrx | None
            Callback interface which will receive notifications.
        ctx : int
            Context this should be used in. Needs to be one or a combination of :class:`MumbleServer.ContextServer`, :class:`MumbleServer.ContextChannel` and :class:`MumbleServer.ContextUser`.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeContextCallbackAsync`
        """
        return Server._op_addContextCallback.invokeAsync(self, ((session, action, text, cb, ctx), context))

    def removeContextCallback(self, cb: ServerContextCallbackPrx | None, context: dict[str, str] | None = None) -> None:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerContextCallbackPrx | None
            Callback interface to be removed. This callback will be removed from all from all users.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addContextCallbackAsync`
        """
        return Server._op_removeContextCallback.invoke(self, ((cb, ), context))

    def removeContextCallbackAsync(self, cb: ServerContextCallbackPrx | None, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerContextCallbackPrx | None
            Callback interface to be removed. This callback will be removed from all from all users.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addContextCallbackAsync`
        """
        return Server._op_removeContextCallback.invokeAsync(self, ((cb, ), context))

    def getChannelState(self, channelid: int, context: dict[str, str] | None = None) -> Channel:
        """
        Get state of single channel.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Channel
            State of channel.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setChannelStateAsync`
            :meth:`MumbleServer.ServerPrx.getChannelsAsync`
        """
        return Server._op_getChannelState.invoke(self, ((channelid, ), context))

    def getChannelStateAsync(self, channelid: int, context: dict[str, str] | None = None) -> Awaitable[Channel]:
        """
        Get state of single channel.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[Channel]
            State of channel.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setChannelStateAsync`
            :meth:`MumbleServer.ServerPrx.getChannelsAsync`
        """
        return Server._op_getChannelState.invokeAsync(self, ((channelid, ), context))

    def setChannelState(self, state: Channel, context: dict[str, str] | None = None) -> None:
        """
        Set state of a single channel. You can use this to move or relink channels.
        
        Parameters
        ----------
        state : Channel
            Channel state to set.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        return Server._op_setChannelState.invoke(self, ((state, ), context))

    def setChannelStateAsync(self, state: Channel, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set state of a single channel. You can use this to move or relink channels.
        
        Parameters
        ----------
        state : Channel
            Channel state to set.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        return Server._op_setChannelState.invokeAsync(self, ((state, ), context))

    def removeChannel(self, channelid: int, context: dict[str, str] | None = None) -> None:
        """
        Remove a channel and all its subchannels.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_removeChannel.invoke(self, ((channelid, ), context))

    def removeChannelAsync(self, channelid: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a channel and all its subchannels.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_removeChannel.invokeAsync(self, ((channelid, ), context))

    def addChannel(self, name: str, parent: int, context: dict[str, str] | None = None) -> int:
        """
        Add a new channel.
        
        Parameters
        ----------
        name : str
            Name of new channel.
        parent : int
            Channel ID of parent channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            ID of newly created channel.
        """
        return Server._op_addChannel.invoke(self, ((name, parent), context))

    def addChannelAsync(self, name: str, parent: int, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Add a new channel.
        
        Parameters
        ----------
        name : str
            Name of new channel.
        parent : int
            Channel ID of parent channel. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            ID of newly created channel.
        """
        return Server._op_addChannel.invokeAsync(self, ((name, parent), context))

    def sendMessageChannel(self, channelid: int, tree: bool, text: str, context: dict[str, str] | None = None) -> None:
        """
        Send text message to channel or a tree of channels.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to send to. See ``Channel.id``.
        tree : bool
            If true, the message will be sent to the channel and all its subchannels.
        text : str
            Message to send.
        context : dict[str, str]
            The request context for the invocation.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageAsync`
        """
        return Server._op_sendMessageChannel.invoke(self, ((channelid, tree, text), context))

    def sendMessageChannelAsync(self, channelid: int, tree: bool, text: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Send text message to channel or a tree of channels.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to send to. See ``Channel.id``.
        tree : bool
            If true, the message will be sent to the channel and all its subchannels.
        text : str
            Message to send.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageAsync`
        """
        return Server._op_sendMessageChannel.invokeAsync(self, ((channelid, tree, text), context))

    def getACL(self, channelid: int, context: dict[str, str] | None = None) -> tuple[list[ACL], list[Group], bool]:
        """
        Retrieve ACLs and Groups on a channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        tuple[list[ACL], list[Group], bool]
        
            A tuple containing:
                - list[ACL] List of ACLs on the channel. This will include inherited ACLs.
                - list[Group] List of groups on the channel. This will include inherited groups.
                - bool Does this channel inherit ACLs from the parent channel?
        """
        return Server._op_getACL.invoke(self, ((channelid, ), context))

    def getACLAsync(self, channelid: int, context: dict[str, str] | None = None) -> Awaitable[tuple[list[ACL], list[Group], bool]]:
        """
        Retrieve ACLs and Groups on a channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[tuple[list[ACL], list[Group], bool]]
        
            A tuple containing:
                - list[ACL] List of ACLs on the channel. This will include inherited ACLs.
                - list[Group] List of groups on the channel. This will include inherited groups.
                - bool Does this channel inherit ACLs from the parent channel?
        """
        return Server._op_getACL.invokeAsync(self, ((channelid, ), context))

    def setACL(self, channelid: int, acls: Sequence[ACL], groups: Sequence[Group], inherit: bool, context: dict[str, str] | None = None) -> None:
        """
        Set ACLs and Groups on a channel. Note that this will replace all existing ACLs and groups on the channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        acls : Sequence[ACL]
            List of ACLs on the channel.
        groups : Sequence[Group]
            List of groups on the channel.
        inherit : bool
            Should this channel inherit ACLs from the parent channel?
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setACL.invoke(self, ((channelid, acls, groups, inherit), context))

    def setACLAsync(self, channelid: int, acls: Sequence[ACL], groups: Sequence[Group], inherit: bool, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set ACLs and Groups on a channel. Note that this will replace all existing ACLs and groups on the channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        acls : Sequence[ACL]
            List of ACLs on the channel.
        groups : Sequence[Group]
            List of groups on the channel.
        inherit : bool
            Should this channel inherit ACLs from the parent channel?
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setACL.invokeAsync(self, ((channelid, acls, groups, inherit), context))

    def addUserToGroup(self, channelid: int, session: int, group: str, context: dict[str, str] | None = None) -> None:
        """
        Temporarily add a user to a group on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to add to.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_addUserToGroup.invoke(self, ((channelid, session, group), context))

    def addUserToGroupAsync(self, channelid: int, session: int, group: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Temporarily add a user to a group on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to add to.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_addUserToGroup.invokeAsync(self, ((channelid, session, group), context))

    def removeUserFromGroup(self, channelid: int, session: int, group: str, context: dict[str, str] | None = None) -> None:
        """
        Remove a user from a temporary group membership on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to remove from.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_removeUserFromGroup.invoke(self, ((channelid, session, group), context))

    def removeUserFromGroupAsync(self, channelid: int, session: int, group: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a user from a temporary group membership on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to remove from.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_removeUserFromGroup.invokeAsync(self, ((channelid, session, group), context))

    def redirectWhisperGroup(self, session: int, source: str, target: str, context: dict[str, str] | None = None) -> None:
        """
        Redirect whisper targets for user. If set, whenever a user tries to whisper to group "source", the whisper will be redirected to group "target".
        To remove a redirect pass an empty target string. This is intended for context groups.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        source : str
            Group name to redirect from.
        target : str
            Group name to redirect to.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_redirectWhisperGroup.invoke(self, ((session, source, target), context))

    def redirectWhisperGroupAsync(self, session: int, source: str, target: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Redirect whisper targets for user. If set, whenever a user tries to whisper to group "source", the whisper will be redirected to group "target".
        To remove a redirect pass an empty target string. This is intended for context groups.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        source : str
            Group name to redirect from.
        target : str
            Group name to redirect to.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_redirectWhisperGroup.invokeAsync(self, ((session, source, target), context))

    def getUserNames(self, ids: Sequence[int] | Buffer, context: dict[str, str] | None = None) -> dict[int, str]:
        """
        Map a list of ``User.userid`` to a matching name.
        
        Parameters
        ----------
        ids : Sequence[int] | Buffer
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[int, str]
            Matching list of names, with an empty string representing invalid or unknown ids.
        """
        return Server._op_getUserNames.invoke(self, ((ids, ), context))

    def getUserNamesAsync(self, ids: Sequence[int] | Buffer, context: dict[str, str] | None = None) -> Awaitable[dict[int, str]]:
        """
        Map a list of ``User.userid`` to a matching name.
        
        Parameters
        ----------
        ids : Sequence[int] | Buffer
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[int, str]]
            Matching list of names, with an empty string representing invalid or unknown ids.
        """
        return Server._op_getUserNames.invokeAsync(self, ((ids, ), context))

    def getUserIds(self, names: Sequence[str], context: dict[str, str] | None = None) -> dict[str, int]:
        """
        Map a list of user names to a matching id.
        
        Parameters
        ----------
        names : Sequence[str]
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[str, int]
        """
        return Server._op_getUserIds.invoke(self, ((names, ), context))

    def getUserIdsAsync(self, names: Sequence[str], context: dict[str, str] | None = None) -> Awaitable[dict[str, int]]:
        """
        Map a list of user names to a matching id.
        
        Parameters
        ----------
        names : Sequence[str]
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[str, int]]
        """
        return Server._op_getUserIds.invokeAsync(self, ((names, ), context))

    def registerUser(self, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> int:
        """
        Register a new user.
        
        Parameters
        ----------
        info : Mapping[UserInfo, str]
            Information about new user. Must include at least "name".
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            The ID of the user. See ``RegisteredUser.userid``.
        """
        return Server._op_registerUser.invoke(self, ((info, ), context))

    def registerUserAsync(self, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Register a new user.
        
        Parameters
        ----------
        info : Mapping[UserInfo, str]
            Information about new user. Must include at least "name".
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            The ID of the user. See ``RegisteredUser.userid``.
        """
        return Server._op_registerUser.invokeAsync(self, ((info, ), context))

    def unregisterUser(self, userid: int, context: dict[str, str] | None = None) -> None:
        """
        Remove a user registration.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_unregisterUser.invoke(self, ((userid, ), context))

    def unregisterUserAsync(self, userid: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Remove a user registration.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_unregisterUser.invokeAsync(self, ((userid, ), context))

    def updateRegistration(self, userid: int, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> None:
        """
        Update the registration for a user. You can use this to set the email or password of a user,
        and can also use it to change the user's name.
        
        Parameters
        ----------
        userid : int
        info : Mapping[UserInfo, str]
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_updateRegistration.invoke(self, ((userid, info), context))

    def updateRegistrationAsync(self, userid: int, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Update the registration for a user. You can use this to set the email or password of a user,
        and can also use it to change the user's name.
        
        Parameters
        ----------
        userid : int
        info : Mapping[UserInfo, str]
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_updateRegistration.invokeAsync(self, ((userid, info), context))

    def getRegistration(self, userid: int, context: dict[str, str] | None = None) -> dict[UserInfo, str]:
        """
        Fetch registration for a single user.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[UserInfo, str]
            Registration record.
        """
        return Server._op_getRegistration.invoke(self, ((userid, ), context))

    def getRegistrationAsync(self, userid: int, context: dict[str, str] | None = None) -> Awaitable[dict[UserInfo, str]]:
        """
        Fetch registration for a single user.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[UserInfo, str]]
            Registration record.
        """
        return Server._op_getRegistration.invokeAsync(self, ((userid, ), context))

    def getRegisteredUsers(self, filter: str, context: dict[str, str] | None = None) -> dict[int, str]:
        """
        Fetch a group of registered users.
        
        Parameters
        ----------
        filter : str
            Substring of user name. If blank, will retrieve all registered users.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[int, str]
            List of registration records.
        """
        return Server._op_getRegisteredUsers.invoke(self, ((filter, ), context))

    def getRegisteredUsersAsync(self, filter: str, context: dict[str, str] | None = None) -> Awaitable[dict[int, str]]:
        """
        Fetch a group of registered users.
        
        Parameters
        ----------
        filter : str
            Substring of user name. If blank, will retrieve all registered users.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[int, str]]
            List of registration records.
        """
        return Server._op_getRegisteredUsers.invokeAsync(self, ((filter, ), context))

    def verifyPassword(self, name: str, pw: str, context: dict[str, str] | None = None) -> int:
        """
        Verify the password of a user. You can use this to verify a user's credentials.
        
        Parameters
        ----------
        name : str
            User name. See ``RegisteredUser.name``.
        pw : str
            User password.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            User ID of registered user (See ``RegisteredUser.userid``), -1 for failed authentication or -2 for unknown usernames.
        """
        return Server._op_verifyPassword.invoke(self, ((name, pw), context))

    def verifyPasswordAsync(self, name: str, pw: str, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Verify the password of a user. You can use this to verify a user's credentials.
        
        Parameters
        ----------
        name : str
            User name. See ``RegisteredUser.name``.
        pw : str
            User password.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            User ID of registered user (See ``RegisteredUser.userid``), -1 for failed authentication or -2 for unknown usernames.
        """
        return Server._op_verifyPassword.invokeAsync(self, ((name, pw), context))

    def getTexture(self, userid: int, context: dict[str, str] | None = None) -> bytes:
        """
        Fetch user texture. Textures are stored as zlib compress()ed 600x60 32-bit BGRA data.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        bytes
            Custom texture associated with user or an empty texture.
        """
        return Server._op_getTexture.invoke(self, ((userid, ), context))

    def getTextureAsync(self, userid: int, context: dict[str, str] | None = None) -> Awaitable[bytes]:
        """
        Fetch user texture. Textures are stored as zlib compress()ed 600x60 32-bit BGRA data.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[bytes]
            Custom texture associated with user or an empty texture.
        """
        return Server._op_getTexture.invokeAsync(self, ((userid, ), context))

    def setTexture(self, userid: int, tex: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> None:
        """
        Set a user texture (now called avatar).
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        tex : Sequence[int] | bytes | Buffer
            Texture (as a Byte-Array) to set for the user, or an empty texture to remove the existing texture.
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setTexture.invoke(self, ((userid, tex), context))

    def setTextureAsync(self, userid: int, tex: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Set a user texture (now called avatar).
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        tex : Sequence[int] | bytes | Buffer
            Texture (as a Byte-Array) to set for the user, or an empty texture to remove the existing texture.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setTexture.invokeAsync(self, ((userid, tex), context))

    def getUptime(self, context: dict[str, str] | None = None) -> int:
        """
        Get virtual server uptime.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            Uptime of the virtual server in seconds
        """
        return Server._op_getUptime.invoke(self, ((), context))

    def getUptimeAsync(self, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Get virtual server uptime.
        
        Parameters
        ----------
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            Uptime of the virtual server in seconds
        """
        return Server._op_getUptime.invokeAsync(self, ((), context))

    def updateCertificate(self, certificate: str, privateKey: str, passphrase: str, context: dict[str, str] | None = None) -> None:
        """
        Update the server's certificate information.
        
        Reconfigure the running server's TLS socket with the given
        certificate and private key.
        
        The certificate and and private key must be PEM formatted.
        
        New clients will see the new certificate.
        Existing clients will continue to see the certificate the server
        was using when they connected to it.
        
        This method throws InvalidInputDataException if any of the
        following errors happen:
        - Unable to decode the PEM certificate and/or private key.
        - Unable to decrypt the private key with the given passphrase.
        - The certificate and/or private key do not contain RSA keys.
        - The certificate is not usable with the given private key.
        
        Parameters
        ----------
        certificate : str
        privateKey : str
        passphrase : str
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_updateCertificate.invoke(self, ((certificate, privateKey, passphrase), context))

    def updateCertificateAsync(self, certificate: str, privateKey: str, passphrase: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Update the server's certificate information.
        
        Reconfigure the running server's TLS socket with the given
        certificate and private key.
        
        The certificate and and private key must be PEM formatted.
        
        New clients will see the new certificate.
        Existing clients will continue to see the certificate the server
        was using when they connected to it.
        
        This method throws InvalidInputDataException if any of the
        following errors happen:
        - Unable to decode the PEM certificate and/or private key.
        - Unable to decrypt the private key with the given passphrase.
        - The certificate and/or private key do not contain RSA keys.
        - The certificate is not usable with the given private key.
        
        Parameters
        ----------
        certificate : str
        privateKey : str
        passphrase : str
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_updateCertificate.invokeAsync(self, ((certificate, privateKey, passphrase), context))

    def startListening(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> None:
        """
        Makes the given user start listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_startListening.invoke(self, ((userid, channelid), context))

    def startListeningAsync(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Makes the given user start listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_startListening.invokeAsync(self, ((userid, channelid), context))

    def stopListening(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> None:
        """
        Makes the given user stop listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_stopListening.invoke(self, ((userid, channelid), context))

    def stopListeningAsync(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Makes the given user stop listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_stopListening.invokeAsync(self, ((userid, channelid), context))

    def isListening(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> bool:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        bool
        """
        return Server._op_isListening.invoke(self, ((userid, channelid), context))

    def isListeningAsync(self, userid: int, channelid: int, context: dict[str, str] | None = None) -> Awaitable[bool]:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[bool]
        """
        return Server._op_isListening.invokeAsync(self, ((userid, channelid), context))

    def getListeningChannels(self, userid: int, context: dict[str, str] | None = None) -> list[int]:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[int]
        """
        return Server._op_getListeningChannels.invoke(self, ((userid, ), context))

    def getListeningChannelsAsync(self, userid: int, context: dict[str, str] | None = None) -> Awaitable[list[int]]:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[int]]
        """
        return Server._op_getListeningChannels.invokeAsync(self, ((userid, ), context))

    def getListeningUsers(self, channelid: int, context: dict[str, str] | None = None) -> list[int]:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        list[int]
        """
        return Server._op_getListeningUsers.invoke(self, ((channelid, ), context))

    def getListeningUsersAsync(self, channelid: int, context: dict[str, str] | None = None) -> Awaitable[list[int]]:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[list[int]]
        """
        return Server._op_getListeningUsers.invokeAsync(self, ((channelid, ), context))

    def getListenerVolumeAdjustment(self, channelid: int, userid: int, context: dict[str, str] | None = None) -> float:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        float
        """
        return Server._op_getListenerVolumeAdjustment.invoke(self, ((channelid, userid), context))

    def getListenerVolumeAdjustmentAsync(self, channelid: int, userid: int, context: dict[str, str] | None = None) -> Awaitable[float]:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[float]
        """
        return Server._op_getListenerVolumeAdjustment.invokeAsync(self, ((channelid, userid), context))

    def setListenerVolumeAdjustment(self, channelid: int, userid: int, volumeAdjustment: float, context: dict[str, str] | None = None) -> None:
        """
        Sets the volume adjustment set for a listener of the given user in the given channel
        
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        volumeAdjustment : float
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_setListenerVolumeAdjustment.invoke(self, ((channelid, userid, volumeAdjustment), context))

    def setListenerVolumeAdjustmentAsync(self, channelid: int, userid: int, volumeAdjustment: float, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Sets the volume adjustment set for a listener of the given user in the given channel
        
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        volumeAdjustment : float
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_setListenerVolumeAdjustment.invokeAsync(self, ((channelid, userid, volumeAdjustment), context))

    def sendWelcomeMessage(self, receiverUserIDs: Sequence[int] | Buffer, context: dict[str, str] | None = None) -> None:
        """
        Parameters
        ----------
        receiverUserIDs : Sequence[int] | Buffer
            list of IDs of the users the message shall be sent to
        context : dict[str, str]
            The request context for the invocation.
        """
        return Server._op_sendWelcomeMessage.invoke(self, ((receiverUserIDs, ), context))

    def sendWelcomeMessageAsync(self, receiverUserIDs: Sequence[int] | Buffer, context: dict[str, str] | None = None) -> Awaitable[None]:
        """
        Parameters
        ----------
        receiverUserIDs : Sequence[int] | Buffer
            list of IDs of the users the message shall be sent to
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[None]
            An awaitable that is completed when the invocation completes.
        """
        return Server._op_sendWelcomeMessage.invokeAsync(self, ((receiverUserIDs, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ServerPrx | None:
        return checkedCast(ServerPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ServerPrx | None ]:
        return checkedCastAsync(ServerPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ServerPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ServerPrx | None:
        return uncheckedCast(ServerPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::Server"

IcePy.defineProxy("::MumbleServer::Server", ServerPrx)

class Server(Object, ABC):
    """
    Per-server interface. This includes all methods for configuring and altering
    the state of a single virtual server. You can retrieve a pointer to this interface
    from one of the methods in :class:`MumbleServer.MetaPrx`.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::Server``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::Server", )
    _op_isRunning: IcePy.Operation
    _op_start: IcePy.Operation
    _op_stop: IcePy.Operation
    _op_delete: IcePy.Operation
    _op_id: IcePy.Operation
    _op_addCallback: IcePy.Operation
    _op_removeCallback: IcePy.Operation
    _op_setAuthenticator: IcePy.Operation
    _op_getConf: IcePy.Operation
    _op_getAllConf: IcePy.Operation
    _op_setConf: IcePy.Operation
    _op_setSuperuserPassword: IcePy.Operation
    _op_getLog: IcePy.Operation
    _op_getLogLen: IcePy.Operation
    _op_getUsers: IcePy.Operation
    _op_getChannels: IcePy.Operation
    _op_getCertificateList: IcePy.Operation
    _op_getTree: IcePy.Operation
    _op_getBans: IcePy.Operation
    _op_setBans: IcePy.Operation
    _op_kickUser: IcePy.Operation
    _op_getState: IcePy.Operation
    _op_setState: IcePy.Operation
    _op_sendMessage: IcePy.Operation
    _op_hasPermission: IcePy.Operation
    _op_effectivePermissions: IcePy.Operation
    _op_addContextCallback: IcePy.Operation
    _op_removeContextCallback: IcePy.Operation
    _op_getChannelState: IcePy.Operation
    _op_setChannelState: IcePy.Operation
    _op_removeChannel: IcePy.Operation
    _op_addChannel: IcePy.Operation
    _op_sendMessageChannel: IcePy.Operation
    _op_getACL: IcePy.Operation
    _op_setACL: IcePy.Operation
    _op_addUserToGroup: IcePy.Operation
    _op_removeUserFromGroup: IcePy.Operation
    _op_redirectWhisperGroup: IcePy.Operation
    _op_getUserNames: IcePy.Operation
    _op_getUserIds: IcePy.Operation
    _op_registerUser: IcePy.Operation
    _op_unregisterUser: IcePy.Operation
    _op_updateRegistration: IcePy.Operation
    _op_getRegistration: IcePy.Operation
    _op_getRegisteredUsers: IcePy.Operation
    _op_verifyPassword: IcePy.Operation
    _op_getTexture: IcePy.Operation
    _op_setTexture: IcePy.Operation
    _op_getUptime: IcePy.Operation
    _op_updateCertificate: IcePy.Operation
    _op_startListening: IcePy.Operation
    _op_stopListening: IcePy.Operation
    _op_isListening: IcePy.Operation
    _op_getListeningChannels: IcePy.Operation
    _op_getListeningUsers: IcePy.Operation
    _op_getListenerVolumeAdjustment: IcePy.Operation
    _op_setListenerVolumeAdjustment: IcePy.Operation
    _op_sendWelcomeMessage: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::Server"

    @abstractmethod
    def isRunning(self, current: Current) -> bool | Awaitable[bool]:
        """
        Shows if the server currently running (accepting users).
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        bool | Awaitable[bool]
            Run-state of server.
        """
        pass

    @abstractmethod
    def start(self, current: Current) -> None | Awaitable[None]:
        """
        Start server.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def stop(self, current: Current) -> None | Awaitable[None]:
        """
        Stop server.
        Note: Server will be restarted on application restart unless explicitly disabled
        with setConf("boot", false)
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def delete(self, current: Current) -> None | Awaitable[None]:
        """
        Delete server and all it's configuration.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def id(self, current: Current) -> int | Awaitable[int]:
        """
        Fetch the server id.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            Unique server id.
        """
        pass

    @abstractmethod
    def addCallback(self, cb: ServerCallbackPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Add a callback. The callback will receive notifications about changes to users and channels.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface which will receive notifications.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeCallbackAsync`
        """
        pass

    @abstractmethod
    def removeCallback(self, cb: ServerCallbackPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerCallbackPrx | None
            Callback interface to be removed.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addCallbackAsync`
        """
        pass

    @abstractmethod
    def setAuthenticator(self, auth: ServerAuthenticatorPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Set external authenticator. If set, all authentications from clients are forwarded to this
        proxy.
        
        Parameters
        ----------
        auth : ServerAuthenticatorPrx | None
            Authenticator object to perform subsequent authentications.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getConf(self, key: str, current: Current) -> str | Awaitable[str]:
        """
        Retrieve configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        str | Awaitable[str]
            Configuration value. If this is empty, see ``Meta.getDefaultConf``
        """
        pass

    @abstractmethod
    def getAllConf(self, current: Current) -> Mapping[str, str] | Awaitable[Mapping[str, str]]:
        """
        Retrieve all configuration items.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[str, str] | Awaitable[Mapping[str, str]]
            All configured values. If a value isn't set here, the value from ``Meta.getDefaultConf`` is used.
        """
        pass

    @abstractmethod
    def setConf(self, key: str, value: str, current: Current) -> None | Awaitable[None]:
        """
        Set a configuration item.
        
        Parameters
        ----------
        key : str
            Configuration key.
        value : str
            Configuration value.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def setSuperuserPassword(self, pw: str, current: Current) -> None | Awaitable[None]:
        """
        Set superuser password. This is just a convenience for using :meth:`MumbleServer.ServerPrx.updateRegistrationAsync` on user id 0.
        
        Parameters
        ----------
        pw : str
            Password.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getLog(self, first: int, last: int, current: Current) -> Sequence[LogEntry] | Awaitable[Sequence[LogEntry]]:
        """
        Fetch log entries.
        
        Parameters
        ----------
        first : int
            Lowest numbered entry to fetch. 0 is the most recent item.
        last : int
            Last entry to fetch.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[LogEntry] | Awaitable[Sequence[LogEntry]]
            List of log entries.
        """
        pass

    @abstractmethod
    def getLogLen(self, current: Current) -> int | Awaitable[int]:
        """
        Fetch length of log
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            Number of entries in log
        """
        pass

    @abstractmethod
    def getUsers(self, current: Current) -> Mapping[int, User] | Awaitable[Mapping[int, User]]:
        """
        Fetch all users. This returns all currently connected users on the server.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[int, User] | Awaitable[Mapping[int, User]]
            List of connected users.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        pass

    @abstractmethod
    def getChannels(self, current: Current) -> Mapping[int, Channel] | Awaitable[Mapping[int, Channel]]:
        """
        Fetch all channels. This returns all defined channels on the server. The root channel is always channel 0.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[int, Channel] | Awaitable[Mapping[int, Channel]]
            List of defined channels.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        pass

    @abstractmethod
    def getCertificateList(self, session: int, current: Current) -> Sequence[Sequence[int] | bytes | Buffer] | Awaitable[Sequence[Sequence[int] | bytes | Buffer]]:
        """
        Fetch certificate of user. This returns the complete certificate chain of a user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[Sequence[int] | bytes | Buffer] | Awaitable[Sequence[Sequence[int] | bytes | Buffer]]
            Certificate list of user.
        """
        pass

    @abstractmethod
    def getTree(self, current: Current) -> Tree | None | Awaitable[Tree | None]:
        """
        Fetch all channels and connected users as a tree. This retrieves an easy-to-use representation of the server
        as a tree. This is primarily used for viewing the state of the server on a webpage.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Tree | None | Awaitable[Tree | None]
            Recursive tree of all channels and connected users.
        """
        pass

    @abstractmethod
    def getBans(self, current: Current) -> Sequence[Ban] | Awaitable[Sequence[Ban]]:
        """
        Fetch all current IP bans on the server.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[Ban] | Awaitable[Sequence[Ban]]
            List of bans.
        """
        pass

    @abstractmethod
    def setBans(self, bans: list[Ban], current: Current) -> None | Awaitable[None]:
        """
        Set all current IP bans on the server. This will replace any bans already present, so if you want to add a ban, be sure to call :meth:`MumbleServer.ServerPrx.getBansAsync` and then
        append to the returned list before calling this method.
        
        Parameters
        ----------
        bans : list[Ban]
            List of bans.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def kickUser(self, session: int, reason: str, current: Current) -> None | Awaitable[None]:
        """
        Kick a user. The user is not banned, and is free to rejoin the server.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        reason : str
            Text message to show when user is kicked.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getState(self, session: int, current: Current) -> User | Awaitable[User]:
        """
        Get state of a single connected user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        User | Awaitable[User]
            State of connected user.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setStateAsync`
            :meth:`MumbleServer.ServerPrx.getUsersAsync`
        """
        pass

    @abstractmethod
    def setState(self, state: User, current: Current) -> None | Awaitable[None]:
        """
        Set user state. You can use this to move, mute and deafen users.
        
        Parameters
        ----------
        state : User
            User state to set.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getStateAsync`
        """
        pass

    @abstractmethod
    def sendMessage(self, session: int, text: str, current: Current) -> None | Awaitable[None]:
        """
        Send text message to a single user.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        text : str
            Message to send.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageChannelAsync`
        """
        pass

    @abstractmethod
    def hasPermission(self, session: int, channelid: int, perm: int, current: Current) -> bool | Awaitable[bool]:
        """
        Check if user is permitted to perform action.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        perm : int
            Permission bits to check.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        bool | Awaitable[bool]
            true if any of the permissions in perm were set for the user.
        """
        pass

    @abstractmethod
    def effectivePermissions(self, session: int, channelid: int, current: Current) -> int | Awaitable[int]:
        """
        Return users effective permissions
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        channelid : int
            ID of Channel. See ``Channel.id``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            bitfield of allowed actions
        """
        pass

    @abstractmethod
    def addContextCallback(self, session: int, action: str, text: str, cb: ServerContextCallbackPrx | None, ctx: int, current: Current) -> None | Awaitable[None]:
        """
        Add a context callback. This is done per user, and will add a context menu action for the user.
        
        Parameters
        ----------
        session : int
            Session of user which should receive context entry.
        action : str
            Action string, a unique name to associate with the action.
        text : str
            Name of action shown to user.
        cb : ServerContextCallbackPrx | None
            Callback interface which will receive notifications.
        ctx : int
            Context this should be used in. Needs to be one or a combination of :class:`MumbleServer.ContextServer`, :class:`MumbleServer.ContextChannel` and :class:`MumbleServer.ContextUser`.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.removeContextCallbackAsync`
        """
        pass

    @abstractmethod
    def removeContextCallback(self, cb: ServerContextCallbackPrx | None, current: Current) -> None | Awaitable[None]:
        """
        Remove a callback.
        
        Parameters
        ----------
        cb : ServerContextCallbackPrx | None
            Callback interface to be removed. This callback will be removed from all from all users.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.addContextCallbackAsync`
        """
        pass

    @abstractmethod
    def getChannelState(self, channelid: int, current: Current) -> Channel | Awaitable[Channel]:
        """
        Get state of single channel.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Channel | Awaitable[Channel]
            State of channel.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.setChannelStateAsync`
            :meth:`MumbleServer.ServerPrx.getChannelsAsync`
        """
        pass

    @abstractmethod
    def setChannelState(self, state: Channel, current: Current) -> None | Awaitable[None]:
        """
        Set state of a single channel. You can use this to move or relink channels.
        
        Parameters
        ----------
        state : Channel
            Channel state to set.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.getChannelStateAsync`
        """
        pass

    @abstractmethod
    def removeChannel(self, channelid: int, current: Current) -> None | Awaitable[None]:
        """
        Remove a channel and all its subchannels.
        
        Parameters
        ----------
        channelid : int
            ID of Channel. See ``Channel.id``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def addChannel(self, name: str, parent: int, current: Current) -> int | Awaitable[int]:
        """
        Add a new channel.
        
        Parameters
        ----------
        name : str
            Name of new channel.
        parent : int
            Channel ID of parent channel. See ``Channel.id``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            ID of newly created channel.
        """
        pass

    @abstractmethod
    def sendMessageChannel(self, channelid: int, tree: bool, text: str, current: Current) -> None | Awaitable[None]:
        """
        Send text message to channel or a tree of channels.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to send to. See ``Channel.id``.
        tree : bool
            If true, the message will be sent to the channel and all its subchannels.
        text : str
            Message to send.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        
        See Also
        --------
            :meth:`MumbleServer.ServerPrx.sendMessageAsync`
        """
        pass

    @abstractmethod
    def getACL(self, channelid: int, current: Current) -> tuple[Sequence[ACL], Sequence[Group], bool] | Awaitable[tuple[Sequence[ACL], Sequence[Group], bool]]:
        """
        Retrieve ACLs and Groups on a channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        tuple[Sequence[ACL], Sequence[Group], bool] | Awaitable[tuple[Sequence[ACL], Sequence[Group], bool]]
        
            A tuple containing:
                - Sequence[ACL] List of ACLs on the channel. This will include inherited ACLs.
                - Sequence[Group] List of groups on the channel. This will include inherited groups.
                - bool Does this channel inherit ACLs from the parent channel?
        """
        pass

    @abstractmethod
    def setACL(self, channelid: int, acls: list[ACL], groups: list[Group], inherit: bool, current: Current) -> None | Awaitable[None]:
        """
        Set ACLs and Groups on a channel. Note that this will replace all existing ACLs and groups on the channel.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to fetch from. See ``Channel.id``.
        acls : list[ACL]
            List of ACLs on the channel.
        groups : list[Group]
            List of groups on the channel.
        inherit : bool
            Should this channel inherit ACLs from the parent channel?
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def addUserToGroup(self, channelid: int, session: int, group: str, current: Current) -> None | Awaitable[None]:
        """
        Temporarily add a user to a group on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to add to.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def removeUserFromGroup(self, channelid: int, session: int, group: str, current: Current) -> None | Awaitable[None]:
        """
        Remove a user from a temporary group membership on a channel. This state is not saved, and is intended for temporary memberships.
        
        Parameters
        ----------
        channelid : int
            Channel ID of channel to add to. See ``Channel.id``.
        session : int
            Connection ID of user. See ``User.session``.
        group : str
            Group name to remove from.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def redirectWhisperGroup(self, session: int, source: str, target: str, current: Current) -> None | Awaitable[None]:
        """
        Redirect whisper targets for user. If set, whenever a user tries to whisper to group "source", the whisper will be redirected to group "target".
        To remove a redirect pass an empty target string. This is intended for context groups.
        
        Parameters
        ----------
        session : int
            Connection ID of user. See ``User.session``.
        source : str
            Group name to redirect from.
        target : str
            Group name to redirect to.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getUserNames(self, ids: list[int], current: Current) -> Mapping[int, str] | Awaitable[Mapping[int, str]]:
        """
        Map a list of ``User.userid`` to a matching name.
        
        Parameters
        ----------
        ids : list[int]
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[int, str] | Awaitable[Mapping[int, str]]
            Matching list of names, with an empty string representing invalid or unknown ids.
        """
        pass

    @abstractmethod
    def getUserIds(self, names: list[str], current: Current) -> Mapping[str, int] | Awaitable[Mapping[str, int]]:
        """
        Map a list of user names to a matching id.
        
        Parameters
        ----------
        names : list[str]
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[str, int] | Awaitable[Mapping[str, int]]
        """
        pass

    @abstractmethod
    def registerUser(self, info: dict[UserInfo, str], current: Current) -> int | Awaitable[int]:
        """
        Register a new user.
        
        Parameters
        ----------
        info : dict[UserInfo, str]
            Information about new user. Must include at least "name".
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            The ID of the user. See ``RegisteredUser.userid``.
        """
        pass

    @abstractmethod
    def unregisterUser(self, userid: int, current: Current) -> None | Awaitable[None]:
        """
        Remove a user registration.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def updateRegistration(self, userid: int, info: dict[UserInfo, str], current: Current) -> None | Awaitable[None]:
        """
        Update the registration for a user. You can use this to set the email or password of a user,
        and can also use it to change the user's name.
        
        Parameters
        ----------
        userid : int
        info : dict[UserInfo, str]
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def getRegistration(self, userid: int, current: Current) -> Mapping[UserInfo, str] | Awaitable[Mapping[UserInfo, str]]:
        """
        Fetch registration for a single user.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[UserInfo, str] | Awaitable[Mapping[UserInfo, str]]
            Registration record.
        """
        pass

    @abstractmethod
    def getRegisteredUsers(self, filter: str, current: Current) -> Mapping[int, str] | Awaitable[Mapping[int, str]]:
        """
        Fetch a group of registered users.
        
        Parameters
        ----------
        filter : str
            Substring of user name. If blank, will retrieve all registered users.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[int, str] | Awaitable[Mapping[int, str]]
            List of registration records.
        """
        pass

    @abstractmethod
    def verifyPassword(self, name: str, pw: str, current: Current) -> int | Awaitable[int]:
        """
        Verify the password of a user. You can use this to verify a user's credentials.
        
        Parameters
        ----------
        name : str
            User name. See ``RegisteredUser.name``.
        pw : str
            User password.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            User ID of registered user (See ``RegisteredUser.userid``), -1 for failed authentication or -2 for unknown usernames.
        """
        pass

    @abstractmethod
    def getTexture(self, userid: int, current: Current) -> Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]:
        """
        Fetch user texture. Textures are stored as zlib compress()ed 600x60 32-bit BGRA data.
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]
            Custom texture associated with user or an empty texture.
        """
        pass

    @abstractmethod
    def setTexture(self, userid: int, tex: bytes, current: Current) -> None | Awaitable[None]:
        """
        Set a user texture (now called avatar).
        
        Parameters
        ----------
        userid : int
            ID of registered user. See ``RegisteredUser.userid``.
        tex : bytes
            Texture (as a Byte-Array) to set for the user, or an empty texture to remove the existing texture.
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
        Get virtual server uptime.
        
        Parameters
        ----------
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            Uptime of the virtual server in seconds
        """
        pass

    @abstractmethod
    def updateCertificate(self, certificate: str, privateKey: str, passphrase: str, current: Current) -> None | Awaitable[None]:
        """
        Update the server's certificate information.
        
        Reconfigure the running server's TLS socket with the given
        certificate and private key.
        
        The certificate and and private key must be PEM formatted.
        
        New clients will see the new certificate.
        Existing clients will continue to see the certificate the server
        was using when they connected to it.
        
        This method throws InvalidInputDataException if any of the
        following errors happen:
        - Unable to decode the PEM certificate and/or private key.
        - Unable to decrypt the private key with the given passphrase.
        - The certificate and/or private key do not contain RSA keys.
        - The certificate is not usable with the given private key.
        
        Parameters
        ----------
        certificate : str
        privateKey : str
        passphrase : str
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def startListening(self, userid: int, channelid: int, current: Current) -> None | Awaitable[None]:
        """
        Makes the given user start listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def stopListening(self, userid: int, channelid: int, current: Current) -> None | Awaitable[None]:
        """
        Makes the given user stop listening to the given channel.
        
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def isListening(self, userid: int, channelid: int, current: Current) -> bool | Awaitable[bool]:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        channelid : int
            The ID of the channel
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        bool | Awaitable[bool]
        """
        pass

    @abstractmethod
    def getListeningChannels(self, userid: int, current: Current) -> Sequence[int] | Buffer | Awaitable[Sequence[int] | Buffer]:
        """
        Parameters
        ----------
        userid : int
            The ID of the user
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[int] | Buffer | Awaitable[Sequence[int] | Buffer]
        """
        pass

    @abstractmethod
    def getListeningUsers(self, channelid: int, current: Current) -> Sequence[int] | Buffer | Awaitable[Sequence[int] | Buffer]:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[int] | Buffer | Awaitable[Sequence[int] | Buffer]
        """
        pass

    @abstractmethod
    def getListenerVolumeAdjustment(self, channelid: int, userid: int, current: Current) -> float | Awaitable[float]:
        """
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        float | Awaitable[float]
        """
        pass

    @abstractmethod
    def setListenerVolumeAdjustment(self, channelid: int, userid: int, volumeAdjustment: float, current: Current) -> None | Awaitable[None]:
        """
        Sets the volume adjustment set for a listener of the given user in the given channel
        
        Parameters
        ----------
        channelid : int
            The ID of the channel
        userid : int
            The ID of the user
        volumeAdjustment : float
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

    @abstractmethod
    def sendWelcomeMessage(self, receiverUserIDs: list[int], current: Current) -> None | Awaitable[None]:
        """
        Parameters
        ----------
        receiverUserIDs : list[int]
            list of IDs of the users the message shall be sent to
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        None | Awaitable[None]
            None or an awaitable that completes when the dispatch completes.
        """
        pass

Server._op_isRunning = IcePy.Operation(
    "isRunning",
    "isRunning",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_bool, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Server._op_start = IcePy.Operation(
    "start",
    "start",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_ServerFailureException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_stop = IcePy.Operation(
    "stop",
    "stop",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_delete = IcePy.Operation(
    "delete",
    "delete",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_id = IcePy.Operation(
    "id",
    "id",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_InvalidSecretException_t,),
    False)

Server._op_addCallback = IcePy.Operation(
    "addCallback",
    "addCallback",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerCallbackPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_removeCallback = IcePy.Operation(
    "removeCallback",
    "removeCallback",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerCallbackPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setAuthenticator = IcePy.Operation(
    "setAuthenticator",
    "setAuthenticator",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerAuthenticatorPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getConf = IcePy.Operation(
    "getConf",
    "getConf",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    ((), IcePy._t_string, False, 0),
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_WriteOnlyException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getAllConf = IcePy.Operation(
    "getAllConf",
    "getAllConf",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ConfigMap_t, False, 0),
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_setConf = IcePy.Operation(
    "setConf",
    "setConf",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_setSuperuserPassword = IcePy.Operation(
    "setSuperuserPassword",
    "setSuperuserPassword",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    None,
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getLog = IcePy.Operation(
    "getLog",
    "getLog",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), _MumbleServer_LogList_t, False, 0),
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getLogLen = IcePy.Operation(
    "getLogLen",
    "getLogLen",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getUsers = IcePy.Operation(
    "getUsers",
    "getUsers",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_UserMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getChannels = IcePy.Operation(
    "getChannels",
    "getChannels",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_ChannelMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getCertificateList = IcePy.Operation(
    "getCertificateList",
    "getCertificateList",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_CertificateList_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getTree = IcePy.Operation(
    "getTree",
    "getTree",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_Tree_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getBans = IcePy.Operation(
    "getBans",
    "getBans",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _MumbleServer_BanList_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setBans = IcePy.Operation(
    "setBans",
    "setBans",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_BanList_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_kickUser = IcePy.Operation(
    "kickUser",
    "kickUser",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getState = IcePy.Operation(
    "getState",
    "getState",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_User_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setState = IcePy.Operation(
    "setState",
    "setState",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_User_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_sendMessage = IcePy.Operation(
    "sendMessage",
    "sendMessage",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_hasPermission = IcePy.Operation(
    "hasPermission",
    "hasPermission",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_bool, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_effectivePermissions = IcePy.Operation(
    "effectivePermissions",
    "effectivePermissions",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_addContextCallback = IcePy.Operation(
    "addContextCallback",
    "addContextCallback",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), _MumbleServer_ServerContextCallbackPrx_t, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_removeContextCallback = IcePy.Operation(
    "removeContextCallback",
    "removeContextCallback",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_ServerContextCallbackPrx_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidCallbackException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getChannelState = IcePy.Operation(
    "getChannelState",
    "getChannelState",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_Channel_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setChannelState = IcePy.Operation(
    "setChannelState",
    "setChannelState",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_Channel_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_NestingLimitException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_removeChannel = IcePy.Operation(
    "removeChannel",
    "removeChannel",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_addChannel = IcePy.Operation(
    "addChannel",
    "addChannel",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_NestingLimitException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_sendMessageChannel = IcePy.Operation(
    "sendMessageChannel",
    "sendMessageChannel",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_bool, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getACL = IcePy.Operation(
    "getACL",
    "getACL",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (((), _MumbleServer_ACLList_t, False, 0), ((), _MumbleServer_GroupList_t, False, 0), ((), IcePy._t_bool, False, 0)),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setACL = IcePy.Operation(
    "setACL",
    "setACL",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), _MumbleServer_ACLList_t, False, 0), ((), _MumbleServer_GroupList_t, False, 0), ((), IcePy._t_bool, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_addUserToGroup = IcePy.Operation(
    "addUserToGroup",
    "addUserToGroup",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_removeUserFromGroup = IcePy.Operation(
    "removeUserFromGroup",
    "removeUserFromGroup",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_redirectWhisperGroup = IcePy.Operation(
    "redirectWhisperGroup",
    "redirectWhisperGroup",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSessionException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getUserNames = IcePy.Operation(
    "getUserNames",
    "getUserNames",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_IdList_t, False, 0),),
    (),
    ((), _MumbleServer_NameMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getUserIds = IcePy.Operation(
    "getUserIds",
    "getUserIds",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_NameList_t, False, 0),),
    (),
    ((), _MumbleServer_IdMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_registerUser = IcePy.Operation(
    "registerUser",
    "registerUser",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_UserInfoMap_t, False, 0),),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_unregisterUser = IcePy.Operation(
    "unregisterUser",
    "unregisterUser",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_updateRegistration = IcePy.Operation(
    "updateRegistration",
    "updateRegistration",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), _MumbleServer_UserInfoMap_t, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getRegistration = IcePy.Operation(
    "getRegistration",
    "getRegistration",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_UserInfoMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getRegisteredUsers = IcePy.Operation(
    "getRegisteredUsers",
    "getRegisteredUsers",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    ((), _MumbleServer_NameMap_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_verifyPassword = IcePy.Operation(
    "verifyPassword",
    "verifyPassword",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getTexture = IcePy.Operation(
    "getTexture",
    "getTexture",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_Texture_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_setTexture = IcePy.Operation(
    "setTexture",
    "setTexture",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), _MumbleServer_Texture_t, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidTextureException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_getUptime = IcePy.Operation(
    "getUptime",
    "getUptime",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_int, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_updateCertificate = IcePy.Operation(
    "updateCertificate",
    "updateCertificate",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_InvalidInputDataException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_startListening = IcePy.Operation(
    "startListening",
    "startListening",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_stopListening = IcePy.Operation(
    "stopListening",
    "stopListening",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_isListening = IcePy.Operation(
    "isListening",
    "isListening",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_bool, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidSecretException_t),
    False)

Server._op_getListeningChannels = IcePy.Operation(
    "getListeningChannels",
    "getListeningChannels",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_IntList_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_InvalidUserException_t),
    False)

Server._op_getListeningUsers = IcePy.Operation(
    "getListeningUsers",
    "getListeningUsers",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_IntList_t, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_InvalidChannelException_t),
    False)

Server._op_getListenerVolumeAdjustment = IcePy.Operation(
    "getListenerVolumeAdjustment",
    "getListenerVolumeAdjustment",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_float, False, 0),
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_InvalidChannelException_t),
    False)

Server._op_setListenerVolumeAdjustment = IcePy.Operation(
    "setListenerVolumeAdjustment",
    "setListenerVolumeAdjustment",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_float, False, 0)),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_InvalidChannelException_t, _MumbleServer_InvalidUserException_t, _MumbleServer_ReadOnlyModeException_t),
    False)

Server._op_sendWelcomeMessage = IcePy.Operation(
    "sendWelcomeMessage",
    "sendWelcomeMessage",
    OperationMode.Idempotent,
    None,
    (),
    (((), _MumbleServer_IdList_t, False, 0),),
    (),
    None,
    (_MumbleServer_ServerBootedException_t, _MumbleServer_InvalidSecretException_t, _MumbleServer_InvalidUserException_t),
    False)

__all__ = ["Server", "ServerPrx", "_MumbleServer_ServerPrx_t"]
