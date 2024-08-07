# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NFTypeAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NRF = "NRF"
    UDM = "UDM"
    AMF = "AMF"
    SMF = "SMF"
    AUSF = "AUSF"
    NEF = "NEF"
    PCF = "PCF"
    SMSF = "SMSF"
    NSSF = "NSSF"
    UDR = "UDR"
    LMF = "LMF"
    GMLC = "GMLC"
    _5G_EIR = "5G_EIR"
    SEPP = "SEPP"
    UPF = "UPF"
    N3IWF = "N3IWF"
    AF = "AF"
    UDSF = "UDSF"
    BSF = "BSF"
    CHF = "CHF"
    NWDAF = "NWDAF"
    PCSCF = "PCSCF"
    CBCF = "CBCF"
    HSS = "HSS"
    UCMF = "UCMF"
    SOR_AF = "SOR_AF"
    SPAF = "SPAF"
    MME = "MME"
    SCSAS = "SCSAS"
    SCEF = "SCEF"
    SCP = "SCP"
    NSSAAF = "NSSAAF"
    ICSCF = "ICSCF"
    SCSCF = "SCSCF"
    DRA = "DRA"
    IMS_AS = "IMS_AS"
    AANF = "AANF"
    _5G_DDNMF = "5G_DDNMF"
    NSACF = "NSACF"
    MFAF = "MFAF"
    EASDF = "EASDF"
    DCCF = "DCCF"
    MB_SMF = "MB_SMF"
    TSCTSF = "TSCTSF"
    ADRF = "ADRF"
    GBA_BSF = "GBA_BSF"
    CEF = "CEF"
    MB_UPF = "MB_UPF"
    NSWOF = "NSWOF"
    PKMF = "PKMF"
    MNPF = "MNPF"
    SMS_GMSC = "SMS_GMSC"
    SMS_IWMSC = "SMS_IWMSC"
    MBSF = "MBSF"
    MBSTF = "MBSTF"
    def __init__(self):  # noqa: E501
        """NFTypeAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'NFTypeAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NFType_anyOf of this NFTypeAnyOf.  # noqa: E501
        :rtype: NFTypeAnyOf
        """
        return util.deserialize_model(dikt, cls)
