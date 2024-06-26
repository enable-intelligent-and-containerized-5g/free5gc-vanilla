# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RankingCriterion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, high_base=None, low_base=None):  # noqa: E501
        """RankingCriterion - a model defined in OpenAPI

        :param high_base: The high_base of this RankingCriterion.  # noqa: E501
        :type high_base: int
        :param low_base: The low_base of this RankingCriterion.  # noqa: E501
        :type low_base: int
        """
        self.openapi_types = {
            'high_base': int,
            'low_base': int
        }

        self.attribute_map = {
            'high_base': 'highBase',
            'low_base': 'lowBase'
        }

        self.high_base = high_base
        self.low_base = low_base

    @classmethod
    def from_dict(cls, dikt) -> 'RankingCriterion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RankingCriterion of this RankingCriterion.  # noqa: E501
        :rtype: RankingCriterion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def high_base(self):
        """Gets the high_base of this RankingCriterion.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :return: The high_base of this RankingCriterion.
        :rtype: int
        """
        return self._high_base

    @high_base.setter
    def high_base(self, high_base):
        """Sets the high_base of this RankingCriterion.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :param high_base: The high_base of this RankingCriterion.
        :type high_base: int
        """
        if high_base is None:
            raise ValueError("Invalid value for `high_base`, must not be `None`")  # noqa: E501
        if high_base is not None and high_base > 100:  # noqa: E501
            raise ValueError("Invalid value for `high_base`, must be a value less than or equal to `100`")  # noqa: E501
        if high_base is not None and high_base < 1:  # noqa: E501
            raise ValueError("Invalid value for `high_base`, must be a value greater than or equal to `1`")  # noqa: E501

        self._high_base = high_base

    @property
    def low_base(self):
        """Gets the low_base of this RankingCriterion.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :return: The low_base of this RankingCriterion.
        :rtype: int
        """
        return self._low_base

    @low_base.setter
    def low_base(self, low_base):
        """Sets the low_base of this RankingCriterion.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :param low_base: The low_base of this RankingCriterion.
        :type low_base: int
        """
        if low_base is None:
            raise ValueError("Invalid value for `low_base`, must not be `None`")  # noqa: E501
        if low_base is not None and low_base > 100:  # noqa: E501
            raise ValueError("Invalid value for `low_base`, must be a value less than or equal to `100`")  # noqa: E501
        if low_base is not None and low_base < 1:  # noqa: E501
            raise ValueError("Invalid value for `low_base`, must be a value greater than or equal to `1`")  # noqa: E501

        self._low_base = low_base
