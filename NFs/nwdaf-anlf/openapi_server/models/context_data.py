# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.context_element import ContextElement
from openapi_server import util

from openapi_server.models.context_element import ContextElement  # noqa: E501

class ContextData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, context_elems=None):  # noqa: E501
        """ContextData - a model defined in OpenAPI

        :param context_elems: The context_elems of this ContextData.  # noqa: E501
        :type context_elems: List[ContextElement]
        """
        self.openapi_types = {
            'context_elems': List[ContextElement]
        }

        self.attribute_map = {
            'context_elems': 'contextElems'
        }

        self.context_elems = context_elems

    @classmethod
    def from_dict(cls, dikt) -> 'ContextData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ContextData of this ContextData.  # noqa: E501
        :rtype: ContextData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context_elems(self):
        """Gets the context_elems of this ContextData.

        List of items that contain context information corresponding with a context identifier.   # noqa: E501

        :return: The context_elems of this ContextData.
        :rtype: List[ContextElement]
        """
        return self._context_elems

    @context_elems.setter
    def context_elems(self, context_elems):
        """Sets the context_elems of this ContextData.

        List of items that contain context information corresponding with a context identifier.   # noqa: E501

        :param context_elems: The context_elems of this ContextData.
        :type context_elems: List[ContextElement]
        """
        if context_elems is None:
            raise ValueError("Invalid value for `context_elems`, must not be `None`")  # noqa: E501
        if context_elems is not None and len(context_elems) < 1:
            raise ValueError("Invalid value for `context_elems`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._context_elems = context_elems
