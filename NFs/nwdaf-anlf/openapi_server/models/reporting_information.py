# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.notification_flag import NotificationFlag
from openapi_server.models.notification_method1 import NotificationMethod1
from openapi_server.models.partitioning_criteria import PartitioningCriteria
from openapi_server import util

from openapi_server.models.notification_flag import NotificationFlag  # noqa: E501
from openapi_server.models.notification_method1 import NotificationMethod1  # noqa: E501
from openapi_server.models.partitioning_criteria import PartitioningCriteria  # noqa: E501

class ReportingInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, imm_rep=None, notif_method=None, max_report_nbr=None, mon_dur=None, rep_period=None, samp_ratio=None, partition_criteria=None, grp_rep_time=None, notif_flag=None):  # noqa: E501
        """ReportingInformation - a model defined in OpenAPI

        :param imm_rep: The imm_rep of this ReportingInformation.  # noqa: E501
        :type imm_rep: bool
        :param notif_method: The notif_method of this ReportingInformation.  # noqa: E501
        :type notif_method: NotificationMethod1
        :param max_report_nbr: The max_report_nbr of this ReportingInformation.  # noqa: E501
        :type max_report_nbr: int
        :param mon_dur: The mon_dur of this ReportingInformation.  # noqa: E501
        :type mon_dur: datetime
        :param rep_period: The rep_period of this ReportingInformation.  # noqa: E501
        :type rep_period: int
        :param samp_ratio: The samp_ratio of this ReportingInformation.  # noqa: E501
        :type samp_ratio: int
        :param partition_criteria: The partition_criteria of this ReportingInformation.  # noqa: E501
        :type partition_criteria: List[PartitioningCriteria]
        :param grp_rep_time: The grp_rep_time of this ReportingInformation.  # noqa: E501
        :type grp_rep_time: int
        :param notif_flag: The notif_flag of this ReportingInformation.  # noqa: E501
        :type notif_flag: NotificationFlag
        """
        self.openapi_types = {
            'imm_rep': bool,
            'notif_method': NotificationMethod1,
            'max_report_nbr': int,
            'mon_dur': datetime,
            'rep_period': int,
            'samp_ratio': int,
            'partition_criteria': List[PartitioningCriteria],
            'grp_rep_time': int,
            'notif_flag': NotificationFlag
        }

        self.attribute_map = {
            'imm_rep': 'immRep',
            'notif_method': 'notifMethod',
            'max_report_nbr': 'maxReportNbr',
            'mon_dur': 'monDur',
            'rep_period': 'repPeriod',
            'samp_ratio': 'sampRatio',
            'partition_criteria': 'partitionCriteria',
            'grp_rep_time': 'grpRepTime',
            'notif_flag': 'notifFlag'
        }

        self.imm_rep = imm_rep
        self.notif_method = notif_method
        self.max_report_nbr = max_report_nbr
        self.mon_dur = mon_dur
        self.rep_period = rep_period
        self.samp_ratio = samp_ratio
        self.partition_criteria = partition_criteria
        self.grp_rep_time = grp_rep_time
        self.notif_flag = notif_flag

    @classmethod
    def from_dict(cls, dikt) -> 'ReportingInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportingInformation of this ReportingInformation.  # noqa: E501
        :rtype: ReportingInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def imm_rep(self):
        """Gets the imm_rep of this ReportingInformation.


        :return: The imm_rep of this ReportingInformation.
        :rtype: bool
        """
        return self._imm_rep

    @imm_rep.setter
    def imm_rep(self, imm_rep):
        """Sets the imm_rep of this ReportingInformation.


        :param imm_rep: The imm_rep of this ReportingInformation.
        :type imm_rep: bool
        """

        self._imm_rep = imm_rep

    @property
    def notif_method(self):
        """Gets the notif_method of this ReportingInformation.


        :return: The notif_method of this ReportingInformation.
        :rtype: NotificationMethod1
        """
        return self._notif_method

    @notif_method.setter
    def notif_method(self, notif_method):
        """Sets the notif_method of this ReportingInformation.


        :param notif_method: The notif_method of this ReportingInformation.
        :type notif_method: NotificationMethod1
        """

        self._notif_method = notif_method

    @property
    def max_report_nbr(self):
        """Gets the max_report_nbr of this ReportingInformation.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The max_report_nbr of this ReportingInformation.
        :rtype: int
        """
        return self._max_report_nbr

    @max_report_nbr.setter
    def max_report_nbr(self, max_report_nbr):
        """Sets the max_report_nbr of this ReportingInformation.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param max_report_nbr: The max_report_nbr of this ReportingInformation.
        :type max_report_nbr: int
        """
        if max_report_nbr is not None and max_report_nbr < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_report_nbr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_report_nbr = max_report_nbr

    @property
    def mon_dur(self):
        """Gets the mon_dur of this ReportingInformation.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The mon_dur of this ReportingInformation.
        :rtype: datetime
        """
        return self._mon_dur

    @mon_dur.setter
    def mon_dur(self, mon_dur):
        """Sets the mon_dur of this ReportingInformation.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param mon_dur: The mon_dur of this ReportingInformation.
        :type mon_dur: datetime
        """

        self._mon_dur = mon_dur

    @property
    def rep_period(self):
        """Gets the rep_period of this ReportingInformation.

        indicating a time in seconds.  # noqa: E501

        :return: The rep_period of this ReportingInformation.
        :rtype: int
        """
        return self._rep_period

    @rep_period.setter
    def rep_period(self, rep_period):
        """Sets the rep_period of this ReportingInformation.

        indicating a time in seconds.  # noqa: E501

        :param rep_period: The rep_period of this ReportingInformation.
        :type rep_period: int
        """

        self._rep_period = rep_period

    @property
    def samp_ratio(self):
        """Gets the samp_ratio of this ReportingInformation.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :return: The samp_ratio of this ReportingInformation.
        :rtype: int
        """
        return self._samp_ratio

    @samp_ratio.setter
    def samp_ratio(self, samp_ratio):
        """Sets the samp_ratio of this ReportingInformation.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :param samp_ratio: The samp_ratio of this ReportingInformation.
        :type samp_ratio: int
        """
        if samp_ratio is not None and samp_ratio > 100:  # noqa: E501
            raise ValueError("Invalid value for `samp_ratio`, must be a value less than or equal to `100`")  # noqa: E501
        if samp_ratio is not None and samp_ratio < 1:  # noqa: E501
            raise ValueError("Invalid value for `samp_ratio`, must be a value greater than or equal to `1`")  # noqa: E501

        self._samp_ratio = samp_ratio

    @property
    def partition_criteria(self):
        """Gets the partition_criteria of this ReportingInformation.

        Criteria for partitioning the UEs before applying the sampling ratio.  # noqa: E501

        :return: The partition_criteria of this ReportingInformation.
        :rtype: List[PartitioningCriteria]
        """
        return self._partition_criteria

    @partition_criteria.setter
    def partition_criteria(self, partition_criteria):
        """Sets the partition_criteria of this ReportingInformation.

        Criteria for partitioning the UEs before applying the sampling ratio.  # noqa: E501

        :param partition_criteria: The partition_criteria of this ReportingInformation.
        :type partition_criteria: List[PartitioningCriteria]
        """
        if partition_criteria is not None and len(partition_criteria) < 1:
            raise ValueError("Invalid value for `partition_criteria`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._partition_criteria = partition_criteria

    @property
    def grp_rep_time(self):
        """Gets the grp_rep_time of this ReportingInformation.

        indicating a time in seconds.  # noqa: E501

        :return: The grp_rep_time of this ReportingInformation.
        :rtype: int
        """
        return self._grp_rep_time

    @grp_rep_time.setter
    def grp_rep_time(self, grp_rep_time):
        """Sets the grp_rep_time of this ReportingInformation.

        indicating a time in seconds.  # noqa: E501

        :param grp_rep_time: The grp_rep_time of this ReportingInformation.
        :type grp_rep_time: int
        """

        self._grp_rep_time = grp_rep_time

    @property
    def notif_flag(self):
        """Gets the notif_flag of this ReportingInformation.


        :return: The notif_flag of this ReportingInformation.
        :rtype: NotificationFlag
        """
        return self._notif_flag

    @notif_flag.setter
    def notif_flag(self, notif_flag):
        """Sets the notif_flag of this ReportingInformation.


        :param notif_flag: The notif_flag of this ReportingInformation.
        :type notif_flag: NotificationFlag
        """

        self._notif_flag = notif_flag