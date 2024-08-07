# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class Tai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, tac=None, nid=None):  # noqa: E501
        """Tai - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this Tai.  # noqa: E501
        :type plmn_id: PlmnId
        :param tac: The tac of this Tai.  # noqa: E501
        :type tac: str
        :param nid: The nid of this Tai.  # noqa: E501
        :type nid: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'tac': str,
            'nid': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'tac': 'tac',
            'nid': 'nid'
        }

        self.plmn_id = plmn_id
        self.tac = tac
        self.nid = nid

    @classmethod
    def from_dict(cls, dikt) -> 'Tai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tai of this Tai.  # noqa: E501
        :rtype: Tai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this Tai.


        :return: The plmn_id of this Tai.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this Tai.


        :param plmn_id: The plmn_id of this Tai.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def tac(self):
        """Gets the tac of this Tai.

        2 or 3-octet string identifying a tracking area code as specified in clause 9.3.3.10  of 3GPP TS 38.413, in hexadecimal representation. Each character in the string shall  take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the 4 most significant bits of the TAC shall  appear first in the string, and the character representing the 4 least significant bit  of the TAC shall appear last in the string.    # noqa: E501

        :return: The tac of this Tai.
        :rtype: str
        """
        return self._tac

    @tac.setter
    def tac(self, tac):
        """Sets the tac of this Tai.

        2 or 3-octet string identifying a tracking area code as specified in clause 9.3.3.10  of 3GPP TS 38.413, in hexadecimal representation. Each character in the string shall  take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the 4 most significant bits of the TAC shall  appear first in the string, and the character representing the 4 least significant bit  of the TAC shall appear last in the string.    # noqa: E501

        :param tac: The tac of this Tai.
        :type tac: str
        """
        if tac is None:
            raise ValueError("Invalid value for `tac`, must not be `None`")  # noqa: E501
        if tac is not None and not re.search(r'(^[A-Fa-f0-9]{4}$)|(^[A-Fa-f0-9]{6}$)', tac):  # noqa: E501
            raise ValueError("Invalid value for `tac`, must be a follow pattern or equal to `/(^[A-Fa-f0-9]{4}$)|(^[A-Fa-f0-9]{6}$)/`")  # noqa: E501

        self._tac = tac

    @property
    def nid(self):
        """Gets the nid of this Tai.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :return: The nid of this Tai.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this Tai.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :param nid: The nid of this Tai.
        :type nid: str
        """
        if nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid):  # noqa: E501
            raise ValueError("Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid
