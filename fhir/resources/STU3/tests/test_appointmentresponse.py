# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import appointmentresponse
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AppointmentResponse", js["resourceType"])
        return appointmentresponse.AppointmentResponse(js)

    def testAppointmentResponse1(self):
        inst = self.instantiate_from("appointmentresponse-example-req.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse1(inst)

        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse1(inst2)

    def implAppointmentResponse1(self, inst):
        self.assertEqual(force_bytes(inst.comment), force_bytes("can't we try for this time, can't do mornings"))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T13:30:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T13:30:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("exampleresp"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/sampleappointmentresponse-identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("response123"))
        self.assertEqual(force_bytes(inst.participantStatus), force_bytes("tentative"))
        self.assertEqual(force_bytes(inst.participantType[0].coding[0].code), force_bytes("ATND"))
        self.assertEqual(force_bytes(inst.participantType[0].coding[0].system), force_bytes("http://hl7.org/fhir/v3/ParticipationType"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T13:15:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T13:15:00Z")
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testAppointmentResponse2(self):
        inst = self.instantiate_from("appointmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse2(inst)

        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse2(inst2)

    def implAppointmentResponse2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.participantStatus), force_bytes("accepted"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

