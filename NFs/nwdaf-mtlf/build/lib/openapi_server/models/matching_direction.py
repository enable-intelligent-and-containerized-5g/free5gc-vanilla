# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.matching_direction_any_of import MatchingDirectionAnyOf
from openapi_server import util

from openapi_server.models.matching_direction_any_of import MatchingDirectionAnyOf  # noqa: E501

class MatchingDirection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """MatchingDirection - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'MatchingDirection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MatchingDirection of this MatchingDirection.  # noqa: E501
        :rtype: MatchingDirection
        """
        return util.deserialize_model(dikt, cls)
