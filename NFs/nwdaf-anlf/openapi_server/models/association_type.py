# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.association_type_any_of import AssociationTypeAnyOf
from openapi_server import util

from openapi_server.models.association_type_any_of import AssociationTypeAnyOf  # noqa: E501

class AssociationType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """AssociationType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AssociationType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssociationType of this AssociationType.  # noqa: E501
        :rtype: AssociationType
        """
        return util.deserialize_model(dikt, cls)
