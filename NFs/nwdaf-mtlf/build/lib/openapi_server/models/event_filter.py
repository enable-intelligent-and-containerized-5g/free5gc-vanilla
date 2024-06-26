# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.addr_fqdn import AddrFqdn
from openapi_server.models.analytics_subset import AnalyticsSubset
from openapi_server.models.bw_requirement import BwRequirement
from openapi_server.models.dispersion_requirement import DispersionRequirement
from openapi_server.models.dn_performance_req import DnPerformanceReq
from openapi_server.models.exception_id import ExceptionId
from openapi_server.models.expected_analytics_type import ExpectedAnalyticsType
from openapi_server.models.expected_ue_behaviour_data import ExpectedUeBehaviourData
from openapi_server.models.nf_type import NFType
from openapi_server.models.network_area_info import NetworkAreaInfo
from openapi_server.models.network_perf_type import NetworkPerfType
from openapi_server.models.nsi_id_info import NsiIdInfo
from openapi_server.models.qos_requirement import QosRequirement
from openapi_server.models.rat_freq_information import RatFreqInformation
from openapi_server.models.redundant_transmission_exp_req import RedundantTransmissionExpReq
from openapi_server.models.snssai import Snssai
from openapi_server.models.wlan_performance_req import WlanPerformanceReq
from openapi_server import util

from openapi_server.models.addr_fqdn import AddrFqdn  # noqa: E501
from openapi_server.models.analytics_subset import AnalyticsSubset  # noqa: E501
from openapi_server.models.bw_requirement import BwRequirement  # noqa: E501
from openapi_server.models.dispersion_requirement import DispersionRequirement  # noqa: E501
from openapi_server.models.dn_performance_req import DnPerformanceReq  # noqa: E501
from openapi_server.models.exception_id import ExceptionId  # noqa: E501
from openapi_server.models.expected_analytics_type import ExpectedAnalyticsType  # noqa: E501
from openapi_server.models.expected_ue_behaviour_data import ExpectedUeBehaviourData  # noqa: E501
from openapi_server.models.network_area_info import NetworkAreaInfo  # noqa: E501
from openapi_server.models.network_perf_type import NetworkPerfType  # noqa: E501
from openapi_server.models.nf_type import NFType  # noqa: E501
from openapi_server.models.nsi_id_info import NsiIdInfo  # noqa: E501
from openapi_server.models.qos_requirement import QosRequirement  # noqa: E501
from openapi_server.models.rat_freq_information import RatFreqInformation  # noqa: E501
from openapi_server.models.redundant_transmission_exp_req import RedundantTransmissionExpReq  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501
from openapi_server.models.wlan_performance_req import WlanPerformanceReq  # noqa: E501

class EventFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, any_slice=None, snssais=None, app_ids=None, dnns=None, dnais=None, ladn_dnns=None, network_area=None, visited_areas=None, max_top_app_ul_nbr=None, max_top_app_dl_nbr=None, nf_instance_ids=None, nf_set_ids=None, nf_types=None, nsi_id_infos=None, qos_requ=None, nw_perf_types=None, bw_requs=None, excep_ids=None, expt_ana_type=None, expt_ue_behav=None, rat_freqs=None, disper_reqs=None, red_trans_reqs=None, wlan_reqs=None, list_of_ana_subsets=None, upf_id=None, app_server_addrs=None, dn_perf_reqs=None):  # noqa: E501
        """EventFilter - a model defined in OpenAPI

        :param any_slice: The any_slice of this EventFilter.  # noqa: E501
        :type any_slice: bool
        :param snssais: The snssais of this EventFilter.  # noqa: E501
        :type snssais: List[Snssai]
        :param app_ids: The app_ids of this EventFilter.  # noqa: E501
        :type app_ids: List[str]
        :param dnns: The dnns of this EventFilter.  # noqa: E501
        :type dnns: List[str]
        :param dnais: The dnais of this EventFilter.  # noqa: E501
        :type dnais: List[str]
        :param ladn_dnns: The ladn_dnns of this EventFilter.  # noqa: E501
        :type ladn_dnns: List[str]
        :param network_area: The network_area of this EventFilter.  # noqa: E501
        :type network_area: NetworkAreaInfo
        :param visited_areas: The visited_areas of this EventFilter.  # noqa: E501
        :type visited_areas: List[NetworkAreaInfo]
        :param max_top_app_ul_nbr: The max_top_app_ul_nbr of this EventFilter.  # noqa: E501
        :type max_top_app_ul_nbr: int
        :param max_top_app_dl_nbr: The max_top_app_dl_nbr of this EventFilter.  # noqa: E501
        :type max_top_app_dl_nbr: int
        :param nf_instance_ids: The nf_instance_ids of this EventFilter.  # noqa: E501
        :type nf_instance_ids: List[str]
        :param nf_set_ids: The nf_set_ids of this EventFilter.  # noqa: E501
        :type nf_set_ids: List[str]
        :param nf_types: The nf_types of this EventFilter.  # noqa: E501
        :type nf_types: List[NFType]
        :param nsi_id_infos: The nsi_id_infos of this EventFilter.  # noqa: E501
        :type nsi_id_infos: List[NsiIdInfo]
        :param qos_requ: The qos_requ of this EventFilter.  # noqa: E501
        :type qos_requ: QosRequirement
        :param nw_perf_types: The nw_perf_types of this EventFilter.  # noqa: E501
        :type nw_perf_types: List[NetworkPerfType]
        :param bw_requs: The bw_requs of this EventFilter.  # noqa: E501
        :type bw_requs: List[BwRequirement]
        :param excep_ids: The excep_ids of this EventFilter.  # noqa: E501
        :type excep_ids: List[ExceptionId]
        :param expt_ana_type: The expt_ana_type of this EventFilter.  # noqa: E501
        :type expt_ana_type: ExpectedAnalyticsType
        :param expt_ue_behav: The expt_ue_behav of this EventFilter.  # noqa: E501
        :type expt_ue_behav: ExpectedUeBehaviourData
        :param rat_freqs: The rat_freqs of this EventFilter.  # noqa: E501
        :type rat_freqs: List[RatFreqInformation]
        :param disper_reqs: The disper_reqs of this EventFilter.  # noqa: E501
        :type disper_reqs: List[DispersionRequirement]
        :param red_trans_reqs: The red_trans_reqs of this EventFilter.  # noqa: E501
        :type red_trans_reqs: List[RedundantTransmissionExpReq]
        :param wlan_reqs: The wlan_reqs of this EventFilter.  # noqa: E501
        :type wlan_reqs: List[WlanPerformanceReq]
        :param list_of_ana_subsets: The list_of_ana_subsets of this EventFilter.  # noqa: E501
        :type list_of_ana_subsets: List[AnalyticsSubset]
        :param upf_id: The upf_id of this EventFilter.  # noqa: E501
        :type upf_id: str
        :param app_server_addrs: The app_server_addrs of this EventFilter.  # noqa: E501
        :type app_server_addrs: List[AddrFqdn]
        :param dn_perf_reqs: The dn_perf_reqs of this EventFilter.  # noqa: E501
        :type dn_perf_reqs: List[DnPerformanceReq]
        """
        self.openapi_types = {
            'any_slice': bool,
            'snssais': List[Snssai],
            'app_ids': List[str],
            'dnns': List[str],
            'dnais': List[str],
            'ladn_dnns': List[str],
            'network_area': NetworkAreaInfo,
            'visited_areas': List[NetworkAreaInfo],
            'max_top_app_ul_nbr': int,
            'max_top_app_dl_nbr': int,
            'nf_instance_ids': List[str],
            'nf_set_ids': List[str],
            'nf_types': List[NFType],
            'nsi_id_infos': List[NsiIdInfo],
            'qos_requ': QosRequirement,
            'nw_perf_types': List[NetworkPerfType],
            'bw_requs': List[BwRequirement],
            'excep_ids': List[ExceptionId],
            'expt_ana_type': ExpectedAnalyticsType,
            'expt_ue_behav': ExpectedUeBehaviourData,
            'rat_freqs': List[RatFreqInformation],
            'disper_reqs': List[DispersionRequirement],
            'red_trans_reqs': List[RedundantTransmissionExpReq],
            'wlan_reqs': List[WlanPerformanceReq],
            'list_of_ana_subsets': List[AnalyticsSubset],
            'upf_id': str,
            'app_server_addrs': List[AddrFqdn],
            'dn_perf_reqs': List[DnPerformanceReq]
        }

        self.attribute_map = {
            'any_slice': 'anySlice',
            'snssais': 'snssais',
            'app_ids': 'appIds',
            'dnns': 'dnns',
            'dnais': 'dnais',
            'ladn_dnns': 'ladnDnns',
            'network_area': 'networkArea',
            'visited_areas': 'visitedAreas',
            'max_top_app_ul_nbr': 'maxTopAppUlNbr',
            'max_top_app_dl_nbr': 'maxTopAppDlNbr',
            'nf_instance_ids': 'nfInstanceIds',
            'nf_set_ids': 'nfSetIds',
            'nf_types': 'nfTypes',
            'nsi_id_infos': 'nsiIdInfos',
            'qos_requ': 'qosRequ',
            'nw_perf_types': 'nwPerfTypes',
            'bw_requs': 'bwRequs',
            'excep_ids': 'excepIds',
            'expt_ana_type': 'exptAnaType',
            'expt_ue_behav': 'exptUeBehav',
            'rat_freqs': 'ratFreqs',
            'disper_reqs': 'disperReqs',
            'red_trans_reqs': 'redTransReqs',
            'wlan_reqs': 'wlanReqs',
            'list_of_ana_subsets': 'listOfAnaSubsets',
            'upf_id': 'upfId',
            'app_server_addrs': 'appServerAddrs',
            'dn_perf_reqs': 'dnPerfReqs'
        }

        self.any_slice = any_slice
        self.snssais = snssais
        self.app_ids = app_ids
        self.dnns = dnns
        self.dnais = dnais
        self.ladn_dnns = ladn_dnns
        self.network_area = network_area
        self.visited_areas = visited_areas
        self.max_top_app_ul_nbr = max_top_app_ul_nbr
        self.max_top_app_dl_nbr = max_top_app_dl_nbr
        self.nf_instance_ids = nf_instance_ids
        self.nf_set_ids = nf_set_ids
        self.nf_types = nf_types
        self.nsi_id_infos = nsi_id_infos
        self.qos_requ = qos_requ
        self.nw_perf_types = nw_perf_types
        self.bw_requs = bw_requs
        self.excep_ids = excep_ids
        self.expt_ana_type = expt_ana_type
        self.expt_ue_behav = expt_ue_behav
        self.rat_freqs = rat_freqs
        self.disper_reqs = disper_reqs
        self.red_trans_reqs = red_trans_reqs
        self.wlan_reqs = wlan_reqs
        self.list_of_ana_subsets = list_of_ana_subsets
        self.upf_id = upf_id
        self.app_server_addrs = app_server_addrs
        self.dn_perf_reqs = dn_perf_reqs

    @classmethod
    def from_dict(cls, dikt) -> 'EventFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventFilter of this EventFilter.  # noqa: E501
        :rtype: EventFilter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def any_slice(self):
        """Gets the any_slice of this EventFilter.

        FALSE represents not applicable for all slices. TRUE represents applicable for all slices.   # noqa: E501

        :return: The any_slice of this EventFilter.
        :rtype: bool
        """
        return self._any_slice

    @any_slice.setter
    def any_slice(self, any_slice):
        """Sets the any_slice of this EventFilter.

        FALSE represents not applicable for all slices. TRUE represents applicable for all slices.   # noqa: E501

        :param any_slice: The any_slice of this EventFilter.
        :type any_slice: bool
        """

        self._any_slice = any_slice

    @property
    def snssais(self):
        """Gets the snssais of this EventFilter.

        Identification(s) of network slice.  # noqa: E501

        :return: The snssais of this EventFilter.
        :rtype: List[Snssai]
        """
        return self._snssais

    @snssais.setter
    def snssais(self, snssais):
        """Sets the snssais of this EventFilter.

        Identification(s) of network slice.  # noqa: E501

        :param snssais: The snssais of this EventFilter.
        :type snssais: List[Snssai]
        """
        if snssais is not None and len(snssais) < 1:
            raise ValueError("Invalid value for `snssais`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._snssais = snssais

    @property
    def app_ids(self):
        """Gets the app_ids of this EventFilter.


        :return: The app_ids of this EventFilter.
        :rtype: List[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this EventFilter.


        :param app_ids: The app_ids of this EventFilter.
        :type app_ids: List[str]
        """
        if app_ids is not None and len(app_ids) < 1:
            raise ValueError("Invalid value for `app_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._app_ids = app_ids

    @property
    def dnns(self):
        """Gets the dnns of this EventFilter.


        :return: The dnns of this EventFilter.
        :rtype: List[str]
        """
        return self._dnns

    @dnns.setter
    def dnns(self, dnns):
        """Sets the dnns of this EventFilter.


        :param dnns: The dnns of this EventFilter.
        :type dnns: List[str]
        """
        if dnns is not None and len(dnns) < 1:
            raise ValueError("Invalid value for `dnns`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dnns = dnns

    @property
    def dnais(self):
        """Gets the dnais of this EventFilter.


        :return: The dnais of this EventFilter.
        :rtype: List[str]
        """
        return self._dnais

    @dnais.setter
    def dnais(self, dnais):
        """Sets the dnais of this EventFilter.


        :param dnais: The dnais of this EventFilter.
        :type dnais: List[str]
        """
        if dnais is not None and len(dnais) < 1:
            raise ValueError("Invalid value for `dnais`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dnais = dnais

    @property
    def ladn_dnns(self):
        """Gets the ladn_dnns of this EventFilter.

        Identification(s) of LADN DNN to indicate the LADN service area as the AOI.  # noqa: E501

        :return: The ladn_dnns of this EventFilter.
        :rtype: List[str]
        """
        return self._ladn_dnns

    @ladn_dnns.setter
    def ladn_dnns(self, ladn_dnns):
        """Sets the ladn_dnns of this EventFilter.

        Identification(s) of LADN DNN to indicate the LADN service area as the AOI.  # noqa: E501

        :param ladn_dnns: The ladn_dnns of this EventFilter.
        :type ladn_dnns: List[str]
        """
        if ladn_dnns is not None and len(ladn_dnns) < 1:
            raise ValueError("Invalid value for `ladn_dnns`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ladn_dnns = ladn_dnns

    @property
    def network_area(self):
        """Gets the network_area of this EventFilter.


        :return: The network_area of this EventFilter.
        :rtype: NetworkAreaInfo
        """
        return self._network_area

    @network_area.setter
    def network_area(self, network_area):
        """Sets the network_area of this EventFilter.


        :param network_area: The network_area of this EventFilter.
        :type network_area: NetworkAreaInfo
        """

        self._network_area = network_area

    @property
    def visited_areas(self):
        """Gets the visited_areas of this EventFilter.


        :return: The visited_areas of this EventFilter.
        :rtype: List[NetworkAreaInfo]
        """
        return self._visited_areas

    @visited_areas.setter
    def visited_areas(self, visited_areas):
        """Sets the visited_areas of this EventFilter.


        :param visited_areas: The visited_areas of this EventFilter.
        :type visited_areas: List[NetworkAreaInfo]
        """
        if visited_areas is not None and len(visited_areas) < 1:
            raise ValueError("Invalid value for `visited_areas`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._visited_areas = visited_areas

    @property
    def max_top_app_ul_nbr(self):
        """Gets the max_top_app_ul_nbr of this EventFilter.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The max_top_app_ul_nbr of this EventFilter.
        :rtype: int
        """
        return self._max_top_app_ul_nbr

    @max_top_app_ul_nbr.setter
    def max_top_app_ul_nbr(self, max_top_app_ul_nbr):
        """Sets the max_top_app_ul_nbr of this EventFilter.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param max_top_app_ul_nbr: The max_top_app_ul_nbr of this EventFilter.
        :type max_top_app_ul_nbr: int
        """
        if max_top_app_ul_nbr is not None and max_top_app_ul_nbr < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_top_app_ul_nbr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_top_app_ul_nbr = max_top_app_ul_nbr

    @property
    def max_top_app_dl_nbr(self):
        """Gets the max_top_app_dl_nbr of this EventFilter.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The max_top_app_dl_nbr of this EventFilter.
        :rtype: int
        """
        return self._max_top_app_dl_nbr

    @max_top_app_dl_nbr.setter
    def max_top_app_dl_nbr(self, max_top_app_dl_nbr):
        """Sets the max_top_app_dl_nbr of this EventFilter.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param max_top_app_dl_nbr: The max_top_app_dl_nbr of this EventFilter.
        :type max_top_app_dl_nbr: int
        """
        if max_top_app_dl_nbr is not None and max_top_app_dl_nbr < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_top_app_dl_nbr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_top_app_dl_nbr = max_top_app_dl_nbr

    @property
    def nf_instance_ids(self):
        """Gets the nf_instance_ids of this EventFilter.


        :return: The nf_instance_ids of this EventFilter.
        :rtype: List[str]
        """
        return self._nf_instance_ids

    @nf_instance_ids.setter
    def nf_instance_ids(self, nf_instance_ids):
        """Sets the nf_instance_ids of this EventFilter.


        :param nf_instance_ids: The nf_instance_ids of this EventFilter.
        :type nf_instance_ids: List[str]
        """
        if nf_instance_ids is not None and len(nf_instance_ids) < 1:
            raise ValueError("Invalid value for `nf_instance_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_instance_ids = nf_instance_ids

    @property
    def nf_set_ids(self):
        """Gets the nf_set_ids of this EventFilter.


        :return: The nf_set_ids of this EventFilter.
        :rtype: List[str]
        """
        return self._nf_set_ids

    @nf_set_ids.setter
    def nf_set_ids(self, nf_set_ids):
        """Sets the nf_set_ids of this EventFilter.


        :param nf_set_ids: The nf_set_ids of this EventFilter.
        :type nf_set_ids: List[str]
        """
        if nf_set_ids is not None and len(nf_set_ids) < 1:
            raise ValueError("Invalid value for `nf_set_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_set_ids = nf_set_ids

    @property
    def nf_types(self):
        """Gets the nf_types of this EventFilter.


        :return: The nf_types of this EventFilter.
        :rtype: List[NFType]
        """
        return self._nf_types

    @nf_types.setter
    def nf_types(self, nf_types):
        """Sets the nf_types of this EventFilter.


        :param nf_types: The nf_types of this EventFilter.
        :type nf_types: List[NFType]
        """
        if nf_types is not None and len(nf_types) < 1:
            raise ValueError("Invalid value for `nf_types`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_types = nf_types

    @property
    def nsi_id_infos(self):
        """Gets the nsi_id_infos of this EventFilter.


        :return: The nsi_id_infos of this EventFilter.
        :rtype: List[NsiIdInfo]
        """
        return self._nsi_id_infos

    @nsi_id_infos.setter
    def nsi_id_infos(self, nsi_id_infos):
        """Sets the nsi_id_infos of this EventFilter.


        :param nsi_id_infos: The nsi_id_infos of this EventFilter.
        :type nsi_id_infos: List[NsiIdInfo]
        """
        if nsi_id_infos is not None and len(nsi_id_infos) < 1:
            raise ValueError("Invalid value for `nsi_id_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nsi_id_infos = nsi_id_infos

    @property
    def qos_requ(self):
        """Gets the qos_requ of this EventFilter.


        :return: The qos_requ of this EventFilter.
        :rtype: QosRequirement
        """
        return self._qos_requ

    @qos_requ.setter
    def qos_requ(self, qos_requ):
        """Sets the qos_requ of this EventFilter.


        :param qos_requ: The qos_requ of this EventFilter.
        :type qos_requ: QosRequirement
        """

        self._qos_requ = qos_requ

    @property
    def nw_perf_types(self):
        """Gets the nw_perf_types of this EventFilter.


        :return: The nw_perf_types of this EventFilter.
        :rtype: List[NetworkPerfType]
        """
        return self._nw_perf_types

    @nw_perf_types.setter
    def nw_perf_types(self, nw_perf_types):
        """Sets the nw_perf_types of this EventFilter.


        :param nw_perf_types: The nw_perf_types of this EventFilter.
        :type nw_perf_types: List[NetworkPerfType]
        """
        if nw_perf_types is not None and len(nw_perf_types) < 1:
            raise ValueError("Invalid value for `nw_perf_types`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nw_perf_types = nw_perf_types

    @property
    def bw_requs(self):
        """Gets the bw_requs of this EventFilter.


        :return: The bw_requs of this EventFilter.
        :rtype: List[BwRequirement]
        """
        return self._bw_requs

    @bw_requs.setter
    def bw_requs(self, bw_requs):
        """Sets the bw_requs of this EventFilter.


        :param bw_requs: The bw_requs of this EventFilter.
        :type bw_requs: List[BwRequirement]
        """
        if bw_requs is not None and len(bw_requs) < 1:
            raise ValueError("Invalid value for `bw_requs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._bw_requs = bw_requs

    @property
    def excep_ids(self):
        """Gets the excep_ids of this EventFilter.


        :return: The excep_ids of this EventFilter.
        :rtype: List[ExceptionId]
        """
        return self._excep_ids

    @excep_ids.setter
    def excep_ids(self, excep_ids):
        """Sets the excep_ids of this EventFilter.


        :param excep_ids: The excep_ids of this EventFilter.
        :type excep_ids: List[ExceptionId]
        """
        if excep_ids is not None and len(excep_ids) < 1:
            raise ValueError("Invalid value for `excep_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._excep_ids = excep_ids

    @property
    def expt_ana_type(self):
        """Gets the expt_ana_type of this EventFilter.


        :return: The expt_ana_type of this EventFilter.
        :rtype: ExpectedAnalyticsType
        """
        return self._expt_ana_type

    @expt_ana_type.setter
    def expt_ana_type(self, expt_ana_type):
        """Sets the expt_ana_type of this EventFilter.


        :param expt_ana_type: The expt_ana_type of this EventFilter.
        :type expt_ana_type: ExpectedAnalyticsType
        """

        self._expt_ana_type = expt_ana_type

    @property
    def expt_ue_behav(self):
        """Gets the expt_ue_behav of this EventFilter.


        :return: The expt_ue_behav of this EventFilter.
        :rtype: ExpectedUeBehaviourData
        """
        return self._expt_ue_behav

    @expt_ue_behav.setter
    def expt_ue_behav(self, expt_ue_behav):
        """Sets the expt_ue_behav of this EventFilter.


        :param expt_ue_behav: The expt_ue_behav of this EventFilter.
        :type expt_ue_behav: ExpectedUeBehaviourData
        """

        self._expt_ue_behav = expt_ue_behav

    @property
    def rat_freqs(self):
        """Gets the rat_freqs of this EventFilter.


        :return: The rat_freqs of this EventFilter.
        :rtype: List[RatFreqInformation]
        """
        return self._rat_freqs

    @rat_freqs.setter
    def rat_freqs(self, rat_freqs):
        """Sets the rat_freqs of this EventFilter.


        :param rat_freqs: The rat_freqs of this EventFilter.
        :type rat_freqs: List[RatFreqInformation]
        """
        if rat_freqs is not None and len(rat_freqs) < 1:
            raise ValueError("Invalid value for `rat_freqs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._rat_freqs = rat_freqs

    @property
    def disper_reqs(self):
        """Gets the disper_reqs of this EventFilter.


        :return: The disper_reqs of this EventFilter.
        :rtype: List[DispersionRequirement]
        """
        return self._disper_reqs

    @disper_reqs.setter
    def disper_reqs(self, disper_reqs):
        """Sets the disper_reqs of this EventFilter.


        :param disper_reqs: The disper_reqs of this EventFilter.
        :type disper_reqs: List[DispersionRequirement]
        """
        if disper_reqs is not None and len(disper_reqs) < 1:
            raise ValueError("Invalid value for `disper_reqs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._disper_reqs = disper_reqs

    @property
    def red_trans_reqs(self):
        """Gets the red_trans_reqs of this EventFilter.


        :return: The red_trans_reqs of this EventFilter.
        :rtype: List[RedundantTransmissionExpReq]
        """
        return self._red_trans_reqs

    @red_trans_reqs.setter
    def red_trans_reqs(self, red_trans_reqs):
        """Sets the red_trans_reqs of this EventFilter.


        :param red_trans_reqs: The red_trans_reqs of this EventFilter.
        :type red_trans_reqs: List[RedundantTransmissionExpReq]
        """
        if red_trans_reqs is not None and len(red_trans_reqs) < 1:
            raise ValueError("Invalid value for `red_trans_reqs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._red_trans_reqs = red_trans_reqs

    @property
    def wlan_reqs(self):
        """Gets the wlan_reqs of this EventFilter.


        :return: The wlan_reqs of this EventFilter.
        :rtype: List[WlanPerformanceReq]
        """
        return self._wlan_reqs

    @wlan_reqs.setter
    def wlan_reqs(self, wlan_reqs):
        """Sets the wlan_reqs of this EventFilter.


        :param wlan_reqs: The wlan_reqs of this EventFilter.
        :type wlan_reqs: List[WlanPerformanceReq]
        """
        if wlan_reqs is not None and len(wlan_reqs) < 1:
            raise ValueError("Invalid value for `wlan_reqs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._wlan_reqs = wlan_reqs

    @property
    def list_of_ana_subsets(self):
        """Gets the list_of_ana_subsets of this EventFilter.


        :return: The list_of_ana_subsets of this EventFilter.
        :rtype: List[AnalyticsSubset]
        """
        return self._list_of_ana_subsets

    @list_of_ana_subsets.setter
    def list_of_ana_subsets(self, list_of_ana_subsets):
        """Sets the list_of_ana_subsets of this EventFilter.


        :param list_of_ana_subsets: The list_of_ana_subsets of this EventFilter.
        :type list_of_ana_subsets: List[AnalyticsSubset]
        """
        if list_of_ana_subsets is not None and len(list_of_ana_subsets) < 1:
            raise ValueError("Invalid value for `list_of_ana_subsets`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._list_of_ana_subsets = list_of_ana_subsets

    @property
    def upf_id(self):
        """Gets the upf_id of this EventFilter.

        Identifies the UPF.  # noqa: E501

        :return: The upf_id of this EventFilter.
        :rtype: str
        """
        return self._upf_id

    @upf_id.setter
    def upf_id(self, upf_id):
        """Sets the upf_id of this EventFilter.

        Identifies the UPF.  # noqa: E501

        :param upf_id: The upf_id of this EventFilter.
        :type upf_id: str
        """

        self._upf_id = upf_id

    @property
    def app_server_addrs(self):
        """Gets the app_server_addrs of this EventFilter.


        :return: The app_server_addrs of this EventFilter.
        :rtype: List[AddrFqdn]
        """
        return self._app_server_addrs

    @app_server_addrs.setter
    def app_server_addrs(self, app_server_addrs):
        """Sets the app_server_addrs of this EventFilter.


        :param app_server_addrs: The app_server_addrs of this EventFilter.
        :type app_server_addrs: List[AddrFqdn]
        """
        if app_server_addrs is not None and len(app_server_addrs) < 1:
            raise ValueError("Invalid value for `app_server_addrs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._app_server_addrs = app_server_addrs

    @property
    def dn_perf_reqs(self):
        """Gets the dn_perf_reqs of this EventFilter.


        :return: The dn_perf_reqs of this EventFilter.
        :rtype: List[DnPerformanceReq]
        """
        return self._dn_perf_reqs

    @dn_perf_reqs.setter
    def dn_perf_reqs(self, dn_perf_reqs):
        """Sets the dn_perf_reqs of this EventFilter.


        :param dn_perf_reqs: The dn_perf_reqs of this EventFilter.
        :type dn_perf_reqs: List[DnPerformanceReq]
        """
        if dn_perf_reqs is not None and len(dn_perf_reqs) < 1:
            raise ValueError("Invalid value for `dn_perf_reqs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dn_perf_reqs = dn_perf_reqs
