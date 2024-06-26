# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SmNasFromUe(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sm_nas_type=None, time_stamp=None):  # noqa: E501
        """SmNasFromUe - a model defined in OpenAPI

        :param sm_nas_type: The sm_nas_type of this SmNasFromUe.  # noqa: E501
        :type sm_nas_type: str
        :param time_stamp: The time_stamp of this SmNasFromUe.  # noqa: E501
        :type time_stamp: datetime
        """
        self.openapi_types = {
            'sm_nas_type': str,
            'time_stamp': datetime
        }

        self.attribute_map = {
            'sm_nas_type': 'smNasType',
            'time_stamp': 'timeStamp'
        }

        self.sm_nas_type = sm_nas_type
        self.time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'SmNasFromUe':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmNasFromUe of this SmNasFromUe.  # noqa: E501
        :rtype: SmNasFromUe
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sm_nas_type(self):
        """Gets the sm_nas_type of this SmNasFromUe.


        :return: The sm_nas_type of this SmNasFromUe.
        :rtype: str
        """
        return self._sm_nas_type

    @sm_nas_type.setter
    def sm_nas_type(self, sm_nas_type):
        """Sets the sm_nas_type of this SmNasFromUe.


        :param sm_nas_type: The sm_nas_type of this SmNasFromUe.
        :type sm_nas_type: str
        """
        if sm_nas_type is None:
            raise ValueError("Invalid value for `sm_nas_type`, must not be `None`")  # noqa: E501

        self._sm_nas_type = sm_nas_type

    @property
    def time_stamp(self):
        """Gets the time_stamp of this SmNasFromUe.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The time_stamp of this SmNasFromUe.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this SmNasFromUe.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param time_stamp: The time_stamp of this SmNasFromUe.
        :type time_stamp: datetime
        """
        if time_stamp is None:
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        self._time_stamp = time_stamp
