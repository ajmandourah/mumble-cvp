
# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

import IcePy

_ice_define = IcePy.defineException

def _compat_defineException(*args, **kwargs):
    try:
        return _ice_define(*args, **kwargs)
    except TypeError:
        base = args[3] if args[3] is not None else -1
        return _ice_define(args[0], args[1], args[2], base, args[4], "")

IcePy.defineException = _compat_defineException

from .ACL import ACL
from .ACL import _MumbleServer_ACL_t
from .ACLList import _MumbleServer_ACLList_t
from .Ban import Ban
from .Ban import _MumbleServer_Ban_t
from .BanList import _MumbleServer_BanList_t
from .CertificateDer import _MumbleServer_CertificateDer_t
from .CertificateList import _MumbleServer_CertificateList_t
from .Channel import Channel
from .Channel import _MumbleServer_Channel_t
from .ChannelInfo import ChannelInfo
from .ChannelInfo import _MumbleServer_ChannelInfo_t
from .ChannelList import _MumbleServer_ChannelList_t
from .ChannelMap import _MumbleServer_ChannelMap_t
from .ConfigMap import _MumbleServer_ConfigMap_t
from .ContextChannel import ContextChannel
from .ContextServer import ContextServer
from .ContextUser import ContextUser
from .DBState import DBState
from .DBState import _MumbleServer_DBState_t
from .Group import Group
from .Group import _MumbleServer_Group_t
from .GroupList import _MumbleServer_GroupList_t
from .GroupNameList import _MumbleServer_GroupNameList_t
from .IdList import _MumbleServer_IdList_t
from .IdMap import _MumbleServer_IdMap_t
from .IntList import _MumbleServer_IntList_t
from .InternalErrorException import InternalErrorException
from .InternalErrorException import _MumbleServer_InternalErrorException_t
from .InvalidCallbackException import InvalidCallbackException
from .InvalidCallbackException import _MumbleServer_InvalidCallbackException_t
from .InvalidChannelException import InvalidChannelException
from .InvalidChannelException import _MumbleServer_InvalidChannelException_t
from .InvalidInputDataException import InvalidInputDataException
from .InvalidInputDataException import _MumbleServer_InvalidInputDataException_t
from .InvalidListenerException import InvalidListenerException
from .InvalidListenerException import _MumbleServer_InvalidListenerException_t
from .InvalidSecretException import InvalidSecretException
from .InvalidSecretException import _MumbleServer_InvalidSecretException_t
from .InvalidServerException import InvalidServerException
from .InvalidServerException import _MumbleServer_InvalidServerException_t
from .InvalidSessionException import InvalidSessionException
from .InvalidSessionException import _MumbleServer_InvalidSessionException_t
from .InvalidTextureException import InvalidTextureException
from .InvalidTextureException import _MumbleServer_InvalidTextureException_t
from .InvalidUserException import InvalidUserException
from .InvalidUserException import _MumbleServer_InvalidUserException_t
from .LogEntry import LogEntry
from .LogEntry import _MumbleServer_LogEntry_t
from .LogList import _MumbleServer_LogList_t
from .Meta import Meta
from .Meta import MetaPrx
from .MetaCallback import MetaCallback
from .MetaCallback import MetaCallbackPrx
from .MetaCallback_forward import _MumbleServer_MetaCallbackPrx_t
from .Meta_forward import _MumbleServer_MetaPrx_t
from .NameList import _MumbleServer_NameList_t
from .NameMap import _MumbleServer_NameMap_t
from .NestingLimitException import NestingLimitException
from .NestingLimitException import _MumbleServer_NestingLimitException_t
from .NetAddress import _MumbleServer_NetAddress_t
from .PermissionBan import PermissionBan
from .PermissionEnter import PermissionEnter
from .PermissionKick import PermissionKick
from .PermissionLinkChannel import PermissionLinkChannel
from .PermissionMakeChannel import PermissionMakeChannel
from .PermissionMakeTempChannel import PermissionMakeTempChannel
from .PermissionMove import PermissionMove
from .PermissionMuteDeafen import PermissionMuteDeafen
from .PermissionRegister import PermissionRegister
from .PermissionRegisterSelf import PermissionRegisterSelf
from .PermissionSpeak import PermissionSpeak
from .PermissionTextMessage import PermissionTextMessage
from .PermissionTraverse import PermissionTraverse
from .PermissionWhisper import PermissionWhisper
from .PermissionWrite import PermissionWrite
from .ReadOnlyModeException import ReadOnlyModeException
from .ReadOnlyModeException import _MumbleServer_ReadOnlyModeException_t
from .ResetUserContent import ResetUserContent
from .Server import Server
from .Server import ServerPrx
from .ServerAuthenticator import ServerAuthenticator
from .ServerAuthenticator import ServerAuthenticatorPrx
from .ServerAuthenticator_forward import _MumbleServer_ServerAuthenticatorPrx_t
from .ServerBootedException import ServerBootedException
from .ServerBootedException import _MumbleServer_ServerBootedException_t
from .ServerCallback import ServerCallback
from .ServerCallback import ServerCallbackPrx
from .ServerCallback_forward import _MumbleServer_ServerCallbackPrx_t
from .ServerContextCallback import ServerContextCallback
from .ServerContextCallback import ServerContextCallbackPrx
from .ServerContextCallback_forward import _MumbleServer_ServerContextCallbackPrx_t
from .ServerException import ServerException
from .ServerException import _MumbleServer_ServerException_t
from .ServerFailureException import ServerFailureException
from .ServerFailureException import _MumbleServer_ServerFailureException_t
from .ServerList import _MumbleServer_ServerList_t
from .ServerUpdatingAuthenticator import ServerUpdatingAuthenticator
from .ServerUpdatingAuthenticator import ServerUpdatingAuthenticatorPrx
from .ServerUpdatingAuthenticator_forward import _MumbleServer_ServerUpdatingAuthenticatorPrx_t
from .Server_forward import _MumbleServer_ServerPrx_t
from .TextMessage import TextMessage
from .TextMessage import _MumbleServer_TextMessage_t
from .Texture import _MumbleServer_Texture_t
from .Tree import Tree
from .TreeList import _MumbleServer_TreeList_t
from .Tree_forward import _MumbleServer_Tree_t
from .User import User
from .User import _MumbleServer_User_t
from .UserInfo import UserInfo
from .UserInfo import _MumbleServer_UserInfo_t
from .UserInfoMap import _MumbleServer_UserInfoMap_t
from .UserList import _MumbleServer_UserList_t
from .UserMap import _MumbleServer_UserMap_t
from .WriteOnlyException import WriteOnlyException
from .WriteOnlyException import _MumbleServer_WriteOnlyException_t


