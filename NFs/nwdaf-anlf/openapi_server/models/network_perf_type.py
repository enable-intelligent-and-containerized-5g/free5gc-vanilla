# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.network_perf_type_any_of import NetworkPerfTypeAnyOf
from openapi_server import util

from openapi_server.models.network_perf_type_any_of import NetworkPerfTypeAnyOf  # noqa: E501

class NetworkPerfType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """NetworkPerfType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkPerfType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetworkPerfType of this NetworkPerfType.  # noqa: E501
        :rtype: NetworkPerfType
        """
        return util.deserialize_model(dikt, cls)
