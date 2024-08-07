# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.gnb_id import GNbId
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.gnb_id import GNbId  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class GlobalRanNodeId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, n3_iwf_id=None, g_nb_id=None, nge_nb_id=None, wagf_id=None, tngf_id=None, nid=None, e_nb_id=None):  # noqa: E501
        """GlobalRanNodeId - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this GlobalRanNodeId.  # noqa: E501
        :type plmn_id: PlmnId
        :param n3_iwf_id: The n3_iwf_id of this GlobalRanNodeId.  # noqa: E501
        :type n3_iwf_id: str
        :param g_nb_id: The g_nb_id of this GlobalRanNodeId.  # noqa: E501
        :type g_nb_id: GNbId
        :param nge_nb_id: The nge_nb_id of this GlobalRanNodeId.  # noqa: E501
        :type nge_nb_id: str
        :param wagf_id: The wagf_id of this GlobalRanNodeId.  # noqa: E501
        :type wagf_id: str
        :param tngf_id: The tngf_id of this GlobalRanNodeId.  # noqa: E501
        :type tngf_id: str
        :param nid: The nid of this GlobalRanNodeId.  # noqa: E501
        :type nid: str
        :param e_nb_id: The e_nb_id of this GlobalRanNodeId.  # noqa: E501
        :type e_nb_id: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'n3_iwf_id': str,
            'g_nb_id': GNbId,
            'nge_nb_id': str,
            'wagf_id': str,
            'tngf_id': str,
            'nid': str,
            'e_nb_id': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'n3_iwf_id': 'n3IwfId',
            'g_nb_id': 'gNbId',
            'nge_nb_id': 'ngeNbId',
            'wagf_id': 'wagfId',
            'tngf_id': 'tngfId',
            'nid': 'nid',
            'e_nb_id': 'eNbId'
        }

        self.plmn_id = plmn_id
        self.n3_iwf_id = n3_iwf_id
        self.g_nb_id = g_nb_id
        self.nge_nb_id = nge_nb_id
        self.wagf_id = wagf_id
        self.tngf_id = tngf_id
        self.nid = nid
        self.e_nb_id = e_nb_id

    @classmethod
    def from_dict(cls, dikt) -> 'GlobalRanNodeId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GlobalRanNodeId of this GlobalRanNodeId.  # noqa: E501
        :rtype: GlobalRanNodeId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this GlobalRanNodeId.


        :return: The plmn_id of this GlobalRanNodeId.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this GlobalRanNodeId.


        :param plmn_id: The plmn_id of this GlobalRanNodeId.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def n3_iwf_id(self):
        """Gets the n3_iwf_id of this GlobalRanNodeId.

        This represents the identifier of the N3IWF ID as specified in clause 9.3.1.57 of  3GPP TS 38.413 in hexadecimal representation. Each character in the string shall take a value  of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant  character representing the 4 most significant bits of the N3IWF ID shall appear first in the  string, and the character representing the 4 least significant bit of the N3IWF ID shall  appear last in the string.    # noqa: E501

        :return: The n3_iwf_id of this GlobalRanNodeId.
        :rtype: str
        """
        return self._n3_iwf_id

    @n3_iwf_id.setter
    def n3_iwf_id(self, n3_iwf_id):
        """Sets the n3_iwf_id of this GlobalRanNodeId.

        This represents the identifier of the N3IWF ID as specified in clause 9.3.1.57 of  3GPP TS 38.413 in hexadecimal representation. Each character in the string shall take a value  of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant  character representing the 4 most significant bits of the N3IWF ID shall appear first in the  string, and the character representing the 4 least significant bit of the N3IWF ID shall  appear last in the string.    # noqa: E501

        :param n3_iwf_id: The n3_iwf_id of this GlobalRanNodeId.
        :type n3_iwf_id: str
        """
        if n3_iwf_id is not None and not re.search(r'^[A-Fa-f0-9]+$', n3_iwf_id):  # noqa: E501
            raise ValueError("Invalid value for `n3_iwf_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]+$/`")  # noqa: E501

        self._n3_iwf_id = n3_iwf_id

    @property
    def g_nb_id(self):
        """Gets the g_nb_id of this GlobalRanNodeId.


        :return: The g_nb_id of this GlobalRanNodeId.
        :rtype: GNbId
        """
        return self._g_nb_id

    @g_nb_id.setter
    def g_nb_id(self, g_nb_id):
        """Sets the g_nb_id of this GlobalRanNodeId.


        :param g_nb_id: The g_nb_id of this GlobalRanNodeId.
        :type g_nb_id: GNbId
        """

        self._g_nb_id = g_nb_id

    @property
    def nge_nb_id(self):
        """Gets the nge_nb_id of this GlobalRanNodeId.

        This represents the identifier of the ng-eNB ID as specified in clause 9.3.1.8 of  3GPP TS 38.413. The value of the ng-eNB ID shall be encoded in hexadecimal representation.  Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and  shall represent 4 bits. The padding 0 shall be added to make multiple nibbles, so the most  significant character representing the padding 0 if required together with the 4 most  significant bits of the ng-eNB ID shall appear first in the string, and the character  representing the 4 least significant bit of the ng-eNB ID (to form a nibble) shall appear last  in the string.    # noqa: E501

        :return: The nge_nb_id of this GlobalRanNodeId.
        :rtype: str
        """
        return self._nge_nb_id

    @nge_nb_id.setter
    def nge_nb_id(self, nge_nb_id):
        """Sets the nge_nb_id of this GlobalRanNodeId.

        This represents the identifier of the ng-eNB ID as specified in clause 9.3.1.8 of  3GPP TS 38.413. The value of the ng-eNB ID shall be encoded in hexadecimal representation.  Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and  shall represent 4 bits. The padding 0 shall be added to make multiple nibbles, so the most  significant character representing the padding 0 if required together with the 4 most  significant bits of the ng-eNB ID shall appear first in the string, and the character  representing the 4 least significant bit of the ng-eNB ID (to form a nibble) shall appear last  in the string.    # noqa: E501

        :param nge_nb_id: The nge_nb_id of this GlobalRanNodeId.
        :type nge_nb_id: str
        """
        if nge_nb_id is not None and not re.search(r'^(MacroNGeNB-[A-Fa-f0-9]{5}|LMacroNGeNB-[A-Fa-f0-9]{6}|SMacroNGeNB-[A-Fa-f0-9]{5})$', nge_nb_id):  # noqa: E501
            raise ValueError("Invalid value for `nge_nb_id`, must be a follow pattern or equal to `/^(MacroNGeNB-[A-Fa-f0-9]{5}|LMacroNGeNB-[A-Fa-f0-9]{6}|SMacroNGeNB-[A-Fa-f0-9]{5})$/`")  # noqa: E501

        self._nge_nb_id = nge_nb_id

    @property
    def wagf_id(self):
        """Gets the wagf_id of this GlobalRanNodeId.

        This represents the identifier of the W-AGF ID as specified in clause 9.3.1.162 of  3GPP TS 38.413 in hexadecimal representation. Each character in the string shall take a value  of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant  character representing the 4 most significant bits of the W-AGF ID shall appear first in the  string, and the character representing the 4 least significant bit of the W-AGF ID shall  appear last in the string.    # noqa: E501

        :return: The wagf_id of this GlobalRanNodeId.
        :rtype: str
        """
        return self._wagf_id

    @wagf_id.setter
    def wagf_id(self, wagf_id):
        """Sets the wagf_id of this GlobalRanNodeId.

        This represents the identifier of the W-AGF ID as specified in clause 9.3.1.162 of  3GPP TS 38.413 in hexadecimal representation. Each character in the string shall take a value  of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant  character representing the 4 most significant bits of the W-AGF ID shall appear first in the  string, and the character representing the 4 least significant bit of the W-AGF ID shall  appear last in the string.    # noqa: E501

        :param wagf_id: The wagf_id of this GlobalRanNodeId.
        :type wagf_id: str
        """
        if wagf_id is not None and not re.search(r'^[A-Fa-f0-9]+$', wagf_id):  # noqa: E501
            raise ValueError("Invalid value for `wagf_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]+$/`")  # noqa: E501

        self._wagf_id = wagf_id

    @property
    def tngf_id(self):
        """Gets the tngf_id of this GlobalRanNodeId.

        This represents the identifier of the TNGF ID as specified in clause 9.3.1.161 of  3GPP TS 38.413  in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\", \"a\"  to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the  4 most significant bits of the TNGF ID shall appear first in the string, and the character  representing the 4 least significant bit of the TNGF ID shall appear last in the string.    # noqa: E501

        :return: The tngf_id of this GlobalRanNodeId.
        :rtype: str
        """
        return self._tngf_id

    @tngf_id.setter
    def tngf_id(self, tngf_id):
        """Sets the tngf_id of this GlobalRanNodeId.

        This represents the identifier of the TNGF ID as specified in clause 9.3.1.161 of  3GPP TS 38.413  in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\", \"a\"  to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the  4 most significant bits of the TNGF ID shall appear first in the string, and the character  representing the 4 least significant bit of the TNGF ID shall appear last in the string.    # noqa: E501

        :param tngf_id: The tngf_id of this GlobalRanNodeId.
        :type tngf_id: str
        """
        if tngf_id is not None and not re.search(r'^[A-Fa-f0-9]+$', tngf_id):  # noqa: E501
            raise ValueError("Invalid value for `tngf_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]+$/`")  # noqa: E501

        self._tngf_id = tngf_id

    @property
    def nid(self):
        """Gets the nid of this GlobalRanNodeId.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :return: The nid of this GlobalRanNodeId.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this GlobalRanNodeId.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :param nid: The nid of this GlobalRanNodeId.
        :type nid: str
        """
        if nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid):  # noqa: E501
            raise ValueError("Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid

    @property
    def e_nb_id(self):
        """Gets the e_nb_id of this GlobalRanNodeId.

        This represents the identifier of the eNB ID as specified in clause 9.2.1.37 of  3GPP TS 36.413. The string shall be formatted with the following pattern  '^('MacroeNB-[A-Fa-f0-9]{5}|LMacroeNB-[A-Fa-f0-9]{6}|SMacroeNB-[A-Fa-f0-9]{5} |HomeeNB-[A-Fa-f0-9]{7})$'. The value of the eNB ID shall be encoded in hexadecimal representation. Each character in the  string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits.  The padding 0 shall be added to make multiple nibbles, so the most significant character  representing the padding 0 if required together with the 4 most significant bits of the eNB ID  shall appear first in the string, and the character representing the 4 least significant bit  of the eNB ID (to form a nibble) shall appear last in the string.   # noqa: E501

        :return: The e_nb_id of this GlobalRanNodeId.
        :rtype: str
        """
        return self._e_nb_id

    @e_nb_id.setter
    def e_nb_id(self, e_nb_id):
        """Sets the e_nb_id of this GlobalRanNodeId.

        This represents the identifier of the eNB ID as specified in clause 9.2.1.37 of  3GPP TS 36.413. The string shall be formatted with the following pattern  '^('MacroeNB-[A-Fa-f0-9]{5}|LMacroeNB-[A-Fa-f0-9]{6}|SMacroeNB-[A-Fa-f0-9]{5} |HomeeNB-[A-Fa-f0-9]{7})$'. The value of the eNB ID shall be encoded in hexadecimal representation. Each character in the  string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits.  The padding 0 shall be added to make multiple nibbles, so the most significant character  representing the padding 0 if required together with the 4 most significant bits of the eNB ID  shall appear first in the string, and the character representing the 4 least significant bit  of the eNB ID (to form a nibble) shall appear last in the string.   # noqa: E501

        :param e_nb_id: The e_nb_id of this GlobalRanNodeId.
        :type e_nb_id: str
        """
        if e_nb_id is not None and not re.search(r'^(MacroeNB-[A-Fa-f0-9]{5}|LMacroeNB-[A-Fa-f0-9]{6}|SMacroeNB-[A-Fa-f0-9]{5}|HomeeNB-[A-Fa-f0-9]{7})$', e_nb_id):  # noqa: E501
            raise ValueError("Invalid value for `e_nb_id`, must be a follow pattern or equal to `/^(MacroeNB-[A-Fa-f0-9]{5}|LMacroeNB-[A-Fa-f0-9]{6}|SMacroeNB-[A-Fa-f0-9]{5}|HomeeNB-[A-Fa-f0-9]{7})$/`")  # noqa: E501

        self._e_nb_id = e_nb_id
