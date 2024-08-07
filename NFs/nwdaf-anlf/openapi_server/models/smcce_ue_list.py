# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SmcceUeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, high_level=None, medium_level=None, low_level=None):  # noqa: E501
        """SmcceUeList - a model defined in OpenAPI

        :param high_level: The high_level of this SmcceUeList.  # noqa: E501
        :type high_level: List[str]
        :param medium_level: The medium_level of this SmcceUeList.  # noqa: E501
        :type medium_level: List[str]
        :param low_level: The low_level of this SmcceUeList.  # noqa: E501
        :type low_level: List[str]
        """
        self.openapi_types = {
            'high_level': List[str],
            'medium_level': List[str],
            'low_level': List[str]
        }

        self.attribute_map = {
            'high_level': 'highLevel',
            'medium_level': 'mediumLevel',
            'low_level': 'lowLevel'
        }

        self.high_level = high_level
        self.medium_level = medium_level
        self.low_level = low_level

    @classmethod
    def from_dict(cls, dikt) -> 'SmcceUeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmcceUeList of this SmcceUeList.  # noqa: E501
        :rtype: SmcceUeList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def high_level(self):
        """Gets the high_level of this SmcceUeList.


        :return: The high_level of this SmcceUeList.
        :rtype: List[str]
        """
        return self._high_level

    @high_level.setter
    def high_level(self, high_level):
        """Sets the high_level of this SmcceUeList.


        :param high_level: The high_level of this SmcceUeList.
        :type high_level: List[str]
        """
        if high_level is not None and len(high_level) < 1:
            raise ValueError("Invalid value for `high_level`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._high_level = high_level

    @property
    def medium_level(self):
        """Gets the medium_level of this SmcceUeList.


        :return: The medium_level of this SmcceUeList.
        :rtype: List[str]
        """
        return self._medium_level

    @medium_level.setter
    def medium_level(self, medium_level):
        """Sets the medium_level of this SmcceUeList.


        :param medium_level: The medium_level of this SmcceUeList.
        :type medium_level: List[str]
        """
        if medium_level is not None and len(medium_level) < 1:
            raise ValueError("Invalid value for `medium_level`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._medium_level = medium_level

    @property
    def low_level(self):
        """Gets the low_level of this SmcceUeList.


        :return: The low_level of this SmcceUeList.
        :rtype: List[str]
        """
        return self._low_level

    @low_level.setter
    def low_level(self, low_level):
        """Sets the low_level of this SmcceUeList.


        :param low_level: The low_level of this SmcceUeList.
        :type low_level: List[str]
        """
        if low_level is not None and len(low_level) < 1:
            raise ValueError("Invalid value for `low_level`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._low_level = low_level
