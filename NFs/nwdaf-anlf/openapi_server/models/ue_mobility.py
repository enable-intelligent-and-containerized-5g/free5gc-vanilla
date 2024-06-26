# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.location_info import LocationInfo
from openapi_server.models.scheduled_communication_time import ScheduledCommunicationTime
from openapi_server import util

from openapi_server.models.location_info import LocationInfo  # noqa: E501
from openapi_server.models.scheduled_communication_time import ScheduledCommunicationTime  # noqa: E501

class UeMobility(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ts=None, recurring_time=None, duration=None, duration_variance=None, loc_infos=None):  # noqa: E501
        """UeMobility - a model defined in OpenAPI

        :param ts: The ts of this UeMobility.  # noqa: E501
        :type ts: datetime
        :param recurring_time: The recurring_time of this UeMobility.  # noqa: E501
        :type recurring_time: ScheduledCommunicationTime
        :param duration: The duration of this UeMobility.  # noqa: E501
        :type duration: int
        :param duration_variance: The duration_variance of this UeMobility.  # noqa: E501
        :type duration_variance: float
        :param loc_infos: The loc_infos of this UeMobility.  # noqa: E501
        :type loc_infos: List[LocationInfo]
        """
        self.openapi_types = {
            'ts': datetime,
            'recurring_time': ScheduledCommunicationTime,
            'duration': int,
            'duration_variance': float,
            'loc_infos': List[LocationInfo]
        }

        self.attribute_map = {
            'ts': 'ts',
            'recurring_time': 'recurringTime',
            'duration': 'duration',
            'duration_variance': 'durationVariance',
            'loc_infos': 'locInfos'
        }

        self.ts = ts
        self.recurring_time = recurring_time
        self.duration = duration
        self.duration_variance = duration_variance
        self.loc_infos = loc_infos

    @classmethod
    def from_dict(cls, dikt) -> 'UeMobility':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeMobility of this UeMobility.  # noqa: E501
        :rtype: UeMobility
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ts(self):
        """Gets the ts of this UeMobility.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The ts of this UeMobility.
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this UeMobility.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param ts: The ts of this UeMobility.
        :type ts: datetime
        """

        self._ts = ts

    @property
    def recurring_time(self):
        """Gets the recurring_time of this UeMobility.


        :return: The recurring_time of this UeMobility.
        :rtype: ScheduledCommunicationTime
        """
        return self._recurring_time

    @recurring_time.setter
    def recurring_time(self, recurring_time):
        """Sets the recurring_time of this UeMobility.


        :param recurring_time: The recurring_time of this UeMobility.
        :type recurring_time: ScheduledCommunicationTime
        """

        self._recurring_time = recurring_time

    @property
    def duration(self):
        """Gets the duration of this UeMobility.

        indicating a time in seconds.  # noqa: E501

        :return: The duration of this UeMobility.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UeMobility.

        indicating a time in seconds.  # noqa: E501

        :param duration: The duration of this UeMobility.
        :type duration: int
        """

        self._duration = duration

    @property
    def duration_variance(self):
        """Gets the duration_variance of this UeMobility.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The duration_variance of this UeMobility.
        :rtype: float
        """
        return self._duration_variance

    @duration_variance.setter
    def duration_variance(self, duration_variance):
        """Sets the duration_variance of this UeMobility.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param duration_variance: The duration_variance of this UeMobility.
        :type duration_variance: float
        """

        self._duration_variance = duration_variance

    @property
    def loc_infos(self):
        """Gets the loc_infos of this UeMobility.


        :return: The loc_infos of this UeMobility.
        :rtype: List[LocationInfo]
        """
        return self._loc_infos

    @loc_infos.setter
    def loc_infos(self, loc_infos):
        """Sets the loc_infos of this UeMobility.


        :param loc_infos: The loc_infos of this UeMobility.
        :type loc_infos: List[LocationInfo]
        """
        if loc_infos is not None and len(loc_infos) < 1:
            raise ValueError("Invalid value for `loc_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._loc_infos = loc_infos
