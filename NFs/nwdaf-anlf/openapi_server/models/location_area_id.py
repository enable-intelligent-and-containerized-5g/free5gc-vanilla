# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class LocationAreaId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, lac=None):  # noqa: E501
        """LocationAreaId - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this LocationAreaId.  # noqa: E501
        :type plmn_id: PlmnId
        :param lac: The lac of this LocationAreaId.  # noqa: E501
        :type lac: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'lac': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'lac': 'lac'
        }

        self.plmn_id = plmn_id
        self.lac = lac

    @classmethod
    def from_dict(cls, dikt) -> 'LocationAreaId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocationAreaId of this LocationAreaId.  # noqa: E501
        :rtype: LocationAreaId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this LocationAreaId.


        :return: The plmn_id of this LocationAreaId.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this LocationAreaId.


        :param plmn_id: The plmn_id of this LocationAreaId.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def lac(self):
        """Gets the lac of this LocationAreaId.

        Location Area Code.  # noqa: E501

        :return: The lac of this LocationAreaId.
        :rtype: str
        """
        return self._lac

    @lac.setter
    def lac(self, lac):
        """Sets the lac of this LocationAreaId.

        Location Area Code.  # noqa: E501

        :param lac: The lac of this LocationAreaId.
        :type lac: str
        """
        if lac is None:
            raise ValueError("Invalid value for `lac`, must not be `None`")  # noqa: E501
        if lac is not None and not re.search(r'^[A-Fa-f0-9]{4}$', lac):  # noqa: E501
            raise ValueError("Invalid value for `lac`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{4}$/`")  # noqa: E501

        self._lac = lac
