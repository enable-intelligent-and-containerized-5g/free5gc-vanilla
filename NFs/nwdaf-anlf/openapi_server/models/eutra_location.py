# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ecgi import Ecgi
from openapi_server.models.global_ran_node_id import GlobalRanNodeId
from openapi_server.models.tai import Tai
import re
from openapi_server import util

from openapi_server.models.ecgi import Ecgi  # noqa: E501
from openapi_server.models.global_ran_node_id import GlobalRanNodeId  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
import re  # noqa: E501

class EutraLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tai=None, ignore_tai=False, ecgi=None, ignore_ecgi=False, age_of_location_information=None, ue_location_timestamp=None, geographical_information=None, geodetic_information=None, global_ngenb_id=None, global_enb_id=None):  # noqa: E501
        """EutraLocation - a model defined in OpenAPI

        :param tai: The tai of this EutraLocation.  # noqa: E501
        :type tai: Tai
        :param ignore_tai: The ignore_tai of this EutraLocation.  # noqa: E501
        :type ignore_tai: bool
        :param ecgi: The ecgi of this EutraLocation.  # noqa: E501
        :type ecgi: Ecgi
        :param ignore_ecgi: The ignore_ecgi of this EutraLocation.  # noqa: E501
        :type ignore_ecgi: bool
        :param age_of_location_information: The age_of_location_information of this EutraLocation.  # noqa: E501
        :type age_of_location_information: int
        :param ue_location_timestamp: The ue_location_timestamp of this EutraLocation.  # noqa: E501
        :type ue_location_timestamp: datetime
        :param geographical_information: The geographical_information of this EutraLocation.  # noqa: E501
        :type geographical_information: str
        :param geodetic_information: The geodetic_information of this EutraLocation.  # noqa: E501
        :type geodetic_information: str
        :param global_ngenb_id: The global_ngenb_id of this EutraLocation.  # noqa: E501
        :type global_ngenb_id: GlobalRanNodeId
        :param global_enb_id: The global_enb_id of this EutraLocation.  # noqa: E501
        :type global_enb_id: GlobalRanNodeId
        """
        self.openapi_types = {
            'tai': Tai,
            'ignore_tai': bool,
            'ecgi': Ecgi,
            'ignore_ecgi': bool,
            'age_of_location_information': int,
            'ue_location_timestamp': datetime,
            'geographical_information': str,
            'geodetic_information': str,
            'global_ngenb_id': GlobalRanNodeId,
            'global_enb_id': GlobalRanNodeId
        }

        self.attribute_map = {
            'tai': 'tai',
            'ignore_tai': 'ignoreTai',
            'ecgi': 'ecgi',
            'ignore_ecgi': 'ignoreEcgi',
            'age_of_location_information': 'ageOfLocationInformation',
            'ue_location_timestamp': 'ueLocationTimestamp',
            'geographical_information': 'geographicalInformation',
            'geodetic_information': 'geodeticInformation',
            'global_ngenb_id': 'globalNgenbId',
            'global_enb_id': 'globalENbId'
        }

        self.tai = tai
        self.ignore_tai = ignore_tai
        self.ecgi = ecgi
        self.ignore_ecgi = ignore_ecgi
        self.age_of_location_information = age_of_location_information
        self.ue_location_timestamp = ue_location_timestamp
        self.geographical_information = geographical_information
        self.geodetic_information = geodetic_information
        self.global_ngenb_id = global_ngenb_id
        self.global_enb_id = global_enb_id

    @classmethod
    def from_dict(cls, dikt) -> 'EutraLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EutraLocation of this EutraLocation.  # noqa: E501
        :rtype: EutraLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tai(self):
        """Gets the tai of this EutraLocation.


        :return: The tai of this EutraLocation.
        :rtype: Tai
        """
        return self._tai

    @tai.setter
    def tai(self, tai):
        """Sets the tai of this EutraLocation.


        :param tai: The tai of this EutraLocation.
        :type tai: Tai
        """
        if tai is None:
            raise ValueError("Invalid value for `tai`, must not be `None`")  # noqa: E501

        self._tai = tai

    @property
    def ignore_tai(self):
        """Gets the ignore_tai of this EutraLocation.


        :return: The ignore_tai of this EutraLocation.
        :rtype: bool
        """
        return self._ignore_tai

    @ignore_tai.setter
    def ignore_tai(self, ignore_tai):
        """Sets the ignore_tai of this EutraLocation.


        :param ignore_tai: The ignore_tai of this EutraLocation.
        :type ignore_tai: bool
        """

        self._ignore_tai = ignore_tai

    @property
    def ecgi(self):
        """Gets the ecgi of this EutraLocation.


        :return: The ecgi of this EutraLocation.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this EutraLocation.


        :param ecgi: The ecgi of this EutraLocation.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def ignore_ecgi(self):
        """Gets the ignore_ecgi of this EutraLocation.

        This flag when present shall indicate that the Ecgi shall be ignored When present, it shall be set as follows: - true: ecgi shall be ignored. - false (default): ecgi shall not be ignored.   # noqa: E501

        :return: The ignore_ecgi of this EutraLocation.
        :rtype: bool
        """
        return self._ignore_ecgi

    @ignore_ecgi.setter
    def ignore_ecgi(self, ignore_ecgi):
        """Sets the ignore_ecgi of this EutraLocation.

        This flag when present shall indicate that the Ecgi shall be ignored When present, it shall be set as follows: - true: ecgi shall be ignored. - false (default): ecgi shall not be ignored.   # noqa: E501

        :param ignore_ecgi: The ignore_ecgi of this EutraLocation.
        :type ignore_ecgi: bool
        """

        self._ignore_ecgi = ignore_ecgi

    @property
    def age_of_location_information(self):
        """Gets the age_of_location_information of this EutraLocation.

        The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \"0\" indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful NG-RAN location reporting procedure with the eNB when the UE is in connected mode.  Any other value than \"0\" indicates that the location information is the last known one.  See 3GPP TS 29.002 clause 17.7.8.   # noqa: E501

        :return: The age_of_location_information of this EutraLocation.
        :rtype: int
        """
        return self._age_of_location_information

    @age_of_location_information.setter
    def age_of_location_information(self, age_of_location_information):
        """Sets the age_of_location_information of this EutraLocation.

        The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \"0\" indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful NG-RAN location reporting procedure with the eNB when the UE is in connected mode.  Any other value than \"0\" indicates that the location information is the last known one.  See 3GPP TS 29.002 clause 17.7.8.   # noqa: E501

        :param age_of_location_information: The age_of_location_information of this EutraLocation.
        :type age_of_location_information: int
        """
        if age_of_location_information is not None and age_of_location_information > 32767:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_information`, must be a value less than or equal to `32767`")  # noqa: E501
        if age_of_location_information is not None and age_of_location_information < 0:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_information`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age_of_location_information = age_of_location_information

    @property
    def ue_location_timestamp(self):
        """Gets the ue_location_timestamp of this EutraLocation.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The ue_location_timestamp of this EutraLocation.
        :rtype: datetime
        """
        return self._ue_location_timestamp

    @ue_location_timestamp.setter
    def ue_location_timestamp(self, ue_location_timestamp):
        """Sets the ue_location_timestamp of this EutraLocation.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param ue_location_timestamp: The ue_location_timestamp of this EutraLocation.
        :type ue_location_timestamp: datetime
        """

        self._ue_location_timestamp = ue_location_timestamp

    @property
    def geographical_information(self):
        """Gets the geographical_information of this EutraLocation.

        Refer to geographical Information. See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.   # noqa: E501

        :return: The geographical_information of this EutraLocation.
        :rtype: str
        """
        return self._geographical_information

    @geographical_information.setter
    def geographical_information(self, geographical_information):
        """Sets the geographical_information of this EutraLocation.

        Refer to geographical Information. See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.   # noqa: E501

        :param geographical_information: The geographical_information of this EutraLocation.
        :type geographical_information: str
        """
        if geographical_information is not None and not re.search(r'^[0-9A-F]{16}$', geographical_information):  # noqa: E501
            raise ValueError("Invalid value for `geographical_information`, must be a follow pattern or equal to `/^[0-9A-F]{16}$/`")  # noqa: E501

        self._geographical_information = geographical_information

    @property
    def geodetic_information(self):
        """Gets the geodetic_information of this EutraLocation.

        Refers to Calling Geodetic Location. See ITU-T Recommendation Q.763 (1999) [24] clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.   # noqa: E501

        :return: The geodetic_information of this EutraLocation.
        :rtype: str
        """
        return self._geodetic_information

    @geodetic_information.setter
    def geodetic_information(self, geodetic_information):
        """Sets the geodetic_information of this EutraLocation.

        Refers to Calling Geodetic Location. See ITU-T Recommendation Q.763 (1999) [24] clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.   # noqa: E501

        :param geodetic_information: The geodetic_information of this EutraLocation.
        :type geodetic_information: str
        """
        if geodetic_information is not None and not re.search(r'^[0-9A-F]{20}$', geodetic_information):  # noqa: E501
            raise ValueError("Invalid value for `geodetic_information`, must be a follow pattern or equal to `/^[0-9A-F]{20}$/`")  # noqa: E501

        self._geodetic_information = geodetic_information

    @property
    def global_ngenb_id(self):
        """Gets the global_ngenb_id of this EutraLocation.


        :return: The global_ngenb_id of this EutraLocation.
        :rtype: GlobalRanNodeId
        """
        return self._global_ngenb_id

    @global_ngenb_id.setter
    def global_ngenb_id(self, global_ngenb_id):
        """Sets the global_ngenb_id of this EutraLocation.


        :param global_ngenb_id: The global_ngenb_id of this EutraLocation.
        :type global_ngenb_id: GlobalRanNodeId
        """

        self._global_ngenb_id = global_ngenb_id

    @property
    def global_enb_id(self):
        """Gets the global_enb_id of this EutraLocation.


        :return: The global_enb_id of this EutraLocation.
        :rtype: GlobalRanNodeId
        """
        return self._global_enb_id

    @global_enb_id.setter
    def global_enb_id(self, global_enb_id):
        """Sets the global_enb_id of this EutraLocation.


        :param global_enb_id: The global_enb_id of this EutraLocation.
        :type global_enb_id: GlobalRanNodeId
        """

        self._global_enb_id = global_enb_id
