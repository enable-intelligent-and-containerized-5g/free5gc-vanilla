# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.amf_event_trigger_any_of import AmfEventTriggerAnyOf
from openapi_server import util

from openapi_server.models.amf_event_trigger_any_of import AmfEventTriggerAnyOf  # noqa: E501

class AmfEventTrigger(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """AmfEventTrigger - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AmfEventTrigger':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfEventTrigger of this AmfEventTrigger.  # noqa: E501
        :rtype: AmfEventTrigger
        """
        return util.deserialize_model(dikt, cls)
