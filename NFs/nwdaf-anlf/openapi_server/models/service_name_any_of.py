# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ServiceNameAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NNRF_NFM = "nnrf-nfm"
    NNRF_DISC = "nnrf-disc"
    NNRF_OAUTH2 = "nnrf-oauth2"
    NUDM_SDM = "nudm-sdm"
    NUDM_UECM = "nudm-uecm"
    NUDM_UEAU = "nudm-ueau"
    NUDM_EE = "nudm-ee"
    NUDM_PP = "nudm-pp"
    NUDM_NIDDAU = "nudm-niddau"
    NUDM_MT = "nudm-mt"
    NUDM_SSAU = "nudm-ssau"
    NAMF_COMM = "namf-comm"
    NAMF_EVTS = "namf-evts"
    NAMF_MT = "namf-mt"
    NAMF_LOC = "namf-loc"
    NAMF_MBS_COMM = "namf-mbs-comm"
    NAMF_MBS_BC = "namf-mbs-bc"
    NSMF_PDUSESSION = "nsmf-pdusession"
    NSMF_EVENT_EXPOSURE = "nsmf-event-exposure"
    NSMF_NIDD = "nsmf-nidd"
    NAUSF_AUTH = "nausf-auth"
    NAUSF_SORPROTECTION = "nausf-sorprotection"
    NAUSF_UPUPROTECTION = "nausf-upuprotection"
    NNEF_PFDMANAGEMENT = "nnef-pfdmanagement"
    NNEF_SMCONTEXT = "nnef-smcontext"
    NNEF_EVENTEXPOSURE = "nnef-eventexposure"
    NNEF_EAS_DEPLOYMENT_INFO = "nnef-eas-deployment-info"
    _3GPP_CP_PARAMETER_PROVISIONING = "3gpp-cp-parameter-provisioning"
    _3GPP_DEVICE_TRIGGERING = "3gpp-device-triggering"
    _3GPP_BDT = "3gpp-bdt"
    _3GPP_TRAFFIC_INFLUENCE = "3gpp-traffic-influence"
    _3GPP_CHARGEABLE_PARTY = "3gpp-chargeable-party"
    _3GPP_AS_SESSION_WITH_QOS = "3gpp-as-session-with-qos"
    _3GPP_MSISDN_LESS_MO_SMS = "3gpp-msisdn-less-mo-sms"
    _3GPP_SERVICE_PARAMETER = "3gpp-service-parameter"
    _3GPP_MONITORING_EVENT = "3gpp-monitoring-event"
    _3GPP_NIDD_CONFIGURATION_TRIGGER = "3gpp-nidd-configuration-trigger"
    _3GPP_NIDD = "3gpp-nidd"
    _3GPP_ANALYTICSEXPOSURE = "3gpp-analyticsexposure"
    _3GPP_RACS_PARAMETER_PROVISIONING = "3gpp-racs-parameter-provisioning"
    _3GPP_ECR_CONTROL = "3gpp-ecr-control"
    _3GPP_APPLYING_BDT_POLICY = "3gpp-applying-bdt-policy"
    _3GPP_MO_LCS_NOTIFY = "3gpp-mo-lcs-notify"
    _3GPP_TIME_SYNC = "3gpp-time-sync"
    _3GPP_AM_INFLUENCE = "3gpp-am-influence"
    _3GPP_AM_POLICYAUTHORIZATION = "3gpp-am-policyauthorization"
    _3GPP_AKMA = "3gpp-akma"
    _3GPP_EAS_DEPLOYMENT = "3gpp-eas-deployment"
    _3GPP_IPTVCONFIGURATION = "3gpp-iptvconfiguration"
    _3GPP_MBS_TMGI = "3gpp-mbs-tmgi"
    _3GPP_MBS_SESSION = "3gpp-mbs-session"
    _3GPP_AUTHENTICATION = "3gpp-authentication"
    _3GPP_ASTI = "3gpp-asti"
    NPCF_AM_POLICY_CONTROL = "npcf-am-policy-control"
    NPCF_SMPOLICYCONTROL = "npcf-smpolicycontrol"
    NPCF_POLICYAUTHORIZATION = "npcf-policyauthorization"
    NPCF_BDTPOLICYCONTROL = "npcf-bdtpolicycontrol"
    NPCF_EVENTEXPOSURE = "npcf-eventexposure"
    NPCF_UE_POLICY_CONTROL = "npcf-ue-policy-control"
    NPCF_AM_POLICYAUTHORIZATION = "npcf-am-policyauthorization"
    NSMSF_SMS = "nsmsf-sms"
    NNSSF_NSSELECTION = "nnssf-nsselection"
    NNSSF_NSSAIAVAILABILITY = "nnssf-nssaiavailability"
    NUDR_DR = "nudr-dr"
    NUDR_GROUP_ID_MAP = "nudr-group-id-map"
    NLMF_LOC = "nlmf-loc"
    N5G_EIR_EIC = "n5g-eir-eic"
    NBSF_MANAGEMENT = "nbsf-management"
    NCHF_SPENDINGLIMITCONTROL = "nchf-spendinglimitcontrol"
    NCHF_CONVERGEDCHARGING = "nchf-convergedcharging"
    NCHF_OFFLINEONLYCHARGING = "nchf-offlineonlycharging"
    NNWDAF_EVENTSSUBSCRIPTION = "nnwdaf-eventssubscription"
    NNWDAF_ANALYTICSINFO = "nnwdaf-analyticsinfo"
    NNWDAF_DATAMANAGEMENT = "nnwdaf-datamanagement"
    NNWDAF_MLMODELPROVISION = "nnwdaf-mlmodelprovision"
    NGMLC_LOC = "ngmlc-loc"
    NUCMF_PROVISIONING = "nucmf-provisioning"
    NUCMF_UECAPABILITYMANAGEMENT = "nucmf-uecapabilitymanagement"
    NHSS_SDM = "nhss-sdm"
    NHSS_UECM = "nhss-uecm"
    NHSS_UEAU = "nhss-ueau"
    NHSS_EE = "nhss-ee"
    NHSS_IMS_SDM = "nhss-ims-sdm"
    NHSS_IMS_UECM = "nhss-ims-uecm"
    NHSS_IMS_UEAU = "nhss-ims-ueau"
    NHSS_GBA_SDM = "nhss-gba-sdm"
    NHSS_GBA_UEAU = "nhss-gba-ueau"
    NSEPP_TELESCOPIC = "nsepp-telescopic"
    NSORAF_SOR = "nsoraf-sor"
    NSPAF_SECURED_PACKET = "nspaf-secured-packet"
    NUDSF_DR = "nudsf-dr"
    NUDSF_TIMER = "nudsf-timer"
    NNSSAAF_NSSAA = "nnssaaf-nssaa"
    NNSSAAF_AIW = "nnssaaf-aiw"
    NAANF_AKMA = "naanf-akma"
    N5GDDNMF_DISCOVERY = "n5gddnmf-discovery"
    NMFAF_3DADM = "nmfaf-3dadm"
    NMFAF_3CADM = "nmfaf-3cadm"
    NEASDF_DNSCONTEXT = "neasdf-dnscontext"
    NEASDF_BASELINEDNSPATTERN = "neasdf-baselinednspattern"
    NDCCF_DM = "ndccf-dm"
    NDCCF_CM = "ndccf-cm"
    NNSACF_NSAC = "nnsacf-nsac"
    NNSACF_SLICE_EE = "nnsacf-slice-ee"
    NMBSMF_TMGI = "nmbsmf-tmgi"
    NMBSMF_MBSSESSION = "nmbsmf-mbssession"
    NADRF_DM = "nadrf-dm"
    NBSP_GBA = "nbsp-gba"
    NTSCTSF_TIME_SYNC = "ntsctsf-time-sync"
    NTSCTSF_QOS_TSCAI = "ntsctsf-qos-tscai"
    NTSCTSF_ASTI = "ntsctsf-asti"
    NPKMF_KEYREQ = "npkmf-keyreq"
    NMNPF_NPSTATUS = "nmnpf-npstatus"
    NIWMSC_SMSERVICE = "niwmsc-smservice"
    NMBSF_MBSUSERSERV = "nmbsf-mbsuserserv"
    NMBSF_MBSUSERDATAING = "nmbsf-mbsuserdataing"
    NMBSTF_DISTSESSION = "nmbstf-distsession"
    def __init__(self):  # noqa: E501
        """ServiceNameAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceNameAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceName_anyOf of this ServiceNameAnyOf.  # noqa: E501
        :rtype: ServiceNameAnyOf
        """
        return util.deserialize_model(dikt, cls)
