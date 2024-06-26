# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ContextInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, orig_headers=None, request_headers=None):  # noqa: E501
        """ContextInfo - a model defined in OpenAPI

        :param orig_headers: The orig_headers of this ContextInfo.  # noqa: E501
        :type orig_headers: List[str]
        :param request_headers: The request_headers of this ContextInfo.  # noqa: E501
        :type request_headers: List[str]
        """
        self.openapi_types = {
            'orig_headers': List[str],
            'request_headers': List[str]
        }

        self.attribute_map = {
            'orig_headers': 'origHeaders',
            'request_headers': 'requestHeaders'
        }

        self.orig_headers = orig_headers
        self.request_headers = request_headers

    @classmethod
    def from_dict(cls, dikt) -> 'ContextInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ContextInfo of this ContextInfo.  # noqa: E501
        :rtype: ContextInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orig_headers(self):
        """Gets the orig_headers of this ContextInfo.


        :return: The orig_headers of this ContextInfo.
        :rtype: List[str]
        """
        return self._orig_headers

    @orig_headers.setter
    def orig_headers(self, orig_headers):
        """Sets the orig_headers of this ContextInfo.


        :param orig_headers: The orig_headers of this ContextInfo.
        :type orig_headers: List[str]
        """
        if orig_headers is not None and len(orig_headers) < 1:
            raise ValueError("Invalid value for `orig_headers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._orig_headers = orig_headers

    @property
    def request_headers(self):
        """Gets the request_headers of this ContextInfo.


        :return: The request_headers of this ContextInfo.
        :rtype: List[str]
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this ContextInfo.


        :param request_headers: The request_headers of this ContextInfo.
        :type request_headers: List[str]
        """
        if request_headers is not None and len(request_headers) < 1:
            raise ValueError("Invalid value for `request_headers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._request_headers = request_headers
