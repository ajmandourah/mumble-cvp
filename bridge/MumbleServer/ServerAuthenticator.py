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

from MumbleServer.CertificateList import _MumbleServer_CertificateList_t

from MumbleServer.GroupNameList import _MumbleServer_GroupNameList_t

from MumbleServer.ServerAuthenticator_forward import _MumbleServer_ServerAuthenticatorPrx_t

from MumbleServer.Texture import _MumbleServer_Texture_t

from MumbleServer.UserInfoMap import _MumbleServer_UserInfoMap_t

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from MumbleServer.UserInfo import UserInfo
    from collections.abc import Awaitable
    from collections.abc import Buffer
    from collections.abc import Mapping
    from collections.abc import Sequence


class ServerAuthenticatorPrx(ObjectPrx):
    """
    Callback interface for server authentication. You need to supply one of these for ``Server.setAuthenticator``.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that unlike :class:`MumbleServer.ServerCallbackPrx` and :class:`MumbleServer.ServerContextCallbackPrx`, these methods are called
    synchronously. If the response lags, the entire server will lag.
    Also note that, as the method calls are synchronous, making a call to :class:`MumbleServer.ServerPrx` or :class:`MumbleServer.MetaPrx` will
    deadlock the server.
    
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::MumbleServer::ServerAuthenticator``.
    """

    def authenticate(self, name: str, pw: str, certificates: Sequence[Sequence[int] | bytes | Buffer], certhash: str, certstrong: bool, context: dict[str, str] | None = None) -> tuple[int, str, list[str]]:
        """
        Called to authenticate a user. If you do not know the username in question, always return -2 from this
        method to fall through to normal database authentication.
        Note that if authentication succeeds, the server will create a record of the user in it's database, reserving
        the username and id so it cannot be used for normal database authentication.
        The data in the certificate (name, email addresses etc), as well as the list of signing certificates,
        should only be trusted if certstrong is true.
        
        Internally, the server treats usernames as case-insensitive. It is recommended
        that authenticators do the same. the server checks if a username is in use when
        a user connects. If the connecting user is registered, the other username is
        kicked. If the connecting user is not registered, the connecting user is not
        allowed to join the server.
        
        Parameters
        ----------
        name : str
            Username to authenticate.
        pw : str
            Password to authenticate with.
        certificates : Sequence[Sequence[int] | bytes | Buffer]
            List of der encoded certificates the user connected with.
        certhash : str
            Hash of user certificate, as used by the server internally when matching.
        certstrong : bool
            True if certificate was valid and signed by a trusted CA.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        tuple[int, str, list[str]]
        
            A tuple containing:
                - int UserID of authenticated user, -1 for authentication failures, -2 for unknown user (fallthrough),
                  -3 for authentication failures where the data could (temporarily) not be verified.
                - str Set this to change the username from the supplied one.
                - list[str] List of groups on the root channel that the user will be added to for the duration of the connection.
        """
        return ServerAuthenticator._op_authenticate.invoke(self, ((name, pw, certificates, certhash, certstrong), context))

    def authenticateAsync(self, name: str, pw: str, certificates: Sequence[Sequence[int] | bytes | Buffer], certhash: str, certstrong: bool, context: dict[str, str] | None = None) -> Awaitable[tuple[int, str, list[str]]]:
        """
        Called to authenticate a user. If you do not know the username in question, always return -2 from this
        method to fall through to normal database authentication.
        Note that if authentication succeeds, the server will create a record of the user in it's database, reserving
        the username and id so it cannot be used for normal database authentication.
        The data in the certificate (name, email addresses etc), as well as the list of signing certificates,
        should only be trusted if certstrong is true.
        
        Internally, the server treats usernames as case-insensitive. It is recommended
        that authenticators do the same. the server checks if a username is in use when
        a user connects. If the connecting user is registered, the other username is
        kicked. If the connecting user is not registered, the connecting user is not
        allowed to join the server.
        
        Parameters
        ----------
        name : str
            Username to authenticate.
        pw : str
            Password to authenticate with.
        certificates : Sequence[Sequence[int] | bytes | Buffer]
            List of der encoded certificates the user connected with.
        certhash : str
            Hash of user certificate, as used by the server internally when matching.
        certstrong : bool
            True if certificate was valid and signed by a trusted CA.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[tuple[int, str, list[str]]]
        
            A tuple containing:
                - int UserID of authenticated user, -1 for authentication failures, -2 for unknown user (fallthrough),
                  -3 for authentication failures where the data could (temporarily) not be verified.
                - str Set this to change the username from the supplied one.
                - list[str] List of groups on the root channel that the user will be added to for the duration of the connection.
        """
        return ServerAuthenticator._op_authenticate.invokeAsync(self, ((name, pw, certificates, certhash, certstrong), context))

    def getInfo(self, id: int, context: dict[str, str] | None = None) -> tuple[bool, dict[UserInfo, str]]:
        """
        Fetch information about a user. This is used to retrieve information like email address, keyhash etc. If you
        want the server to take care of this information itself, simply return false to fall through.
        
        Parameters
        ----------
        id : int
            User id.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        tuple[bool, dict[UserInfo, str]]
        
            A tuple containing:
                - bool true if information is present, false to fall through.
                - dict[UserInfo, str] Information about user. This needs to include at least "name".
        """
        return ServerAuthenticator._op_getInfo.invoke(self, ((id, ), context))

    def getInfoAsync(self, id: int, context: dict[str, str] | None = None) -> Awaitable[tuple[bool, dict[UserInfo, str]]]:
        """
        Fetch information about a user. This is used to retrieve information like email address, keyhash etc. If you
        want the server to take care of this information itself, simply return false to fall through.
        
        Parameters
        ----------
        id : int
            User id.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[tuple[bool, dict[UserInfo, str]]]
        
            A tuple containing:
                - bool true if information is present, false to fall through.
                - dict[UserInfo, str] Information about user. This needs to include at least "name".
        """
        return ServerAuthenticator._op_getInfo.invokeAsync(self, ((id, ), context))

    def nameToId(self, name: str, context: dict[str, str] | None = None) -> int:
        """
        Map a name to a user id.
        
        Parameters
        ----------
        name : str
            Username to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        int
            User id or -2 for unknown name.
        """
        return ServerAuthenticator._op_nameToId.invoke(self, ((name, ), context))

    def nameToIdAsync(self, name: str, context: dict[str, str] | None = None) -> Awaitable[int]:
        """
        Map a name to a user id.
        
        Parameters
        ----------
        name : str
            Username to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[int]
            User id or -2 for unknown name.
        """
        return ServerAuthenticator._op_nameToId.invokeAsync(self, ((name, ), context))

    def idToName(self, id: int, context: dict[str, str] | None = None) -> str:
        """
        Map a user id to a username.
        
        Parameters
        ----------
        id : int
            User id to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        str
            Name of user or empty string for unknown id.
        """
        return ServerAuthenticator._op_idToName.invoke(self, ((id, ), context))

    def idToNameAsync(self, id: int, context: dict[str, str] | None = None) -> Awaitable[str]:
        """
        Map a user id to a username.
        
        Parameters
        ----------
        id : int
            User id to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[str]
            Name of user or empty string for unknown id.
        """
        return ServerAuthenticator._op_idToName.invokeAsync(self, ((id, ), context))

    def idToTexture(self, id: int, context: dict[str, str] | None = None) -> bytes:
        """
        Map a user to a custom Texture.
        
        Parameters
        ----------
        id : int
            User id to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        bytes
            User texture or an empty texture for unknown users or users without textures.
        """
        return ServerAuthenticator._op_idToTexture.invoke(self, ((id, ), context))

    def idToTextureAsync(self, id: int, context: dict[str, str] | None = None) -> Awaitable[bytes]:
        """
        Map a user to a custom Texture.
        
        Parameters
        ----------
        id : int
            User id to map.
        context : dict[str, str]
            The request context for the invocation.
        
        Returns
        -------
        Awaitable[bytes]
            User texture or an empty texture for unknown users or users without textures.
        """
        return ServerAuthenticator._op_idToTexture.invokeAsync(self, ((id, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> ServerAuthenticatorPrx | None:
        return checkedCast(ServerAuthenticatorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[ServerAuthenticatorPrx | None ]:
        return checkedCastAsync(ServerAuthenticatorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> ServerAuthenticatorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> ServerAuthenticatorPrx | None:
        return uncheckedCast(ServerAuthenticatorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerAuthenticator"

IcePy.defineProxy("::MumbleServer::ServerAuthenticator", ServerAuthenticatorPrx)

class ServerAuthenticator(Object, ABC):
    """
    Callback interface for server authentication. You need to supply one of these for ``Server.setAuthenticator``.
    If an added callback ever throws an exception or goes away, it will be automatically removed.
    Please note that unlike :class:`MumbleServer.ServerCallbackPrx` and :class:`MumbleServer.ServerContextCallbackPrx`, these methods are called
    synchronously. If the response lags, the entire server will lag.
    Also note that, as the method calls are synchronous, making a call to :class:`MumbleServer.ServerPrx` or :class:`MumbleServer.MetaPrx` will
    deadlock the server.
    
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::MumbleServer::ServerAuthenticator``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::MumbleServer::ServerAuthenticator", )
    _op_authenticate: IcePy.Operation
    _op_getInfo: IcePy.Operation
    _op_nameToId: IcePy.Operation
    _op_idToName: IcePy.Operation
    _op_idToTexture: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::MumbleServer::ServerAuthenticator"

    @abstractmethod
    def authenticate(self, name: str, pw: str, certificates: list[bytes], certhash: str, certstrong: bool, current: Current) -> tuple[int, str, Sequence[str]] | Awaitable[tuple[int, str, Sequence[str]]]:
        """
        Called to authenticate a user. If you do not know the username in question, always return -2 from this
        method to fall through to normal database authentication.
        Note that if authentication succeeds, the server will create a record of the user in it's database, reserving
        the username and id so it cannot be used for normal database authentication.
        The data in the certificate (name, email addresses etc), as well as the list of signing certificates,
        should only be trusted if certstrong is true.
        
        Internally, the server treats usernames as case-insensitive. It is recommended
        that authenticators do the same. the server checks if a username is in use when
        a user connects. If the connecting user is registered, the other username is
        kicked. If the connecting user is not registered, the connecting user is not
        allowed to join the server.
        
        Parameters
        ----------
        name : str
            Username to authenticate.
        pw : str
            Password to authenticate with.
        certificates : list[bytes]
            List of der encoded certificates the user connected with.
        certhash : str
            Hash of user certificate, as used by the server internally when matching.
        certstrong : bool
            True if certificate was valid and signed by a trusted CA.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        tuple[int, str, Sequence[str]] | Awaitable[tuple[int, str, Sequence[str]]]
        
            A tuple containing:
                - int UserID of authenticated user, -1 for authentication failures, -2 for unknown user (fallthrough),
                  -3 for authentication failures where the data could (temporarily) not be verified.
                - str Set this to change the username from the supplied one.
                - Sequence[str] List of groups on the root channel that the user will be added to for the duration of the connection.
        """
        pass

    @abstractmethod
    def getInfo(self, id: int, current: Current) -> tuple[bool, Mapping[UserInfo, str]] | Awaitable[tuple[bool, Mapping[UserInfo, str]]]:
        """
        Fetch information about a user. This is used to retrieve information like email address, keyhash etc. If you
        want the server to take care of this information itself, simply return false to fall through.
        
        Parameters
        ----------
        id : int
            User id.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        tuple[bool, Mapping[UserInfo, str]] | Awaitable[tuple[bool, Mapping[UserInfo, str]]]
        
            A tuple containing:
                - bool true if information is present, false to fall through.
                - Mapping[UserInfo, str] Information about user. This needs to include at least "name".
        """
        pass

    @abstractmethod
    def nameToId(self, name: str, current: Current) -> int | Awaitable[int]:
        """
        Map a name to a user id.
        
        Parameters
        ----------
        name : str
            Username to map.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        int | Awaitable[int]
            User id or -2 for unknown name.
        """
        pass

    @abstractmethod
    def idToName(self, id: int, current: Current) -> str | Awaitable[str]:
        """
        Map a user id to a username.
        
        Parameters
        ----------
        id : int
            User id to map.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        str | Awaitable[str]
            Name of user or empty string for unknown id.
        """
        pass

    @abstractmethod
    def idToTexture(self, id: int, current: Current) -> Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]:
        """
        Map a user to a custom Texture.
        
        Parameters
        ----------
        id : int
            User id to map.
        current : Ice.Current
            The Current object for the dispatch.
        
        Returns
        -------
        Sequence[int] | bytes | Buffer | Awaitable[Sequence[int] | bytes | Buffer]
            User texture or an empty texture for unknown users or users without textures.
        """
        pass

ServerAuthenticator._op_authenticate = IcePy.Operation(
    "authenticate",
    "authenticate",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), _MumbleServer_CertificateList_t, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_bool, False, 0)),
    (((), IcePy._t_string, False, 0), ((), _MumbleServer_GroupNameList_t, False, 0)),
    ((), IcePy._t_int, False, 0),
    (),
    False)

ServerAuthenticator._op_getInfo = IcePy.Operation(
    "getInfo",
    "getInfo",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (((), _MumbleServer_UserInfoMap_t, False, 0),),
    ((), IcePy._t_bool, False, 0),
    (),
    False)

ServerAuthenticator._op_nameToId = IcePy.Operation(
    "nameToId",
    "nameToId",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    ((), IcePy._t_int, False, 0),
    (),
    False)

ServerAuthenticator._op_idToName = IcePy.Operation(
    "idToName",
    "idToName",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), IcePy._t_string, False, 0),
    (),
    False)

ServerAuthenticator._op_idToTexture = IcePy.Operation(
    "idToTexture",
    "idToTexture",
    OperationMode.Idempotent,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    ((), _MumbleServer_Texture_t, False, 0),
    (),
    False)

__all__ = ["ServerAuthenticator", "ServerAuthenticatorPrx", "_MumbleServer_ServerAuthenticatorPrx_t"]
