# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class BwRequirement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id=None, mar_bw_dl=None, mar_bw_ul=None, mir_bw_dl=None, mir_bw_ul=None):  # noqa: E501
        """BwRequirement - a model defined in OpenAPI

        :param app_id: The app_id of this BwRequirement.  # noqa: E501
        :type app_id: str
        :param mar_bw_dl: The mar_bw_dl of this BwRequirement.  # noqa: E501
        :type mar_bw_dl: str
        :param mar_bw_ul: The mar_bw_ul of this BwRequirement.  # noqa: E501
        :type mar_bw_ul: str
        :param mir_bw_dl: The mir_bw_dl of this BwRequirement.  # noqa: E501
        :type mir_bw_dl: str
        :param mir_bw_ul: The mir_bw_ul of this BwRequirement.  # noqa: E501
        :type mir_bw_ul: str
        """
        self.openapi_types = {
            'app_id': str,
            'mar_bw_dl': str,
            'mar_bw_ul': str,
            'mir_bw_dl': str,
            'mir_bw_ul': str
        }

        self.attribute_map = {
            'app_id': 'appId',
            'mar_bw_dl': 'marBwDl',
            'mar_bw_ul': 'marBwUl',
            'mir_bw_dl': 'mirBwDl',
            'mir_bw_ul': 'mirBwUl'
        }

        self.app_id = app_id
        self.mar_bw_dl = mar_bw_dl
        self.mar_bw_ul = mar_bw_ul
        self.mir_bw_dl = mir_bw_dl
        self.mir_bw_ul = mir_bw_ul

    @classmethod
    def from_dict(cls, dikt) -> 'BwRequirement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BwRequirement of this BwRequirement.  # noqa: E501
        :rtype: BwRequirement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this BwRequirement.

        String providing an application identifier.  # noqa: E501

        :return: The app_id of this BwRequirement.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this BwRequirement.

        String providing an application identifier.  # noqa: E501

        :param app_id: The app_id of this BwRequirement.
        :type app_id: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def mar_bw_dl(self):
        """Gets the mar_bw_dl of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The mar_bw_dl of this BwRequirement.
        :rtype: str
        """
        return self._mar_bw_dl

    @mar_bw_dl.setter
    def mar_bw_dl(self, mar_bw_dl):
        """Sets the mar_bw_dl of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param mar_bw_dl: The mar_bw_dl of this BwRequirement.
        :type mar_bw_dl: str
        """
        if mar_bw_dl is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', mar_bw_dl):  # noqa: E501
            raise ValueError("Invalid value for `mar_bw_dl`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._mar_bw_dl = mar_bw_dl

    @property
    def mar_bw_ul(self):
        """Gets the mar_bw_ul of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The mar_bw_ul of this BwRequirement.
        :rtype: str
        """
        return self._mar_bw_ul

    @mar_bw_ul.setter
    def mar_bw_ul(self, mar_bw_ul):
        """Sets the mar_bw_ul of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param mar_bw_ul: The mar_bw_ul of this BwRequirement.
        :type mar_bw_ul: str
        """
        if mar_bw_ul is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', mar_bw_ul):  # noqa: E501
            raise ValueError("Invalid value for `mar_bw_ul`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._mar_bw_ul = mar_bw_ul

    @property
    def mir_bw_dl(self):
        """Gets the mir_bw_dl of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The mir_bw_dl of this BwRequirement.
        :rtype: str
        """
        return self._mir_bw_dl

    @mir_bw_dl.setter
    def mir_bw_dl(self, mir_bw_dl):
        """Sets the mir_bw_dl of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param mir_bw_dl: The mir_bw_dl of this BwRequirement.
        :type mir_bw_dl: str
        """
        if mir_bw_dl is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', mir_bw_dl):  # noqa: E501
            raise ValueError("Invalid value for `mir_bw_dl`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._mir_bw_dl = mir_bw_dl

    @property
    def mir_bw_ul(self):
        """Gets the mir_bw_ul of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The mir_bw_ul of this BwRequirement.
        :rtype: str
        """
        return self._mir_bw_ul

    @mir_bw_ul.setter
    def mir_bw_ul(self, mir_bw_ul):
        """Sets the mir_bw_ul of this BwRequirement.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param mir_bw_ul: The mir_bw_ul of this BwRequirement.
        :type mir_bw_ul: str
        """
        if mir_bw_ul is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', mir_bw_ul):  # noqa: E501
            raise ValueError("Invalid value for `mir_bw_ul`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._mir_bw_ul = mir_bw_ul
