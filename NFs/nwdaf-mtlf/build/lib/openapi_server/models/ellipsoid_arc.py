# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.gad_shape import GADShape
from openapi_server.models.geographical_coordinates import GeographicalCoordinates
from openapi_server.models.supported_gad_shapes import SupportedGADShapes
from openapi_server import util

from openapi_server.models.gad_shape import GADShape  # noqa: E501
from openapi_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501
from openapi_server.models.supported_gad_shapes import SupportedGADShapes  # noqa: E501

class EllipsoidArc(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, shape=None, point=None, inner_radius=None, uncertainty_radius=None, offset_angle=None, included_angle=None, confidence=None):  # noqa: E501
        """EllipsoidArc - a model defined in OpenAPI

        :param shape: The shape of this EllipsoidArc.  # noqa: E501
        :type shape: SupportedGADShapes
        :param point: The point of this EllipsoidArc.  # noqa: E501
        :type point: GeographicalCoordinates
        :param inner_radius: The inner_radius of this EllipsoidArc.  # noqa: E501
        :type inner_radius: int
        :param uncertainty_radius: The uncertainty_radius of this EllipsoidArc.  # noqa: E501
        :type uncertainty_radius: float
        :param offset_angle: The offset_angle of this EllipsoidArc.  # noqa: E501
        :type offset_angle: int
        :param included_angle: The included_angle of this EllipsoidArc.  # noqa: E501
        :type included_angle: int
        :param confidence: The confidence of this EllipsoidArc.  # noqa: E501
        :type confidence: int
        """
        self.openapi_types = {
            'shape': SupportedGADShapes,
            'point': GeographicalCoordinates,
            'inner_radius': int,
            'uncertainty_radius': float,
            'offset_angle': int,
            'included_angle': int,
            'confidence': int
        }

        self.attribute_map = {
            'shape': 'shape',
            'point': 'point',
            'inner_radius': 'innerRadius',
            'uncertainty_radius': 'uncertaintyRadius',
            'offset_angle': 'offsetAngle',
            'included_angle': 'includedAngle',
            'confidence': 'confidence'
        }

        self.shape = shape
        self.point = point
        self.inner_radius = inner_radius
        self.uncertainty_radius = uncertainty_radius
        self.offset_angle = offset_angle
        self.included_angle = included_angle
        self.confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'EllipsoidArc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EllipsoidArc of this EllipsoidArc.  # noqa: E501
        :rtype: EllipsoidArc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shape(self):
        """Gets the shape of this EllipsoidArc.


        :return: The shape of this EllipsoidArc.
        :rtype: SupportedGADShapes
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this EllipsoidArc.


        :param shape: The shape of this EllipsoidArc.
        :type shape: SupportedGADShapes
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def point(self):
        """Gets the point of this EllipsoidArc.


        :return: The point of this EllipsoidArc.
        :rtype: GeographicalCoordinates
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this EllipsoidArc.


        :param point: The point of this EllipsoidArc.
        :type point: GeographicalCoordinates
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

    @property
    def inner_radius(self):
        """Gets the inner_radius of this EllipsoidArc.

        Indicates value of the inner radius.  # noqa: E501

        :return: The inner_radius of this EllipsoidArc.
        :rtype: int
        """
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, inner_radius):
        """Sets the inner_radius of this EllipsoidArc.

        Indicates value of the inner radius.  # noqa: E501

        :param inner_radius: The inner_radius of this EllipsoidArc.
        :type inner_radius: int
        """
        if inner_radius is None:
            raise ValueError("Invalid value for `inner_radius`, must not be `None`")  # noqa: E501
        if inner_radius is not None and inner_radius > 327675:  # noqa: E501
            raise ValueError("Invalid value for `inner_radius`, must be a value less than or equal to `327675`")  # noqa: E501
        if inner_radius is not None and inner_radius < 0:  # noqa: E501
            raise ValueError("Invalid value for `inner_radius`, must be a value greater than or equal to `0`")  # noqa: E501

        self._inner_radius = inner_radius

    @property
    def uncertainty_radius(self):
        """Gets the uncertainty_radius of this EllipsoidArc.

        Indicates value of uncertainty.  # noqa: E501

        :return: The uncertainty_radius of this EllipsoidArc.
        :rtype: float
        """
        return self._uncertainty_radius

    @uncertainty_radius.setter
    def uncertainty_radius(self, uncertainty_radius):
        """Sets the uncertainty_radius of this EllipsoidArc.

        Indicates value of uncertainty.  # noqa: E501

        :param uncertainty_radius: The uncertainty_radius of this EllipsoidArc.
        :type uncertainty_radius: float
        """
        if uncertainty_radius is None:
            raise ValueError("Invalid value for `uncertainty_radius`, must not be `None`")  # noqa: E501
        if uncertainty_radius is not None and uncertainty_radius < 0:  # noqa: E501
            raise ValueError("Invalid value for `uncertainty_radius`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uncertainty_radius = uncertainty_radius

    @property
    def offset_angle(self):
        """Gets the offset_angle of this EllipsoidArc.

        Indicates value of angle.  # noqa: E501

        :return: The offset_angle of this EllipsoidArc.
        :rtype: int
        """
        return self._offset_angle

    @offset_angle.setter
    def offset_angle(self, offset_angle):
        """Sets the offset_angle of this EllipsoidArc.

        Indicates value of angle.  # noqa: E501

        :param offset_angle: The offset_angle of this EllipsoidArc.
        :type offset_angle: int
        """
        if offset_angle is None:
            raise ValueError("Invalid value for `offset_angle`, must not be `None`")  # noqa: E501
        if offset_angle is not None and offset_angle > 360:  # noqa: E501
            raise ValueError("Invalid value for `offset_angle`, must be a value less than or equal to `360`")  # noqa: E501
        if offset_angle is not None and offset_angle < 0:  # noqa: E501
            raise ValueError("Invalid value for `offset_angle`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset_angle = offset_angle

    @property
    def included_angle(self):
        """Gets the included_angle of this EllipsoidArc.

        Indicates value of angle.  # noqa: E501

        :return: The included_angle of this EllipsoidArc.
        :rtype: int
        """
        return self._included_angle

    @included_angle.setter
    def included_angle(self, included_angle):
        """Sets the included_angle of this EllipsoidArc.

        Indicates value of angle.  # noqa: E501

        :param included_angle: The included_angle of this EllipsoidArc.
        :type included_angle: int
        """
        if included_angle is None:
            raise ValueError("Invalid value for `included_angle`, must not be `None`")  # noqa: E501
        if included_angle is not None and included_angle > 360:  # noqa: E501
            raise ValueError("Invalid value for `included_angle`, must be a value less than or equal to `360`")  # noqa: E501
        if included_angle is not None and included_angle < 0:  # noqa: E501
            raise ValueError("Invalid value for `included_angle`, must be a value greater than or equal to `0`")  # noqa: E501

        self._included_angle = included_angle

    @property
    def confidence(self):
        """Gets the confidence of this EllipsoidArc.

        Indicates value of confidence.  # noqa: E501

        :return: The confidence of this EllipsoidArc.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this EllipsoidArc.

        Indicates value of confidence.  # noqa: E501

        :param confidence: The confidence of this EllipsoidArc.
        :type confidence: int
        """
        if confidence is None:
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501
        if confidence is not None and confidence > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence
