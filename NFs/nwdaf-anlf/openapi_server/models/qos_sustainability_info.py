# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.network_area_info import NetworkAreaInfo
from openapi_server.models.retainability_threshold import RetainabilityThreshold
from openapi_server.models.snssai import Snssai
import re
from openapi_server import util

from openapi_server.models.network_area_info import NetworkAreaInfo  # noqa: E501
from openapi_server.models.retainability_threshold import RetainabilityThreshold  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501
import re  # noqa: E501

class QosSustainabilityInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_info=None, start_ts=None, end_ts=None, qos_flow_ret_thd=None, ran_ue_throu_thd=None, snssai=None, confidence=None):  # noqa: E501
        """QosSustainabilityInfo - a model defined in OpenAPI

        :param area_info: The area_info of this QosSustainabilityInfo.  # noqa: E501
        :type area_info: NetworkAreaInfo
        :param start_ts: The start_ts of this QosSustainabilityInfo.  # noqa: E501
        :type start_ts: datetime
        :param end_ts: The end_ts of this QosSustainabilityInfo.  # noqa: E501
        :type end_ts: datetime
        :param qos_flow_ret_thd: The qos_flow_ret_thd of this QosSustainabilityInfo.  # noqa: E501
        :type qos_flow_ret_thd: RetainabilityThreshold
        :param ran_ue_throu_thd: The ran_ue_throu_thd of this QosSustainabilityInfo.  # noqa: E501
        :type ran_ue_throu_thd: str
        :param snssai: The snssai of this QosSustainabilityInfo.  # noqa: E501
        :type snssai: Snssai
        :param confidence: The confidence of this QosSustainabilityInfo.  # noqa: E501
        :type confidence: int
        """
        self.openapi_types = {
            'area_info': NetworkAreaInfo,
            'start_ts': datetime,
            'end_ts': datetime,
            'qos_flow_ret_thd': RetainabilityThreshold,
            'ran_ue_throu_thd': str,
            'snssai': Snssai,
            'confidence': int
        }

        self.attribute_map = {
            'area_info': 'areaInfo',
            'start_ts': 'startTs',
            'end_ts': 'endTs',
            'qos_flow_ret_thd': 'qosFlowRetThd',
            'ran_ue_throu_thd': 'ranUeThrouThd',
            'snssai': 'snssai',
            'confidence': 'confidence'
        }

        self.area_info = area_info
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.qos_flow_ret_thd = qos_flow_ret_thd
        self.ran_ue_throu_thd = ran_ue_throu_thd
        self.snssai = snssai
        self.confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'QosSustainabilityInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QosSustainabilityInfo of this QosSustainabilityInfo.  # noqa: E501
        :rtype: QosSustainabilityInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_info(self):
        """Gets the area_info of this QosSustainabilityInfo.


        :return: The area_info of this QosSustainabilityInfo.
        :rtype: NetworkAreaInfo
        """
        return self._area_info

    @area_info.setter
    def area_info(self, area_info):
        """Sets the area_info of this QosSustainabilityInfo.


        :param area_info: The area_info of this QosSustainabilityInfo.
        :type area_info: NetworkAreaInfo
        """

        self._area_info = area_info

    @property
    def start_ts(self):
        """Gets the start_ts of this QosSustainabilityInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The start_ts of this QosSustainabilityInfo.
        :rtype: datetime
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this QosSustainabilityInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param start_ts: The start_ts of this QosSustainabilityInfo.
        :type start_ts: datetime
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this QosSustainabilityInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The end_ts of this QosSustainabilityInfo.
        :rtype: datetime
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this QosSustainabilityInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param end_ts: The end_ts of this QosSustainabilityInfo.
        :type end_ts: datetime
        """

        self._end_ts = end_ts

    @property
    def qos_flow_ret_thd(self):
        """Gets the qos_flow_ret_thd of this QosSustainabilityInfo.


        :return: The qos_flow_ret_thd of this QosSustainabilityInfo.
        :rtype: RetainabilityThreshold
        """
        return self._qos_flow_ret_thd

    @qos_flow_ret_thd.setter
    def qos_flow_ret_thd(self, qos_flow_ret_thd):
        """Sets the qos_flow_ret_thd of this QosSustainabilityInfo.


        :param qos_flow_ret_thd: The qos_flow_ret_thd of this QosSustainabilityInfo.
        :type qos_flow_ret_thd: RetainabilityThreshold
        """

        self._qos_flow_ret_thd = qos_flow_ret_thd

    @property
    def ran_ue_throu_thd(self):
        """Gets the ran_ue_throu_thd of this QosSustainabilityInfo.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The ran_ue_throu_thd of this QosSustainabilityInfo.
        :rtype: str
        """
        return self._ran_ue_throu_thd

    @ran_ue_throu_thd.setter
    def ran_ue_throu_thd(self, ran_ue_throu_thd):
        """Sets the ran_ue_throu_thd of this QosSustainabilityInfo.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param ran_ue_throu_thd: The ran_ue_throu_thd of this QosSustainabilityInfo.
        :type ran_ue_throu_thd: str
        """
        if ran_ue_throu_thd is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', ran_ue_throu_thd):  # noqa: E501
            raise ValueError("Invalid value for `ran_ue_throu_thd`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._ran_ue_throu_thd = ran_ue_throu_thd

    @property
    def snssai(self):
        """Gets the snssai of this QosSustainabilityInfo.


        :return: The snssai of this QosSustainabilityInfo.
        :rtype: Snssai
        """
        return self._snssai

    @snssai.setter
    def snssai(self, snssai):
        """Sets the snssai of this QosSustainabilityInfo.


        :param snssai: The snssai of this QosSustainabilityInfo.
        :type snssai: Snssai
        """

        self._snssai = snssai

    @property
    def confidence(self):
        """Gets the confidence of this QosSustainabilityInfo.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The confidence of this QosSustainabilityInfo.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this QosSustainabilityInfo.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param confidence: The confidence of this QosSustainabilityInfo.
        :type confidence: int
        """
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence
