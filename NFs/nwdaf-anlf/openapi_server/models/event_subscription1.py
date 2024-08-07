# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ddd_traffic_descriptor import DddTrafficDescriptor
from openapi_server.models.dl_data_delivery_status import DlDataDeliveryStatus
from openapi_server.models.dnai_change_type import DnaiChangeType
from openapi_server.models.ip_addr import IpAddr
from openapi_server.models.smf_event import SmfEvent
from openapi_server.models.time_window import TimeWindow
from openapi_server.models.transaction_metric import TransactionMetric
from openapi_server import util

from openapi_server.models.ddd_traffic_descriptor import DddTrafficDescriptor  # noqa: E501
from openapi_server.models.dl_data_delivery_status import DlDataDeliveryStatus  # noqa: E501
from openapi_server.models.dnai_change_type import DnaiChangeType  # noqa: E501
from openapi_server.models.ip_addr import IpAddr  # noqa: E501
from openapi_server.models.smf_event import SmfEvent  # noqa: E501
from openapi_server.models.time_window import TimeWindow  # noqa: E501
from openapi_server.models.transaction_metric import TransactionMetric  # noqa: E501

class EventSubscription1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, dnai_chg_type=None, ddd_tra_descriptors=None, ddd_stati=None, app_ids=None, target_period=None, transac_disp_ind=None, transac_metrics=None, ue_ip_addr=None):  # noqa: E501
        """EventSubscription1 - a model defined in OpenAPI

        :param event: The event of this EventSubscription1.  # noqa: E501
        :type event: SmfEvent
        :param dnai_chg_type: The dnai_chg_type of this EventSubscription1.  # noqa: E501
        :type dnai_chg_type: DnaiChangeType
        :param ddd_tra_descriptors: The ddd_tra_descriptors of this EventSubscription1.  # noqa: E501
        :type ddd_tra_descriptors: List[DddTrafficDescriptor]
        :param ddd_stati: The ddd_stati of this EventSubscription1.  # noqa: E501
        :type ddd_stati: List[DlDataDeliveryStatus]
        :param app_ids: The app_ids of this EventSubscription1.  # noqa: E501
        :type app_ids: List[str]
        :param target_period: The target_period of this EventSubscription1.  # noqa: E501
        :type target_period: TimeWindow
        :param transac_disp_ind: The transac_disp_ind of this EventSubscription1.  # noqa: E501
        :type transac_disp_ind: bool
        :param transac_metrics: The transac_metrics of this EventSubscription1.  # noqa: E501
        :type transac_metrics: List[TransactionMetric]
        :param ue_ip_addr: The ue_ip_addr of this EventSubscription1.  # noqa: E501
        :type ue_ip_addr: IpAddr
        """
        self.openapi_types = {
            'event': SmfEvent,
            'dnai_chg_type': DnaiChangeType,
            'ddd_tra_descriptors': List[DddTrafficDescriptor],
            'ddd_stati': List[DlDataDeliveryStatus],
            'app_ids': List[str],
            'target_period': TimeWindow,
            'transac_disp_ind': bool,
            'transac_metrics': List[TransactionMetric],
            'ue_ip_addr': IpAddr
        }

        self.attribute_map = {
            'event': 'event',
            'dnai_chg_type': 'dnaiChgType',
            'ddd_tra_descriptors': 'dddTraDescriptors',
            'ddd_stati': 'dddStati',
            'app_ids': 'appIds',
            'target_period': 'targetPeriod',
            'transac_disp_ind': 'transacDispInd',
            'transac_metrics': 'transacMetrics',
            'ue_ip_addr': 'ueIpAddr'
        }

        self.event = event
        self.dnai_chg_type = dnai_chg_type
        self.ddd_tra_descriptors = ddd_tra_descriptors
        self.ddd_stati = ddd_stati
        self.app_ids = app_ids
        self.target_period = target_period
        self.transac_disp_ind = transac_disp_ind
        self.transac_metrics = transac_metrics
        self.ue_ip_addr = ue_ip_addr

    @classmethod
    def from_dict(cls, dikt) -> 'EventSubscription1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventSubscription_1 of this EventSubscription1.  # noqa: E501
        :rtype: EventSubscription1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self):
        """Gets the event of this EventSubscription1.


        :return: The event of this EventSubscription1.
        :rtype: SmfEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this EventSubscription1.


        :param event: The event of this EventSubscription1.
        :type event: SmfEvent
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def dnai_chg_type(self):
        """Gets the dnai_chg_type of this EventSubscription1.


        :return: The dnai_chg_type of this EventSubscription1.
        :rtype: DnaiChangeType
        """
        return self._dnai_chg_type

    @dnai_chg_type.setter
    def dnai_chg_type(self, dnai_chg_type):
        """Sets the dnai_chg_type of this EventSubscription1.


        :param dnai_chg_type: The dnai_chg_type of this EventSubscription1.
        :type dnai_chg_type: DnaiChangeType
        """

        self._dnai_chg_type = dnai_chg_type

    @property
    def ddd_tra_descriptors(self):
        """Gets the ddd_tra_descriptors of this EventSubscription1.


        :return: The ddd_tra_descriptors of this EventSubscription1.
        :rtype: List[DddTrafficDescriptor]
        """
        return self._ddd_tra_descriptors

    @ddd_tra_descriptors.setter
    def ddd_tra_descriptors(self, ddd_tra_descriptors):
        """Sets the ddd_tra_descriptors of this EventSubscription1.


        :param ddd_tra_descriptors: The ddd_tra_descriptors of this EventSubscription1.
        :type ddd_tra_descriptors: List[DddTrafficDescriptor]
        """
        if ddd_tra_descriptors is not None and len(ddd_tra_descriptors) < 1:
            raise ValueError("Invalid value for `ddd_tra_descriptors`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ddd_tra_descriptors = ddd_tra_descriptors

    @property
    def ddd_stati(self):
        """Gets the ddd_stati of this EventSubscription1.


        :return: The ddd_stati of this EventSubscription1.
        :rtype: List[DlDataDeliveryStatus]
        """
        return self._ddd_stati

    @ddd_stati.setter
    def ddd_stati(self, ddd_stati):
        """Sets the ddd_stati of this EventSubscription1.


        :param ddd_stati: The ddd_stati of this EventSubscription1.
        :type ddd_stati: List[DlDataDeliveryStatus]
        """
        if ddd_stati is not None and len(ddd_stati) < 1:
            raise ValueError("Invalid value for `ddd_stati`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ddd_stati = ddd_stati

    @property
    def app_ids(self):
        """Gets the app_ids of this EventSubscription1.


        :return: The app_ids of this EventSubscription1.
        :rtype: List[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this EventSubscription1.


        :param app_ids: The app_ids of this EventSubscription1.
        :type app_ids: List[str]
        """
        if app_ids is not None and len(app_ids) < 1:
            raise ValueError("Invalid value for `app_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._app_ids = app_ids

    @property
    def target_period(self):
        """Gets the target_period of this EventSubscription1.


        :return: The target_period of this EventSubscription1.
        :rtype: TimeWindow
        """
        return self._target_period

    @target_period.setter
    def target_period(self, target_period):
        """Sets the target_period of this EventSubscription1.


        :param target_period: The target_period of this EventSubscription1.
        :type target_period: TimeWindow
        """

        self._target_period = target_period

    @property
    def transac_disp_ind(self):
        """Gets the transac_disp_ind of this EventSubscription1.

        Indicates the subscription for UE transaction dispersion collectionon, if it is included and set to \"true\". Default value is \"false\".   # noqa: E501

        :return: The transac_disp_ind of this EventSubscription1.
        :rtype: bool
        """
        return self._transac_disp_ind

    @transac_disp_ind.setter
    def transac_disp_ind(self, transac_disp_ind):
        """Sets the transac_disp_ind of this EventSubscription1.

        Indicates the subscription for UE transaction dispersion collectionon, if it is included and set to \"true\". Default value is \"false\".   # noqa: E501

        :param transac_disp_ind: The transac_disp_ind of this EventSubscription1.
        :type transac_disp_ind: bool
        """

        self._transac_disp_ind = transac_disp_ind

    @property
    def transac_metrics(self):
        """Gets the transac_metrics of this EventSubscription1.

        Indicates Session Management Transaction metrics.  # noqa: E501

        :return: The transac_metrics of this EventSubscription1.
        :rtype: List[TransactionMetric]
        """
        return self._transac_metrics

    @transac_metrics.setter
    def transac_metrics(self, transac_metrics):
        """Sets the transac_metrics of this EventSubscription1.

        Indicates Session Management Transaction metrics.  # noqa: E501

        :param transac_metrics: The transac_metrics of this EventSubscription1.
        :type transac_metrics: List[TransactionMetric]
        """
        if transac_metrics is not None and len(transac_metrics) < 1:
            raise ValueError("Invalid value for `transac_metrics`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._transac_metrics = transac_metrics

    @property
    def ue_ip_addr(self):
        """Gets the ue_ip_addr of this EventSubscription1.


        :return: The ue_ip_addr of this EventSubscription1.
        :rtype: IpAddr
        """
        return self._ue_ip_addr

    @ue_ip_addr.setter
    def ue_ip_addr(self, ue_ip_addr):
        """Sets the ue_ip_addr of this EventSubscription1.


        :param ue_ip_addr: The ue_ip_addr of this EventSubscription1.
        :type ue_ip_addr: IpAddr
        """

        self._ue_ip_addr = ue_ip_addr
