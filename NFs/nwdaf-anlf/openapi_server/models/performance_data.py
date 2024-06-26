# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class PerformanceData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pdb=None, plr=None, thrput_ul=None, thrput_dl=None):  # noqa: E501
        """PerformanceData - a model defined in OpenAPI

        :param pdb: The pdb of this PerformanceData.  # noqa: E501
        :type pdb: int
        :param plr: The plr of this PerformanceData.  # noqa: E501
        :type plr: int
        :param thrput_ul: The thrput_ul of this PerformanceData.  # noqa: E501
        :type thrput_ul: str
        :param thrput_dl: The thrput_dl of this PerformanceData.  # noqa: E501
        :type thrput_dl: str
        """
        self.openapi_types = {
            'pdb': int,
            'plr': int,
            'thrput_ul': str,
            'thrput_dl': str
        }

        self.attribute_map = {
            'pdb': 'pdb',
            'plr': 'plr',
            'thrput_ul': 'thrputUl',
            'thrput_dl': 'thrputDl'
        }

        self.pdb = pdb
        self.plr = plr
        self.thrput_ul = thrput_ul
        self.thrput_dl = thrput_dl

    @classmethod
    def from_dict(cls, dikt) -> 'PerformanceData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PerformanceData of this PerformanceData.  # noqa: E501
        :rtype: PerformanceData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pdb(self):
        """Gets the pdb of this PerformanceData.

        Unsigned integer indicating Packet Delay Budget (see clauses 5.7.3.4 and 5.7.4 of 3GPP TS 23.501), expressed in milliseconds.   # noqa: E501

        :return: The pdb of this PerformanceData.
        :rtype: int
        """
        return self._pdb

    @pdb.setter
    def pdb(self, pdb):
        """Sets the pdb of this PerformanceData.

        Unsigned integer indicating Packet Delay Budget (see clauses 5.7.3.4 and 5.7.4 of 3GPP TS 23.501), expressed in milliseconds.   # noqa: E501

        :param pdb: The pdb of this PerformanceData.
        :type pdb: int
        """
        if pdb is not None and pdb < 1:  # noqa: E501
            raise ValueError("Invalid value for `pdb`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pdb = pdb

    @property
    def plr(self):
        """Gets the plr of this PerformanceData.

        Unsigned integer indicating Packet Loss Rate (see clauses 5.7.2.8 and 5.7.4 of 3GPP TS 23.501), expressed in tenth of percent.   # noqa: E501

        :return: The plr of this PerformanceData.
        :rtype: int
        """
        return self._plr

    @plr.setter
    def plr(self, plr):
        """Sets the plr of this PerformanceData.

        Unsigned integer indicating Packet Loss Rate (see clauses 5.7.2.8 and 5.7.4 of 3GPP TS 23.501), expressed in tenth of percent.   # noqa: E501

        :param plr: The plr of this PerformanceData.
        :type plr: int
        """
        if plr is not None and plr > 1000:  # noqa: E501
            raise ValueError("Invalid value for `plr`, must be a value less than or equal to `1000`")  # noqa: E501
        if plr is not None and plr < 0:  # noqa: E501
            raise ValueError("Invalid value for `plr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._plr = plr

    @property
    def thrput_ul(self):
        """Gets the thrput_ul of this PerformanceData.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_ul of this PerformanceData.
        :rtype: str
        """
        return self._thrput_ul

    @thrput_ul.setter
    def thrput_ul(self, thrput_ul):
        """Sets the thrput_ul of this PerformanceData.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_ul: The thrput_ul of this PerformanceData.
        :type thrput_ul: str
        """
        if thrput_ul is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_ul):  # noqa: E501
            raise ValueError("Invalid value for `thrput_ul`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_ul = thrput_ul

    @property
    def thrput_dl(self):
        """Gets the thrput_dl of this PerformanceData.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_dl of this PerformanceData.
        :rtype: str
        """
        return self._thrput_dl

    @thrput_dl.setter
    def thrput_dl(self, thrput_dl):
        """Sets the thrput_dl of this PerformanceData.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_dl: The thrput_dl of this PerformanceData.
        :type thrput_dl: str
        """
        if thrput_dl is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_dl):  # noqa: E501
            raise ValueError("Invalid value for `thrput_dl`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_dl = thrput_dl
