# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.addr_fqdn import AddrFqdn
from openapi_server.models.location_info import LocationInfo
from openapi_server.models.network_area_info import NetworkAreaInfo
from openapi_server.models.rat_freq_information import RatFreqInformation
from openapi_server.models.service_experience_type import ServiceExperienceType
from openapi_server.models.snssai import Snssai
from openapi_server.models.svc_experience import SvcExperience
from openapi_server.models.upf_information import UpfInformation
from openapi_server import util

from openapi_server.models.addr_fqdn import AddrFqdn  # noqa: E501
from openapi_server.models.location_info import LocationInfo  # noqa: E501
from openapi_server.models.network_area_info import NetworkAreaInfo  # noqa: E501
from openapi_server.models.rat_freq_information import RatFreqInformation  # noqa: E501
from openapi_server.models.service_experience_type import ServiceExperienceType  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501
from openapi_server.models.svc_experience import SvcExperience  # noqa: E501
from openapi_server.models.upf_information import UpfInformation  # noqa: E501

class ServiceExperienceInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, svc_exprc=None, svc_exprc_variance=None, supis=None, snssai=None, app_id=None, srv_expc_type=None, ue_locs=None, upf_info=None, dnai=None, app_server_inst=None, confidence=None, dnn=None, network_area=None, nsi_id=None, ratio=None, rat_freq=None):  # noqa: E501
        """ServiceExperienceInfo - a model defined in OpenAPI

        :param svc_exprc: The svc_exprc of this ServiceExperienceInfo.  # noqa: E501
        :type svc_exprc: SvcExperience
        :param svc_exprc_variance: The svc_exprc_variance of this ServiceExperienceInfo.  # noqa: E501
        :type svc_exprc_variance: float
        :param supis: The supis of this ServiceExperienceInfo.  # noqa: E501
        :type supis: List[str]
        :param snssai: The snssai of this ServiceExperienceInfo.  # noqa: E501
        :type snssai: Snssai
        :param app_id: The app_id of this ServiceExperienceInfo.  # noqa: E501
        :type app_id: str
        :param srv_expc_type: The srv_expc_type of this ServiceExperienceInfo.  # noqa: E501
        :type srv_expc_type: ServiceExperienceType
        :param ue_locs: The ue_locs of this ServiceExperienceInfo.  # noqa: E501
        :type ue_locs: List[LocationInfo]
        :param upf_info: The upf_info of this ServiceExperienceInfo.  # noqa: E501
        :type upf_info: UpfInformation
        :param dnai: The dnai of this ServiceExperienceInfo.  # noqa: E501
        :type dnai: str
        :param app_server_inst: The app_server_inst of this ServiceExperienceInfo.  # noqa: E501
        :type app_server_inst: AddrFqdn
        :param confidence: The confidence of this ServiceExperienceInfo.  # noqa: E501
        :type confidence: int
        :param dnn: The dnn of this ServiceExperienceInfo.  # noqa: E501
        :type dnn: str
        :param network_area: The network_area of this ServiceExperienceInfo.  # noqa: E501
        :type network_area: NetworkAreaInfo
        :param nsi_id: The nsi_id of this ServiceExperienceInfo.  # noqa: E501
        :type nsi_id: str
        :param ratio: The ratio of this ServiceExperienceInfo.  # noqa: E501
        :type ratio: int
        :param rat_freq: The rat_freq of this ServiceExperienceInfo.  # noqa: E501
        :type rat_freq: RatFreqInformation
        """
        self.openapi_types = {
            'svc_exprc': SvcExperience,
            'svc_exprc_variance': float,
            'supis': List[str],
            'snssai': Snssai,
            'app_id': str,
            'srv_expc_type': ServiceExperienceType,
            'ue_locs': List[LocationInfo],
            'upf_info': UpfInformation,
            'dnai': str,
            'app_server_inst': AddrFqdn,
            'confidence': int,
            'dnn': str,
            'network_area': NetworkAreaInfo,
            'nsi_id': str,
            'ratio': int,
            'rat_freq': RatFreqInformation
        }

        self.attribute_map = {
            'svc_exprc': 'svcExprc',
            'svc_exprc_variance': 'svcExprcVariance',
            'supis': 'supis',
            'snssai': 'snssai',
            'app_id': 'appId',
            'srv_expc_type': 'srvExpcType',
            'ue_locs': 'ueLocs',
            'upf_info': 'upfInfo',
            'dnai': 'dnai',
            'app_server_inst': 'appServerInst',
            'confidence': 'confidence',
            'dnn': 'dnn',
            'network_area': 'networkArea',
            'nsi_id': 'nsiId',
            'ratio': 'ratio',
            'rat_freq': 'ratFreq'
        }

        self.svc_exprc = svc_exprc
        self.svc_exprc_variance = svc_exprc_variance
        self.supis = supis
        self.snssai = snssai
        self.app_id = app_id
        self.srv_expc_type = srv_expc_type
        self.ue_locs = ue_locs
        self.upf_info = upf_info
        self.dnai = dnai
        self.app_server_inst = app_server_inst
        self.confidence = confidence
        self.dnn = dnn
        self.network_area = network_area
        self.nsi_id = nsi_id
        self.ratio = ratio
        self.rat_freq = rat_freq

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceExperienceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceExperienceInfo of this ServiceExperienceInfo.  # noqa: E501
        :rtype: ServiceExperienceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def svc_exprc(self):
        """Gets the svc_exprc of this ServiceExperienceInfo.


        :return: The svc_exprc of this ServiceExperienceInfo.
        :rtype: SvcExperience
        """
        return self._svc_exprc

    @svc_exprc.setter
    def svc_exprc(self, svc_exprc):
        """Sets the svc_exprc of this ServiceExperienceInfo.


        :param svc_exprc: The svc_exprc of this ServiceExperienceInfo.
        :type svc_exprc: SvcExperience
        """
        if svc_exprc is None:
            raise ValueError("Invalid value for `svc_exprc`, must not be `None`")  # noqa: E501

        self._svc_exprc = svc_exprc

    @property
    def svc_exprc_variance(self):
        """Gets the svc_exprc_variance of this ServiceExperienceInfo.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The svc_exprc_variance of this ServiceExperienceInfo.
        :rtype: float
        """
        return self._svc_exprc_variance

    @svc_exprc_variance.setter
    def svc_exprc_variance(self, svc_exprc_variance):
        """Sets the svc_exprc_variance of this ServiceExperienceInfo.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param svc_exprc_variance: The svc_exprc_variance of this ServiceExperienceInfo.
        :type svc_exprc_variance: float
        """

        self._svc_exprc_variance = svc_exprc_variance

    @property
    def supis(self):
        """Gets the supis of this ServiceExperienceInfo.


        :return: The supis of this ServiceExperienceInfo.
        :rtype: List[str]
        """
        return self._supis

    @supis.setter
    def supis(self, supis):
        """Sets the supis of this ServiceExperienceInfo.


        :param supis: The supis of this ServiceExperienceInfo.
        :type supis: List[str]
        """
        if supis is not None and len(supis) < 1:
            raise ValueError("Invalid value for `supis`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supis = supis

    @property
    def snssai(self):
        """Gets the snssai of this ServiceExperienceInfo.


        :return: The snssai of this ServiceExperienceInfo.
        :rtype: Snssai
        """
        return self._snssai

    @snssai.setter
    def snssai(self, snssai):
        """Sets the snssai of this ServiceExperienceInfo.


        :param snssai: The snssai of this ServiceExperienceInfo.
        :type snssai: Snssai
        """

        self._snssai = snssai

    @property
    def app_id(self):
        """Gets the app_id of this ServiceExperienceInfo.

        String providing an application identifier.  # noqa: E501

        :return: The app_id of this ServiceExperienceInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ServiceExperienceInfo.

        String providing an application identifier.  # noqa: E501

        :param app_id: The app_id of this ServiceExperienceInfo.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def srv_expc_type(self):
        """Gets the srv_expc_type of this ServiceExperienceInfo.


        :return: The srv_expc_type of this ServiceExperienceInfo.
        :rtype: ServiceExperienceType
        """
        return self._srv_expc_type

    @srv_expc_type.setter
    def srv_expc_type(self, srv_expc_type):
        """Sets the srv_expc_type of this ServiceExperienceInfo.


        :param srv_expc_type: The srv_expc_type of this ServiceExperienceInfo.
        :type srv_expc_type: ServiceExperienceType
        """

        self._srv_expc_type = srv_expc_type

    @property
    def ue_locs(self):
        """Gets the ue_locs of this ServiceExperienceInfo.


        :return: The ue_locs of this ServiceExperienceInfo.
        :rtype: List[LocationInfo]
        """
        return self._ue_locs

    @ue_locs.setter
    def ue_locs(self, ue_locs):
        """Sets the ue_locs of this ServiceExperienceInfo.


        :param ue_locs: The ue_locs of this ServiceExperienceInfo.
        :type ue_locs: List[LocationInfo]
        """
        if ue_locs is not None and len(ue_locs) < 1:
            raise ValueError("Invalid value for `ue_locs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_locs = ue_locs

    @property
    def upf_info(self):
        """Gets the upf_info of this ServiceExperienceInfo.


        :return: The upf_info of this ServiceExperienceInfo.
        :rtype: UpfInformation
        """
        return self._upf_info

    @upf_info.setter
    def upf_info(self, upf_info):
        """Sets the upf_info of this ServiceExperienceInfo.


        :param upf_info: The upf_info of this ServiceExperienceInfo.
        :type upf_info: UpfInformation
        """

        self._upf_info = upf_info

    @property
    def dnai(self):
        """Gets the dnai of this ServiceExperienceInfo.

        DNAI (Data network access identifier), see clause 5.6.7 of 3GPP TS 23.501.  # noqa: E501

        :return: The dnai of this ServiceExperienceInfo.
        :rtype: str
        """
        return self._dnai

    @dnai.setter
    def dnai(self, dnai):
        """Sets the dnai of this ServiceExperienceInfo.

        DNAI (Data network access identifier), see clause 5.6.7 of 3GPP TS 23.501.  # noqa: E501

        :param dnai: The dnai of this ServiceExperienceInfo.
        :type dnai: str
        """

        self._dnai = dnai

    @property
    def app_server_inst(self):
        """Gets the app_server_inst of this ServiceExperienceInfo.


        :return: The app_server_inst of this ServiceExperienceInfo.
        :rtype: AddrFqdn
        """
        return self._app_server_inst

    @app_server_inst.setter
    def app_server_inst(self, app_server_inst):
        """Sets the app_server_inst of this ServiceExperienceInfo.


        :param app_server_inst: The app_server_inst of this ServiceExperienceInfo.
        :type app_server_inst: AddrFqdn
        """

        self._app_server_inst = app_server_inst

    @property
    def confidence(self):
        """Gets the confidence of this ServiceExperienceInfo.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The confidence of this ServiceExperienceInfo.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ServiceExperienceInfo.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param confidence: The confidence of this ServiceExperienceInfo.
        :type confidence: int
        """
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def dnn(self):
        """Gets the dnn of this ServiceExperienceInfo.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :return: The dnn of this ServiceExperienceInfo.
        :rtype: str
        """
        return self._dnn

    @dnn.setter
    def dnn(self, dnn):
        """Sets the dnn of this ServiceExperienceInfo.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :param dnn: The dnn of this ServiceExperienceInfo.
        :type dnn: str
        """

        self._dnn = dnn

    @property
    def network_area(self):
        """Gets the network_area of this ServiceExperienceInfo.


        :return: The network_area of this ServiceExperienceInfo.
        :rtype: NetworkAreaInfo
        """
        return self._network_area

    @network_area.setter
    def network_area(self, network_area):
        """Sets the network_area of this ServiceExperienceInfo.


        :param network_area: The network_area of this ServiceExperienceInfo.
        :type network_area: NetworkAreaInfo
        """

        self._network_area = network_area

    @property
    def nsi_id(self):
        """Gets the nsi_id of this ServiceExperienceInfo.

        Contains the Identifier of the selected Network Slice instance  # noqa: E501

        :return: The nsi_id of this ServiceExperienceInfo.
        :rtype: str
        """
        return self._nsi_id

    @nsi_id.setter
    def nsi_id(self, nsi_id):
        """Sets the nsi_id of this ServiceExperienceInfo.

        Contains the Identifier of the selected Network Slice instance  # noqa: E501

        :param nsi_id: The nsi_id of this ServiceExperienceInfo.
        :type nsi_id: str
        """

        self._nsi_id = nsi_id

    @property
    def ratio(self):
        """Gets the ratio of this ServiceExperienceInfo.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :return: The ratio of this ServiceExperienceInfo.
        :rtype: int
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this ServiceExperienceInfo.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :param ratio: The ratio of this ServiceExperienceInfo.
        :type ratio: int
        """
        if ratio is not None and ratio > 100:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value less than or equal to `100`")  # noqa: E501
        if ratio is not None and ratio < 1:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ratio = ratio

    @property
    def rat_freq(self):
        """Gets the rat_freq of this ServiceExperienceInfo.


        :return: The rat_freq of this ServiceExperienceInfo.
        :rtype: RatFreqInformation
        """
        return self._rat_freq

    @rat_freq.setter
    def rat_freq(self, rat_freq):
        """Sets the rat_freq of this ServiceExperienceInfo.


        :param rat_freq: The rat_freq of this ServiceExperienceInfo.
        :type rat_freq: RatFreqInformation
        """

        self._rat_freq = rat_freq
