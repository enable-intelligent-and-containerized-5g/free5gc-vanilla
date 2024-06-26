# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CivicAddress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, country=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, prd=None, pod=None, sts=None, hno=None, hns=None, lmk=None, loc=None, nam=None, pc=None, bld=None, unit=None, flr=None, room=None, plc=None, pcn=None, pobox=None, addcode=None, seat=None, rd=None, rdsec=None, rdbr=None, rdsubbr=None, prm=None, pom=None, usage_rules=None, method=None, provided_by=None):  # noqa: E501
        """CivicAddress - a model defined in OpenAPI

        :param country: The country of this CivicAddress.  # noqa: E501
        :type country: str
        :param a1: The a1 of this CivicAddress.  # noqa: E501
        :type a1: str
        :param a2: The a2 of this CivicAddress.  # noqa: E501
        :type a2: str
        :param a3: The a3 of this CivicAddress.  # noqa: E501
        :type a3: str
        :param a4: The a4 of this CivicAddress.  # noqa: E501
        :type a4: str
        :param a5: The a5 of this CivicAddress.  # noqa: E501
        :type a5: str
        :param a6: The a6 of this CivicAddress.  # noqa: E501
        :type a6: str
        :param prd: The prd of this CivicAddress.  # noqa: E501
        :type prd: str
        :param pod: The pod of this CivicAddress.  # noqa: E501
        :type pod: str
        :param sts: The sts of this CivicAddress.  # noqa: E501
        :type sts: str
        :param hno: The hno of this CivicAddress.  # noqa: E501
        :type hno: str
        :param hns: The hns of this CivicAddress.  # noqa: E501
        :type hns: str
        :param lmk: The lmk of this CivicAddress.  # noqa: E501
        :type lmk: str
        :param loc: The loc of this CivicAddress.  # noqa: E501
        :type loc: str
        :param nam: The nam of this CivicAddress.  # noqa: E501
        :type nam: str
        :param pc: The pc of this CivicAddress.  # noqa: E501
        :type pc: str
        :param bld: The bld of this CivicAddress.  # noqa: E501
        :type bld: str
        :param unit: The unit of this CivicAddress.  # noqa: E501
        :type unit: str
        :param flr: The flr of this CivicAddress.  # noqa: E501
        :type flr: str
        :param room: The room of this CivicAddress.  # noqa: E501
        :type room: str
        :param plc: The plc of this CivicAddress.  # noqa: E501
        :type plc: str
        :param pcn: The pcn of this CivicAddress.  # noqa: E501
        :type pcn: str
        :param pobox: The pobox of this CivicAddress.  # noqa: E501
        :type pobox: str
        :param addcode: The addcode of this CivicAddress.  # noqa: E501
        :type addcode: str
        :param seat: The seat of this CivicAddress.  # noqa: E501
        :type seat: str
        :param rd: The rd of this CivicAddress.  # noqa: E501
        :type rd: str
        :param rdsec: The rdsec of this CivicAddress.  # noqa: E501
        :type rdsec: str
        :param rdbr: The rdbr of this CivicAddress.  # noqa: E501
        :type rdbr: str
        :param rdsubbr: The rdsubbr of this CivicAddress.  # noqa: E501
        :type rdsubbr: str
        :param prm: The prm of this CivicAddress.  # noqa: E501
        :type prm: str
        :param pom: The pom of this CivicAddress.  # noqa: E501
        :type pom: str
        :param usage_rules: The usage_rules of this CivicAddress.  # noqa: E501
        :type usage_rules: str
        :param method: The method of this CivicAddress.  # noqa: E501
        :type method: str
        :param provided_by: The provided_by of this CivicAddress.  # noqa: E501
        :type provided_by: str
        """
        self.openapi_types = {
            'country': str,
            'a1': str,
            'a2': str,
            'a3': str,
            'a4': str,
            'a5': str,
            'a6': str,
            'prd': str,
            'pod': str,
            'sts': str,
            'hno': str,
            'hns': str,
            'lmk': str,
            'loc': str,
            'nam': str,
            'pc': str,
            'bld': str,
            'unit': str,
            'flr': str,
            'room': str,
            'plc': str,
            'pcn': str,
            'pobox': str,
            'addcode': str,
            'seat': str,
            'rd': str,
            'rdsec': str,
            'rdbr': str,
            'rdsubbr': str,
            'prm': str,
            'pom': str,
            'usage_rules': str,
            'method': str,
            'provided_by': str
        }

        self.attribute_map = {
            'country': 'country',
            'a1': 'A1',
            'a2': 'A2',
            'a3': 'A3',
            'a4': 'A4',
            'a5': 'A5',
            'a6': 'A6',
            'prd': 'PRD',
            'pod': 'POD',
            'sts': 'STS',
            'hno': 'HNO',
            'hns': 'HNS',
            'lmk': 'LMK',
            'loc': 'LOC',
            'nam': 'NAM',
            'pc': 'PC',
            'bld': 'BLD',
            'unit': 'UNIT',
            'flr': 'FLR',
            'room': 'ROOM',
            'plc': 'PLC',
            'pcn': 'PCN',
            'pobox': 'POBOX',
            'addcode': 'ADDCODE',
            'seat': 'SEAT',
            'rd': 'RD',
            'rdsec': 'RDSEC',
            'rdbr': 'RDBR',
            'rdsubbr': 'RDSUBBR',
            'prm': 'PRM',
            'pom': 'POM',
            'usage_rules': 'usageRules',
            'method': 'method',
            'provided_by': 'providedBy'
        }

        self.country = country
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.prd = prd
        self.pod = pod
        self.sts = sts
        self.hno = hno
        self.hns = hns
        self.lmk = lmk
        self.loc = loc
        self.nam = nam
        self.pc = pc
        self.bld = bld
        self.unit = unit
        self.flr = flr
        self.room = room
        self.plc = plc
        self.pcn = pcn
        self.pobox = pobox
        self.addcode = addcode
        self.seat = seat
        self.rd = rd
        self.rdsec = rdsec
        self.rdbr = rdbr
        self.rdsubbr = rdsubbr
        self.prm = prm
        self.pom = pom
        self.usage_rules = usage_rules
        self.method = method
        self.provided_by = provided_by

    @classmethod
    def from_dict(cls, dikt) -> 'CivicAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CivicAddress of this CivicAddress.  # noqa: E501
        :rtype: CivicAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country(self):
        """Gets the country of this CivicAddress.


        :return: The country of this CivicAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CivicAddress.


        :param country: The country of this CivicAddress.
        :type country: str
        """

        self._country = country

    @property
    def a1(self):
        """Gets the a1 of this CivicAddress.


        :return: The a1 of this CivicAddress.
        :rtype: str
        """
        return self._a1

    @a1.setter
    def a1(self, a1):
        """Sets the a1 of this CivicAddress.


        :param a1: The a1 of this CivicAddress.
        :type a1: str
        """

        self._a1 = a1

    @property
    def a2(self):
        """Gets the a2 of this CivicAddress.


        :return: The a2 of this CivicAddress.
        :rtype: str
        """
        return self._a2

    @a2.setter
    def a2(self, a2):
        """Sets the a2 of this CivicAddress.


        :param a2: The a2 of this CivicAddress.
        :type a2: str
        """

        self._a2 = a2

    @property
    def a3(self):
        """Gets the a3 of this CivicAddress.


        :return: The a3 of this CivicAddress.
        :rtype: str
        """
        return self._a3

    @a3.setter
    def a3(self, a3):
        """Sets the a3 of this CivicAddress.


        :param a3: The a3 of this CivicAddress.
        :type a3: str
        """

        self._a3 = a3

    @property
    def a4(self):
        """Gets the a4 of this CivicAddress.


        :return: The a4 of this CivicAddress.
        :rtype: str
        """
        return self._a4

    @a4.setter
    def a4(self, a4):
        """Sets the a4 of this CivicAddress.


        :param a4: The a4 of this CivicAddress.
        :type a4: str
        """

        self._a4 = a4

    @property
    def a5(self):
        """Gets the a5 of this CivicAddress.


        :return: The a5 of this CivicAddress.
        :rtype: str
        """
        return self._a5

    @a5.setter
    def a5(self, a5):
        """Sets the a5 of this CivicAddress.


        :param a5: The a5 of this CivicAddress.
        :type a5: str
        """

        self._a5 = a5

    @property
    def a6(self):
        """Gets the a6 of this CivicAddress.


        :return: The a6 of this CivicAddress.
        :rtype: str
        """
        return self._a6

    @a6.setter
    def a6(self, a6):
        """Sets the a6 of this CivicAddress.


        :param a6: The a6 of this CivicAddress.
        :type a6: str
        """

        self._a6 = a6

    @property
    def prd(self):
        """Gets the prd of this CivicAddress.


        :return: The prd of this CivicAddress.
        :rtype: str
        """
        return self._prd

    @prd.setter
    def prd(self, prd):
        """Sets the prd of this CivicAddress.


        :param prd: The prd of this CivicAddress.
        :type prd: str
        """

        self._prd = prd

    @property
    def pod(self):
        """Gets the pod of this CivicAddress.


        :return: The pod of this CivicAddress.
        :rtype: str
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """Sets the pod of this CivicAddress.


        :param pod: The pod of this CivicAddress.
        :type pod: str
        """

        self._pod = pod

    @property
    def sts(self):
        """Gets the sts of this CivicAddress.


        :return: The sts of this CivicAddress.
        :rtype: str
        """
        return self._sts

    @sts.setter
    def sts(self, sts):
        """Sets the sts of this CivicAddress.


        :param sts: The sts of this CivicAddress.
        :type sts: str
        """

        self._sts = sts

    @property
    def hno(self):
        """Gets the hno of this CivicAddress.


        :return: The hno of this CivicAddress.
        :rtype: str
        """
        return self._hno

    @hno.setter
    def hno(self, hno):
        """Sets the hno of this CivicAddress.


        :param hno: The hno of this CivicAddress.
        :type hno: str
        """

        self._hno = hno

    @property
    def hns(self):
        """Gets the hns of this CivicAddress.


        :return: The hns of this CivicAddress.
        :rtype: str
        """
        return self._hns

    @hns.setter
    def hns(self, hns):
        """Sets the hns of this CivicAddress.


        :param hns: The hns of this CivicAddress.
        :type hns: str
        """

        self._hns = hns

    @property
    def lmk(self):
        """Gets the lmk of this CivicAddress.


        :return: The lmk of this CivicAddress.
        :rtype: str
        """
        return self._lmk

    @lmk.setter
    def lmk(self, lmk):
        """Sets the lmk of this CivicAddress.


        :param lmk: The lmk of this CivicAddress.
        :type lmk: str
        """

        self._lmk = lmk

    @property
    def loc(self):
        """Gets the loc of this CivicAddress.


        :return: The loc of this CivicAddress.
        :rtype: str
        """
        return self._loc

    @loc.setter
    def loc(self, loc):
        """Sets the loc of this CivicAddress.


        :param loc: The loc of this CivicAddress.
        :type loc: str
        """

        self._loc = loc

    @property
    def nam(self):
        """Gets the nam of this CivicAddress.


        :return: The nam of this CivicAddress.
        :rtype: str
        """
        return self._nam

    @nam.setter
    def nam(self, nam):
        """Sets the nam of this CivicAddress.


        :param nam: The nam of this CivicAddress.
        :type nam: str
        """

        self._nam = nam

    @property
    def pc(self):
        """Gets the pc of this CivicAddress.


        :return: The pc of this CivicAddress.
        :rtype: str
        """
        return self._pc

    @pc.setter
    def pc(self, pc):
        """Sets the pc of this CivicAddress.


        :param pc: The pc of this CivicAddress.
        :type pc: str
        """

        self._pc = pc

    @property
    def bld(self):
        """Gets the bld of this CivicAddress.


        :return: The bld of this CivicAddress.
        :rtype: str
        """
        return self._bld

    @bld.setter
    def bld(self, bld):
        """Sets the bld of this CivicAddress.


        :param bld: The bld of this CivicAddress.
        :type bld: str
        """

        self._bld = bld

    @property
    def unit(self):
        """Gets the unit of this CivicAddress.


        :return: The unit of this CivicAddress.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CivicAddress.


        :param unit: The unit of this CivicAddress.
        :type unit: str
        """

        self._unit = unit

    @property
    def flr(self):
        """Gets the flr of this CivicAddress.


        :return: The flr of this CivicAddress.
        :rtype: str
        """
        return self._flr

    @flr.setter
    def flr(self, flr):
        """Sets the flr of this CivicAddress.


        :param flr: The flr of this CivicAddress.
        :type flr: str
        """

        self._flr = flr

    @property
    def room(self):
        """Gets the room of this CivicAddress.


        :return: The room of this CivicAddress.
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this CivicAddress.


        :param room: The room of this CivicAddress.
        :type room: str
        """

        self._room = room

    @property
    def plc(self):
        """Gets the plc of this CivicAddress.


        :return: The plc of this CivicAddress.
        :rtype: str
        """
        return self._plc

    @plc.setter
    def plc(self, plc):
        """Sets the plc of this CivicAddress.


        :param plc: The plc of this CivicAddress.
        :type plc: str
        """

        self._plc = plc

    @property
    def pcn(self):
        """Gets the pcn of this CivicAddress.


        :return: The pcn of this CivicAddress.
        :rtype: str
        """
        return self._pcn

    @pcn.setter
    def pcn(self, pcn):
        """Sets the pcn of this CivicAddress.


        :param pcn: The pcn of this CivicAddress.
        :type pcn: str
        """

        self._pcn = pcn

    @property
    def pobox(self):
        """Gets the pobox of this CivicAddress.


        :return: The pobox of this CivicAddress.
        :rtype: str
        """
        return self._pobox

    @pobox.setter
    def pobox(self, pobox):
        """Sets the pobox of this CivicAddress.


        :param pobox: The pobox of this CivicAddress.
        :type pobox: str
        """

        self._pobox = pobox

    @property
    def addcode(self):
        """Gets the addcode of this CivicAddress.


        :return: The addcode of this CivicAddress.
        :rtype: str
        """
        return self._addcode

    @addcode.setter
    def addcode(self, addcode):
        """Sets the addcode of this CivicAddress.


        :param addcode: The addcode of this CivicAddress.
        :type addcode: str
        """

        self._addcode = addcode

    @property
    def seat(self):
        """Gets the seat of this CivicAddress.


        :return: The seat of this CivicAddress.
        :rtype: str
        """
        return self._seat

    @seat.setter
    def seat(self, seat):
        """Sets the seat of this CivicAddress.


        :param seat: The seat of this CivicAddress.
        :type seat: str
        """

        self._seat = seat

    @property
    def rd(self):
        """Gets the rd of this CivicAddress.


        :return: The rd of this CivicAddress.
        :rtype: str
        """
        return self._rd

    @rd.setter
    def rd(self, rd):
        """Sets the rd of this CivicAddress.


        :param rd: The rd of this CivicAddress.
        :type rd: str
        """

        self._rd = rd

    @property
    def rdsec(self):
        """Gets the rdsec of this CivicAddress.


        :return: The rdsec of this CivicAddress.
        :rtype: str
        """
        return self._rdsec

    @rdsec.setter
    def rdsec(self, rdsec):
        """Sets the rdsec of this CivicAddress.


        :param rdsec: The rdsec of this CivicAddress.
        :type rdsec: str
        """

        self._rdsec = rdsec

    @property
    def rdbr(self):
        """Gets the rdbr of this CivicAddress.


        :return: The rdbr of this CivicAddress.
        :rtype: str
        """
        return self._rdbr

    @rdbr.setter
    def rdbr(self, rdbr):
        """Sets the rdbr of this CivicAddress.


        :param rdbr: The rdbr of this CivicAddress.
        :type rdbr: str
        """

        self._rdbr = rdbr

    @property
    def rdsubbr(self):
        """Gets the rdsubbr of this CivicAddress.


        :return: The rdsubbr of this CivicAddress.
        :rtype: str
        """
        return self._rdsubbr

    @rdsubbr.setter
    def rdsubbr(self, rdsubbr):
        """Sets the rdsubbr of this CivicAddress.


        :param rdsubbr: The rdsubbr of this CivicAddress.
        :type rdsubbr: str
        """

        self._rdsubbr = rdsubbr

    @property
    def prm(self):
        """Gets the prm of this CivicAddress.


        :return: The prm of this CivicAddress.
        :rtype: str
        """
        return self._prm

    @prm.setter
    def prm(self, prm):
        """Sets the prm of this CivicAddress.


        :param prm: The prm of this CivicAddress.
        :type prm: str
        """

        self._prm = prm

    @property
    def pom(self):
        """Gets the pom of this CivicAddress.


        :return: The pom of this CivicAddress.
        :rtype: str
        """
        return self._pom

    @pom.setter
    def pom(self, pom):
        """Sets the pom of this CivicAddress.


        :param pom: The pom of this CivicAddress.
        :type pom: str
        """

        self._pom = pom

    @property
    def usage_rules(self):
        """Gets the usage_rules of this CivicAddress.


        :return: The usage_rules of this CivicAddress.
        :rtype: str
        """
        return self._usage_rules

    @usage_rules.setter
    def usage_rules(self, usage_rules):
        """Sets the usage_rules of this CivicAddress.


        :param usage_rules: The usage_rules of this CivicAddress.
        :type usage_rules: str
        """

        self._usage_rules = usage_rules

    @property
    def method(self):
        """Gets the method of this CivicAddress.


        :return: The method of this CivicAddress.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CivicAddress.


        :param method: The method of this CivicAddress.
        :type method: str
        """

        self._method = method

    @property
    def provided_by(self):
        """Gets the provided_by of this CivicAddress.


        :return: The provided_by of this CivicAddress.
        :rtype: str
        """
        return self._provided_by

    @provided_by.setter
    def provided_by(self, provided_by):
        """Sets the provided_by of this CivicAddress.


        :param provided_by: The provided_by of this CivicAddress.
        :type provided_by: str
        """

        self._provided_by = provided_by
