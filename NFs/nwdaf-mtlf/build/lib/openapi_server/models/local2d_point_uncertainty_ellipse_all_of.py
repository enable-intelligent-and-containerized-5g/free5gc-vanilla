# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.local_origin import LocalOrigin
from openapi_server.models.relative_cartesian_location import RelativeCartesianLocation
from openapi_server.models.uncertainty_ellipse import UncertaintyEllipse
from openapi_server import util

from openapi_server.models.local_origin import LocalOrigin  # noqa: E501
from openapi_server.models.relative_cartesian_location import RelativeCartesianLocation  # noqa: E501
from openapi_server.models.uncertainty_ellipse import UncertaintyEllipse  # noqa: E501

class Local2dPointUncertaintyEllipseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, local_origin=None, point=None, uncertainty_ellipse=None, confidence=None):  # noqa: E501
        """Local2dPointUncertaintyEllipseAllOf - a model defined in OpenAPI

        :param local_origin: The local_origin of this Local2dPointUncertaintyEllipseAllOf.  # noqa: E501
        :type local_origin: LocalOrigin
        :param point: The point of this Local2dPointUncertaintyEllipseAllOf.  # noqa: E501
        :type point: RelativeCartesianLocation
        :param uncertainty_ellipse: The uncertainty_ellipse of this Local2dPointUncertaintyEllipseAllOf.  # noqa: E501
        :type uncertainty_ellipse: UncertaintyEllipse
        :param confidence: The confidence of this Local2dPointUncertaintyEllipseAllOf.  # noqa: E501
        :type confidence: int
        """
        self.openapi_types = {
            'local_origin': LocalOrigin,
            'point': RelativeCartesianLocation,
            'uncertainty_ellipse': UncertaintyEllipse,
            'confidence': int
        }

        self.attribute_map = {
            'local_origin': 'localOrigin',
            'point': 'point',
            'uncertainty_ellipse': 'uncertaintyEllipse',
            'confidence': 'confidence'
        }

        self.local_origin = local_origin
        self.point = point
        self.uncertainty_ellipse = uncertainty_ellipse
        self.confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'Local2dPointUncertaintyEllipseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Local2dPointUncertaintyEllipse_allOf of this Local2dPointUncertaintyEllipseAllOf.  # noqa: E501
        :rtype: Local2dPointUncertaintyEllipseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def local_origin(self):
        """Gets the local_origin of this Local2dPointUncertaintyEllipseAllOf.


        :return: The local_origin of this Local2dPointUncertaintyEllipseAllOf.
        :rtype: LocalOrigin
        """
        return self._local_origin

    @local_origin.setter
    def local_origin(self, local_origin):
        """Sets the local_origin of this Local2dPointUncertaintyEllipseAllOf.


        :param local_origin: The local_origin of this Local2dPointUncertaintyEllipseAllOf.
        :type local_origin: LocalOrigin
        """
        if local_origin is None:
            raise ValueError("Invalid value for `local_origin`, must not be `None`")  # noqa: E501

        self._local_origin = local_origin

    @property
    def point(self):
        """Gets the point of this Local2dPointUncertaintyEllipseAllOf.


        :return: The point of this Local2dPointUncertaintyEllipseAllOf.
        :rtype: RelativeCartesianLocation
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this Local2dPointUncertaintyEllipseAllOf.


        :param point: The point of this Local2dPointUncertaintyEllipseAllOf.
        :type point: RelativeCartesianLocation
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

    @property
    def uncertainty_ellipse(self):
        """Gets the uncertainty_ellipse of this Local2dPointUncertaintyEllipseAllOf.


        :return: The uncertainty_ellipse of this Local2dPointUncertaintyEllipseAllOf.
        :rtype: UncertaintyEllipse
        """
        return self._uncertainty_ellipse

    @uncertainty_ellipse.setter
    def uncertainty_ellipse(self, uncertainty_ellipse):
        """Sets the uncertainty_ellipse of this Local2dPointUncertaintyEllipseAllOf.


        :param uncertainty_ellipse: The uncertainty_ellipse of this Local2dPointUncertaintyEllipseAllOf.
        :type uncertainty_ellipse: UncertaintyEllipse
        """
        if uncertainty_ellipse is None:
            raise ValueError("Invalid value for `uncertainty_ellipse`, must not be `None`")  # noqa: E501

        self._uncertainty_ellipse = uncertainty_ellipse

    @property
    def confidence(self):
        """Gets the confidence of this Local2dPointUncertaintyEllipseAllOf.

        Indicates value of confidence.  # noqa: E501

        :return: The confidence of this Local2dPointUncertaintyEllipseAllOf.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Local2dPointUncertaintyEllipseAllOf.

        Indicates value of confidence.  # noqa: E501

        :param confidence: The confidence of this Local2dPointUncertaintyEllipseAllOf.
        :type confidence: int
        """
        if confidence is None:
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501
        if confidence is not None and confidence > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence
