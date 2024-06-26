# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SvcExperience(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mos=None, upper_range=None, lower_range=None):  # noqa: E501
        """SvcExperience - a model defined in OpenAPI

        :param mos: The mos of this SvcExperience.  # noqa: E501
        :type mos: float
        :param upper_range: The upper_range of this SvcExperience.  # noqa: E501
        :type upper_range: float
        :param lower_range: The lower_range of this SvcExperience.  # noqa: E501
        :type lower_range: float
        """
        self.openapi_types = {
            'mos': float,
            'upper_range': float,
            'lower_range': float
        }

        self.attribute_map = {
            'mos': 'mos',
            'upper_range': 'upperRange',
            'lower_range': 'lowerRange'
        }

        self.mos = mos
        self.upper_range = upper_range
        self.lower_range = lower_range

    @classmethod
    def from_dict(cls, dikt) -> 'SvcExperience':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SvcExperience of this SvcExperience.  # noqa: E501
        :rtype: SvcExperience
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mos(self):
        """Gets the mos of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The mos of this SvcExperience.
        :rtype: float
        """
        return self._mos

    @mos.setter
    def mos(self, mos):
        """Sets the mos of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param mos: The mos of this SvcExperience.
        :type mos: float
        """

        self._mos = mos

    @property
    def upper_range(self):
        """Gets the upper_range of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The upper_range of this SvcExperience.
        :rtype: float
        """
        return self._upper_range

    @upper_range.setter
    def upper_range(self, upper_range):
        """Sets the upper_range of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param upper_range: The upper_range of this SvcExperience.
        :type upper_range: float
        """

        self._upper_range = upper_range

    @property
    def lower_range(self):
        """Gets the lower_range of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The lower_range of this SvcExperience.
        :rtype: float
        """
        return self._lower_range

    @lower_range.setter
    def lower_range(self, lower_range):
        """Sets the lower_range of this SvcExperience.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param lower_range: The lower_range of this SvcExperience.
        :type lower_range: float
        """

        self._lower_range = lower_range