__all__ = [
    "ACL",
    "_MumbleServer_ACL_t",
    "_MumbleServer_ACLList_t",
    "Ban",
    "_MumbleServer_Ban_t",
    "_MumbleServer_BanList_t",
    "_MumbleServer_CertificateDer_t",
    "_MumbleServer_CertificateList_t",
    "Channel",
    "_MumbleServer_Channel_t",
    "ChannelInfo",
    "_MumbleServer_ChannelInfo_t",
    "_MumbleServer_ChannelList_t",
    "_MumbleServer_ChannelMap_t",
    "_MumbleServer_ConfigMap_t",
    "ContextChannel",
    "ContextServer",
    "ContextUser",
    "DBState",
    "_MumbleServer_DBState_t",
    "Group",
    "_MumbleServer_Group_t",
    "_MumbleServer_GroupList_t",
    "_MumbleServer_GroupNameList_t",
    "_MumbleServer_IdList_t",
    "_MumbleServer_IdMap_t",
    "_MumbleServer_IntList_t",
    "InternalErrorException",
    "_MumbleServer_InternalErrorException_t",
    "InvalidCallbackException",
    "_MumbleServer_InvalidCallbackException_t",
    "InvalidChannelException",
    "_MumbleServer_InvalidChannelException_t",
    "InvalidInputDataException",
    "_MumbleServer_InvalidInputDataException_t",
    "InvalidListenerException",
    "_MumbleServer_InvalidListenerException_t",
    "InvalidSecretException",
    "_MumbleServer_InvalidSecretException_t",
    "InvalidServerException",
    "_MumbleServer_InvalidServerException_t",
    "InvalidSessionException",
    "_MumbleServer_InvalidSessionException_t",
    "InvalidTextureException",
    "_MumbleServer_InvalidTextureException_t",
    "InvalidUserException",
    "_MumbleServer_InvalidUserException_t",
    "LogEntry",
    "_MumbleServer_LogEntry_t",
    "_MumbleServer_LogList_t",
    "Meta",
    "MetaPrx",
    "MetaCallback",
    "MetaCallbackPrx",
    "_MumbleServer_MetaCallbackPrx_t",
    "_MumbleServer_MetaPrx_t",
    "_MumbleServer_NameList_t",
    "_MumbleServer_NameMap_t",
    "NestingLimitException",
    "_MumbleServer_NestingLimitException_t",
    "_MumbleServer_NetAddress_t",
    "PermissionBan",
    "PermissionEnter",
    "PermissionKick",
    "PermissionLinkChannel",
    "PermissionMakeChannel",
    "PermissionMakeTempChannel",
    "PermissionMove",
    "PermissionMuteDeafen",
    "PermissionRegister",
    "PermissionRegisterSelf",
    "PermissionSpeak",
    "PermissionTextMessage",
    "PermissionTraverse",
    "PermissionWhisper",
    "PermissionWrite",
    "ReadOnlyModeException",
    "_MumbleServer_ReadOnlyModeException_t",
    "ResetUserContent",
    "Server",
    "ServerPrx",
    "ServerAuthenticator",
    "ServerAuthenticatorPrx",
    "_MumbleServer_ServerAuthenticatorPrx_t",
    "ServerBootedException",
    "_MumbleServer_ServerBootedException_t",
    "ServerCallback",
    "ServerCallbackPrx",
    "_MumbleServer_ServerCallbackPrx_t",
    "ServerContextCallback",
    "ServerContextCallbackPrx",
    "_MumbleServer_ServerContextCallbackPrx_t",
    "ServerException",
    "_MumbleServer_ServerException_t",
    "ServerFailureException",
    "_MumbleServer_ServerFailureException_t",
    "_MumbleServer_ServerList_t",
    "ServerUpdatingAuthenticator",
    "ServerUpdatingAuthenticatorPrx",
    "_MumbleServer_ServerUpdatingAuthenticatorPrx_t",
    "_MumbleServer_ServerPrx_t",
    "TextMessage",
    "_MumbleServer_TextMessage_t",
    "_MumbleServer_Texture_t",
    "Tree",
    "_MumbleServer_TreeList_t",
    "_MumbleServer_Tree_t",
    "User",
    "_MumbleServer_User_t",
    "UserInfo",
    "_MumbleServer_UserInfo_t",
    "_MumbleServer_UserInfoMap_t",
    "_MumbleServer_UserList_t",
    "_MumbleServer_UserMap_t",
    "WriteOnlyException",
    "_MumbleServer_WriteOnlyException_t"
]
