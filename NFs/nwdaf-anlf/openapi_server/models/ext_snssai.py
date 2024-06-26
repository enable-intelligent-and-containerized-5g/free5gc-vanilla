# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.sd_range import SdRange
import re
from openapi_server import util

from openapi_server.models.sd_range import SdRange  # noqa: E501
import re  # noqa: E501

class ExtSnssai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sst=None, sd=None, sd_ranges=None, wildcard_sd=None):  # noqa: E501
        """ExtSnssai - a model defined in OpenAPI

        :param sst: The sst of this ExtSnssai.  # noqa: E501
        :type sst: int
        :param sd: The sd of this ExtSnssai.  # noqa: E501
        :type sd: str
        :param sd_ranges: The sd_ranges of this ExtSnssai.  # noqa: E501
        :type sd_ranges: List[SdRange]
        :param wildcard_sd: The wildcard_sd of this ExtSnssai.  # noqa: E501
        :type wildcard_sd: bool
        """
        self.openapi_types = {
            'sst': int,
            'sd': str,
            'sd_ranges': List[SdRange],
            'wildcard_sd': bool
        }

        self.attribute_map = {
            'sst': 'sst',
            'sd': 'sd',
            'sd_ranges': 'sdRanges',
            'wildcard_sd': 'wildcardSd'
        }

        self.sst = sst
        self.sd = sd
        self.sd_ranges = sd_ranges
        self.wildcard_sd = wildcard_sd

    @classmethod
    def from_dict(cls, dikt) -> 'ExtSnssai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExtSnssai of this ExtSnssai.  # noqa: E501
        :rtype: ExtSnssai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sst(self):
        """Gets the sst of this ExtSnssai.

        Unsigned integer, within the range 0 to 255, representing the Slice/Service Type.  It indicates the expected Network Slice behaviour in terms of features and services. Values 0 to 127 correspond to the standardized SST range. Values 128 to 255 correspond  to the Operator-specific range. See clause 28.4.2 of 3GPP TS 23.003. Standardized values are defined in clause 5.15.2.2 of 3GPP TS 23.501.    # noqa: E501

        :return: The sst of this ExtSnssai.
        :rtype: int
        """
        return self._sst

    @sst.setter
    def sst(self, sst):
        """Sets the sst of this ExtSnssai.

        Unsigned integer, within the range 0 to 255, representing the Slice/Service Type.  It indicates the expected Network Slice behaviour in terms of features and services. Values 0 to 127 correspond to the standardized SST range. Values 128 to 255 correspond  to the Operator-specific range. See clause 28.4.2 of 3GPP TS 23.003. Standardized values are defined in clause 5.15.2.2 of 3GPP TS 23.501.    # noqa: E501

        :param sst: The sst of this ExtSnssai.
        :type sst: int
        """
        if sst is None:
            raise ValueError("Invalid value for `sst`, must not be `None`")  # noqa: E501
        if sst is not None and sst > 255:  # noqa: E501
            raise ValueError("Invalid value for `sst`, must be a value less than or equal to `255`")  # noqa: E501
        if sst is not None and sst < 0:  # noqa: E501
            raise ValueError("Invalid value for `sst`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sst = sst

    @property
    def sd(self):
        """Gets the sd of this ExtSnssai.

        3-octet string, representing the Slice Differentiator, in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the 4 most significant bits of the SD shall appear first in the string, and the character representing the 4 least significant bit of the SD shall appear last in the string. This is an optional parameter that complements the Slice/Service type(s) to allow to  differentiate amongst multiple Network Slices of the same Slice/Service type. This IE shall be absent if no SD value is associated with the SST.   # noqa: E501

        :return: The sd of this ExtSnssai.
        :rtype: str
        """
        return self._sd

    @sd.setter
    def sd(self, sd):
        """Sets the sd of this ExtSnssai.

        3-octet string, representing the Slice Differentiator, in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the 4 most significant bits of the SD shall appear first in the string, and the character representing the 4 least significant bit of the SD shall appear last in the string. This is an optional parameter that complements the Slice/Service type(s) to allow to  differentiate amongst multiple Network Slices of the same Slice/Service type. This IE shall be absent if no SD value is associated with the SST.   # noqa: E501

        :param sd: The sd of this ExtSnssai.
        :type sd: str
        """
        if sd is not None and not re.search(r'^[A-Fa-f0-9]{6}$', sd):  # noqa: E501
            raise ValueError("Invalid value for `sd`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{6}$/`")  # noqa: E501

        self._sd = sd

    @property
    def sd_ranges(self):
        """Gets the sd_ranges of this ExtSnssai.

        When present, it shall contain the range(s) of Slice Differentiator values supported for the Slice/Service Type value indicated in the sst attribute of the Snssai data type   # noqa: E501

        :return: The sd_ranges of this ExtSnssai.
        :rtype: List[SdRange]
        """
        return self._sd_ranges

    @sd_ranges.setter
    def sd_ranges(self, sd_ranges):
        """Sets the sd_ranges of this ExtSnssai.

        When present, it shall contain the range(s) of Slice Differentiator values supported for the Slice/Service Type value indicated in the sst attribute of the Snssai data type   # noqa: E501

        :param sd_ranges: The sd_ranges of this ExtSnssai.
        :type sd_ranges: List[SdRange]
        """
        if sd_ranges is not None and len(sd_ranges) < 1:
            raise ValueError("Invalid value for `sd_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._sd_ranges = sd_ranges

    @property
    def wildcard_sd(self):
        """Gets the wildcard_sd of this ExtSnssai.

        When present, it shall be set to true, to indicate that all SD values are supported for the Slice/Service Type value indicated in the sst attribute of the Snssai data type.   # noqa: E501

        :return: The wildcard_sd of this ExtSnssai.
        :rtype: bool
        """
        return self._wildcard_sd

    @wildcard_sd.setter
    def wildcard_sd(self, wildcard_sd):
        """Sets the wildcard_sd of this ExtSnssai.

        When present, it shall be set to true, to indicate that all SD values are supported for the Slice/Service Type value indicated in the sst attribute of the Snssai data type.   # noqa: E501

        :param wildcard_sd: The wildcard_sd of this ExtSnssai.
        :type wildcard_sd: bool
        """
        allowed_values = [true]  # noqa: E501
        if wildcard_sd not in allowed_values:
            raise ValueError(
                "Invalid value for `wildcard_sd` ({0}), must be one of {1}"
                .format(wildcard_sd, allowed_values)
            )

        self._wildcard_sd = wildcard_sd
