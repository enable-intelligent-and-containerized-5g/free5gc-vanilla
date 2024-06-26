# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ng_ap_cause import NgApCause
from openapi_server import util

from openapi_server.models.ng_ap_cause import NgApCause  # noqa: E501

class CommunicationFailure(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nas_release_code=None, ran_release_code=None):  # noqa: E501
        """CommunicationFailure - a model defined in OpenAPI

        :param nas_release_code: The nas_release_code of this CommunicationFailure.  # noqa: E501
        :type nas_release_code: str
        :param ran_release_code: The ran_release_code of this CommunicationFailure.  # noqa: E501
        :type ran_release_code: NgApCause
        """
        self.openapi_types = {
            'nas_release_code': str,
            'ran_release_code': NgApCause
        }

        self.attribute_map = {
            'nas_release_code': 'nasReleaseCode',
            'ran_release_code': 'ranReleaseCode'
        }

        self.nas_release_code = nas_release_code
        self.ran_release_code = ran_release_code

    @classmethod
    def from_dict(cls, dikt) -> 'CommunicationFailure':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommunicationFailure of this CommunicationFailure.  # noqa: E501
        :rtype: CommunicationFailure
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nas_release_code(self):
        """Gets the nas_release_code of this CommunicationFailure.


        :return: The nas_release_code of this CommunicationFailure.
        :rtype: str
        """
        return self._nas_release_code

    @nas_release_code.setter
    def nas_release_code(self, nas_release_code):
        """Sets the nas_release_code of this CommunicationFailure.


        :param nas_release_code: The nas_release_code of this CommunicationFailure.
        :type nas_release_code: str
        """

        self._nas_release_code = nas_release_code

    @property
    def ran_release_code(self):
        """Gets the ran_release_code of this CommunicationFailure.


        :return: The ran_release_code of this CommunicationFailure.
        :rtype: NgApCause
        """
        return self._ran_release_code

    @ran_release_code.setter
    def ran_release_code(self, ran_release_code):
        """Sets the ran_release_code of this CommunicationFailure.


        :param ran_release_code: The ran_release_code of this CommunicationFailure.
        :type ran_release_code: NgApCause
        """

        self._ran_release_code = ran_release_code
