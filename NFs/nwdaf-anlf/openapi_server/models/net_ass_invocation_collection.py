# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NetAssInvocationCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, net_ass_invocs=None):  # noqa: E501
        """NetAssInvocationCollection - a model defined in OpenAPI

        :param net_ass_invocs: The net_ass_invocs of this NetAssInvocationCollection.  # noqa: E501
        :type net_ass_invocs: List[str]
        """
        self.openapi_types = {
            'net_ass_invocs': List[str]
        }

        self.attribute_map = {
            'net_ass_invocs': 'netAssInvocs'
        }

        self.net_ass_invocs = net_ass_invocs

    @classmethod
    def from_dict(cls, dikt) -> 'NetAssInvocationCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetAssInvocationCollection of this NetAssInvocationCollection.  # noqa: E501
        :rtype: NetAssInvocationCollection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def net_ass_invocs(self):
        """Gets the net_ass_invocs of this NetAssInvocationCollection.


        :return: The net_ass_invocs of this NetAssInvocationCollection.
        :rtype: List[str]
        """
        return self._net_ass_invocs

    @net_ass_invocs.setter
    def net_ass_invocs(self, net_ass_invocs):
        """Sets the net_ass_invocs of this NetAssInvocationCollection.


        :param net_ass_invocs: The net_ass_invocs of this NetAssInvocationCollection.
        :type net_ass_invocs: List[str]
        """
        if net_ass_invocs is None:
            raise ValueError("Invalid value for `net_ass_invocs`, must not be `None`")  # noqa: E501
        if net_ass_invocs is not None and len(net_ass_invocs) < 1:
            raise ValueError("Invalid value for `net_ass_invocs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._net_ass_invocs = net_ass_invocs