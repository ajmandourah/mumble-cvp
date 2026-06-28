# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from MumbleServer.CertificateList import _MumbleServer_CertificateList_t

from MumbleServer.GroupNameList import _MumbleServer_GroupNameList_t

from MumbleServer.NameMap import _MumbleServer_NameMap_t

from MumbleServer.ServerAuthenticator import ServerAuthenticator
from MumbleServer.ServerAuthenticator import ServerAuthenticatorPrx

from MumbleServer.ServerUpdatingAuthenticator_forward import _MumbleServer_ServerUpdatingAuthenticatorPrx_t

from MumbleServer.Texture import _MumbleServer_Texture_t

from MumbleServer.UserInfoMap import _MumbleServer_UserInfoMap_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from Ice.ObjectPrx import ObjectPrx
    from MumbleServer.UserInfo import UserInfo
    from collections.abc import Awaitable
    from collections.abc import Buffer
    from collections.abc import Mapping
    from collections.abc import Sequence


class ServerUpdatingAuthenticatorPrx(ServerAuthenticatorPrx):
    """
    Callback interface for server authentication and registration. This allows you to support both authentication
    and account updating.
    You do not need to implement this if all you want is authentication, you only need this if other scripts
    connected to the same server calls e.g. ``Server.setTexture``.
    Almost all of these methods support fall through, meaning the server should continue the operation against its
    own database.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::ServerUpdatingAuthenticator``.
    """

    def registerUser(self, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> int:
        """
        Register a new user.
        
        Parameters
        ----------
        info : Mapping[UserInfo, str]
            Information about user to register.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            User id of new user, -1 for registration failure, or -2 to fall through.
        """
        return ServerUpdatingAuthenticator._op_registerUser.invoke(self, ((info, ), context))

    def registerUserAsync(self, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Register a new user.
        
        Parameters
        ----------
        info : Mapping[UserInfo, str]
            Information about user to register.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            User id of new user, -1 for registration failure, or -2 to fall through.
        """
        return ServerUpdatingAuthenticator._op_registerUser.invokeAsync(self, ((info, ), context))

    def unregisterUser(self, id: int, context: dict[str, str] | None = None) -> int:
        """
        Unregister a user.
        
        Parameters
        ----------
        id : int
            Userid to unregister.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            1 for successful unregistration, 0 for unsuccessful unregistration, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_unregisterUser.invoke(self, ((id, ), context))

    def unregisterUserAsync(self, id: int, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Unregister a user.
        
        Parameters
        ----------
        id : int
            Userid to unregister.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            1 for successful unregistration, 0 for unsuccessful unregistration, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_unregisterUser.invokeAsync(self, ((id, ), context))

    def getRegisteredUsers(self, filter: str, context: dict[str, str] | None = None) -> dict[int, str]:
        """
        Get a list of registered users matching filter.
        
        Parameters
        ----------
        filter : str
            Substring usernames must contain. If empty, return all registered users.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        dict[int, str]
            List of matching registered users.
        """
        return ServerUpdatingAuthenticator._op_getRegisteredUsers.invoke(self, ((filter, ), context))

    def getRegisteredUsersAsync(self, filter: str, context: dict[str, str] | None = None) -> Awaitable[dict[int, str]]:
        """
        Get a list of registered users matching filter.
        
        Parameters
        ----------
        filter : str
            Substring usernames must contain. If empty, return all registered users.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[dict[int, str]]
            List of matching registered users.
        """
        return ServerUpdatingAuthenticator._op_getRegisteredUsers.invokeAsync(self, ((filter, ), context))

    def setInfo(self, id: int, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> int:
        """
        Set additional information for user registration.
        
        Parameters
        ----------
        id : int
            Userid of registered user.
        info : Mapping[UserInfo, str]
            Information to set about user. This should be merged with existing information.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_setInfo.invoke(self, ((id, info), context))

    def setInfoAsync(self, id: int, info: Mapping[UserInfo, str], context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Set additional information for user registration.
        
        Parameters
        ----------
        id : int
            Userid of registered user.
        info : Mapping[UserInfo, str]
            Information to set about user. This should be merged with existing information.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_setInfo.invokeAsync(self, ((id, info), context))

    def setTexture(self, id: int, tex: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> int:
        """
        Set texture (now called avatar) of user registration.
        
        Parameters
        ----------
        id : int
            registrationId of registered user.
        tex : Sequence[int] | bytes | Buffer
            New texture.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_setTexture.invoke(self, ((id, tex), context))

    def setTextureAsync(self, id: int, tex: Sequence[int] | bytes | Buffer, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Set texture (now called avatar) of user registration.
        
        Parameters
        ----------
        id : int
            registrationId of registered user.
        tex : Sequence[int] | bytes | Buffer
            New texture.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        return ServerUpdatingAuthenticator._op_setTexture.invokeAsync(self, ((id, tex), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ServerUpdatingAuthenticatorPrx | None:
        return checkedCast(ServerUpdatingAuthenticatorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ServerUpdatingAuthenticatorPrx | None ]:
        return checkedCastAsync(ServerUpdatingAuthenticatorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ServerUpdatingAuthenticatorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ServerUpdatingAuthenticatorPrx | None:
        return uncheckedCast(ServerUpdatingAuthenticatorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerUpdatingAuthenticator"

IcePy.defineProxy("::MumbleServer::ServerUpdatingAuthenticator", ServerUpdatingAuthenticatorPrx)

class ServerUpdatingAuthenticator(ServerAuthenticator, ABC):
    """
    Callback interface for server authentication and registration. This allows you to support both authentication
    and account updating.
    You do not need to implement this if all you want is authentication, you only need this if other scripts
    connected to the same server calls e.g. ``Server.setTexture``.
    Almost all of these methods support fall through, meaning the server should continue the operation against its
    own database.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::ServerUpdatingAuthenticator``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::ServerAuthenticator", "::MumbleServer::ServerUpdatingAuthenticator", )
    _op_registerUser: IcePy.Operation
    _op_unregisterUser: IcePy.Operation
    _op_getRegisteredUsers: IcePy.Operation
    _op_setInfo: IcePy.Operation
    _op_setTexture: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerUpdatingAuthenticator"

    @abstractmethod
    def registerUser(self, info: dict[UserInfo, str], current: Current) -> int | Awaitable[int]:
        """
        Register a new user.
        
        Parameters
        ----------
        info : dict[UserInfo, str]
            Information about user to register.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            User id of new user, -1 for registration failure, or -2 to fall through.
        """
        pass

    @abstractmethod
    def unregisterUser(self, id: int, current: Current) -> int | Awaitable[int]:
        """
        Unregister a user.
        
        Parameters
        ----------
        id : int
            Userid to unregister.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            1 for successful unregistration, 0 for unsuccessful unregistration, -1 to fall through.
        """
        pass

    @abstractmethod
    def getRegisteredUsers(self, filter: str, current: Current) -> Mapping[int, str] | Awaitable[Mapping[int, str]]:
        """
        Get a list of registered users matching filter.
        
        Parameters
        ----------
        filter : str
            Substring usernames must contain. If empty, return all registered users.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Mapping[int, str] | Awaitable[Mapping[int, str]]
            List of matching registered users.
        """
        pass

    @abstractmethod
    def setInfo(self, id: int, info: dict[UserInfo, str], current: Current) -> int | Awaitable[int]:
        """
        Set additional information for user registration.
        
        Parameters
        ----------
        id : int
            Userid of registered user.
        info : dict[UserInfo, str]
            Information to set about user. This should be merged with existing information.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        pass

    @abstractmethod
    def setTexture(self, id: int, tex: bytes, current: Current) -> int | Awaitable[int]:
        """
        Set texture (now called avatar) of user registration.
        
        Parameters
        ----------
        id : int
            registrationId of registered user.
        tex : bytes
            New texture.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            1 for successful update, 0 for unsuccessful update, -1 to fall through.
        """
        pass

ServerUpdatingAuthenticator._op_registerUser = IcePy.Operation(
    "registerUser",
    "registerUser",
    OperationMode.Normal,
    None,
    (),
    (((), _MumbleServer_UserInfoMap_t, False, 0),),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

ServerUpdatingAuthenticator._op_unregisterUser = IcePy.Operation(
    "unregisterUser",
    "unregisterUser",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

ServerUpdatingAuthenticator._op_getRegisteredUsers = IcePy.Operation(
    "getRegisteredUsers",
    "getRegisteredUsers",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    ((), _MumbleServer_NameMap_t, False, 0),
    (),
    False)

ServerUpdatingAuthenticator._op_setInfo = IcePy.Operation(
    "setInfo",
    "setInfo",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), _MumbleServer_UserInfoMap_t, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

ServerUpdatingAuthenticator._op_setTexture = IcePy.Operation(
    "setTexture",
    "setTexture",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), _MumbleServer_Texture_t, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

__all__ = ["ServerUpdatingAuthenticator", "ServerUpdatingAuthenticatorPrx", "_MumbleServer_ServerUpdatingAuthenticatorPrx_t"]
