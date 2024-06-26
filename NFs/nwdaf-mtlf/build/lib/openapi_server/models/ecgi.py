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

class Ecgi(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, eutra_cell_id=None, nid=None):  # noqa: E501
        """Ecgi - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this Ecgi.  # noqa: E501
        :type plmn_id: PlmnId
        :param eutra_cell_id: The eutra_cell_id of this Ecgi.  # noqa: E501
        :type eutra_cell_id: str
        :param nid: The nid of this Ecgi.  # noqa: E501
        :type nid: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'eutra_cell_id': str,
            'nid': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'eutra_cell_id': 'eutraCellId',
            'nid': 'nid'
        }

        self.plmn_id = plmn_id
        self.eutra_cell_id = eutra_cell_id
        self.nid = nid

    @classmethod
    def from_dict(cls, dikt) -> 'Ecgi':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ecgi of this Ecgi.  # noqa: E501
        :rtype: Ecgi
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this Ecgi.


        :return: The plmn_id of this Ecgi.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this Ecgi.


        :param plmn_id: The plmn_id of this Ecgi.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def eutra_cell_id(self):
        """Gets the eutra_cell_id of this Ecgi.

        28-bit string identifying an E-UTRA Cell Id as specified in clause 9.3.1.9 of  3GPP TS 38.413, in hexadecimal representation. Each character in the string shall take a  value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most  significant character representing the 4 most significant bits of the Cell Id shall appear  first in the string, and the character representing the 4 least significant bit of the  Cell Id shall appear last in the string.    # noqa: E501

        :return: The eutra_cell_id of this Ecgi.
        :rtype: str
        """
        return self._eutra_cell_id

    @eutra_cell_id.setter
    def eutra_cell_id(self, eutra_cell_id):
        """Sets the eutra_cell_id of this Ecgi.

        28-bit string identifying an E-UTRA Cell Id as specified in clause 9.3.1.9 of  3GPP TS 38.413, in hexadecimal representation. Each character in the string shall take a  value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most  significant character representing the 4 most significant bits of the Cell Id shall appear  first in the string, and the character representing the 4 least significant bit of the  Cell Id shall appear last in the string.    # noqa: E501

        :param eutra_cell_id: The eutra_cell_id of this Ecgi.
        :type eutra_cell_id: str
        """
        if eutra_cell_id is None:
            raise ValueError("Invalid value for `eutra_cell_id`, must not be `None`")  # noqa: E501
        if eutra_cell_id is not None and not re.search(r'^[A-Fa-f0-9]{7}$', eutra_cell_id):  # noqa: E501
            raise ValueError("Invalid value for `eutra_cell_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{7}$/`")  # noqa: E501

        self._eutra_cell_id = eutra_cell_id

    @property
    def nid(self):
        """Gets the nid of this Ecgi.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :return: The nid of this Ecgi.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this Ecgi.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :param nid: The nid of this Ecgi.
        :type nid: str
        """
        if nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid):  # noqa: E501
            raise ValueError("Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid
