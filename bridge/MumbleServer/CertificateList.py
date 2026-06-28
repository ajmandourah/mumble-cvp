# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.2

from __future__ import annotations
import IcePy

from MumbleServer.CertificateDer import _MumbleServer_CertificateDer_t

_MumbleServer_CertificateList_t = IcePy.defineSequence("::MumbleServer::CertificateList", (), _MumbleServer_CertificateDer_t)

__all__ = ["_MumbleServer_CertificateList_t"]
