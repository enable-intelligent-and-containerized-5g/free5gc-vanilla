# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nf_type_any_of import NFTypeAnyOf
from openapi_server import util

from openapi_server.models.nf_type_any_of import NFTypeAnyOf  # noqa: E501

class NFType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """NFType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'NFType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NFType of this NFType.  # noqa: E501
        :rtype: NFType
        """
        return util.deserialize_model(dikt, cls)
