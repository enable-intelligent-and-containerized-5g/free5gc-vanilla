# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class TrafficInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, uplink_rate=None, downlink_rate=None, uplink_volume=None, downlink_volume=None, total_volume=None):  # noqa: E501
        """TrafficInformation - a model defined in OpenAPI

        :param uplink_rate: The uplink_rate of this TrafficInformation.  # noqa: E501
        :type uplink_rate: str
        :param downlink_rate: The downlink_rate of this TrafficInformation.  # noqa: E501
        :type downlink_rate: str
        :param uplink_volume: The uplink_volume of this TrafficInformation.  # noqa: E501
        :type uplink_volume: int
        :param downlink_volume: The downlink_volume of this TrafficInformation.  # noqa: E501
        :type downlink_volume: int
        :param total_volume: The total_volume of this TrafficInformation.  # noqa: E501
        :type total_volume: int
        """
        self.openapi_types = {
            'uplink_rate': str,
            'downlink_rate': str,
            'uplink_volume': int,
            'downlink_volume': int,
            'total_volume': int
        }

        self.attribute_map = {
            'uplink_rate': 'uplinkRate',
            'downlink_rate': 'downlinkRate',
            'uplink_volume': 'uplinkVolume',
            'downlink_volume': 'downlinkVolume',
            'total_volume': 'totalVolume'
        }

        self.uplink_rate = uplink_rate
        self.downlink_rate = downlink_rate
        self.uplink_volume = uplink_volume
        self.downlink_volume = downlink_volume
        self.total_volume = total_volume

    @classmethod
    def from_dict(cls, dikt) -> 'TrafficInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrafficInformation of this TrafficInformation.  # noqa: E501
        :rtype: TrafficInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uplink_rate(self):
        """Gets the uplink_rate of this TrafficInformation.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The uplink_rate of this TrafficInformation.
        :rtype: str
        """
        return self._uplink_rate

    @uplink_rate.setter
    def uplink_rate(self, uplink_rate):
        """Sets the uplink_rate of this TrafficInformation.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param uplink_rate: The uplink_rate of this TrafficInformation.
        :type uplink_rate: str
        """
        if uplink_rate is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', uplink_rate):  # noqa: E501
            raise ValueError("Invalid value for `uplink_rate`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._uplink_rate = uplink_rate

    @property
    def downlink_rate(self):
        """Gets the downlink_rate of this TrafficInformation.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The downlink_rate of this TrafficInformation.
        :rtype: str
        """
        return self._downlink_rate

    @downlink_rate.setter
    def downlink_rate(self, downlink_rate):
        """Sets the downlink_rate of this TrafficInformation.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param downlink_rate: The downlink_rate of this TrafficInformation.
        :type downlink_rate: str
        """
        if downlink_rate is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', downlink_rate):  # noqa: E501
            raise ValueError("Invalid value for `downlink_rate`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._downlink_rate = downlink_rate

    @property
    def uplink_volume(self):
        """Gets the uplink_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :return: The uplink_volume of this TrafficInformation.
        :rtype: int
        """
        return self._uplink_volume

    @uplink_volume.setter
    def uplink_volume(self, uplink_volume):
        """Sets the uplink_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :param uplink_volume: The uplink_volume of this TrafficInformation.
        :type uplink_volume: int
        """
        if uplink_volume is not None and uplink_volume < 0:  # noqa: E501
            raise ValueError("Invalid value for `uplink_volume`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uplink_volume = uplink_volume

    @property
    def downlink_volume(self):
        """Gets the downlink_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :return: The downlink_volume of this TrafficInformation.
        :rtype: int
        """
        return self._downlink_volume

    @downlink_volume.setter
    def downlink_volume(self, downlink_volume):
        """Sets the downlink_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :param downlink_volume: The downlink_volume of this TrafficInformation.
        :type downlink_volume: int
        """
        if downlink_volume is not None and downlink_volume < 0:  # noqa: E501
            raise ValueError("Invalid value for `downlink_volume`, must be a value greater than or equal to `0`")  # noqa: E501

        self._downlink_volume = downlink_volume

    @property
    def total_volume(self):
        """Gets the total_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :return: The total_volume of this TrafficInformation.
        :rtype: int
        """
        return self._total_volume

    @total_volume.setter
    def total_volume(self, total_volume):
        """Sets the total_volume of this TrafficInformation.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :param total_volume: The total_volume of this TrafficInformation.
        :type total_volume: int
        """
        if total_volume is not None and total_volume < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_volume`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_volume = total_volume
