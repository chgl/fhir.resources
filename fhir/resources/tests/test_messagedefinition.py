# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import messagedefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageDefinition", js["resourceType"])
        return messagedefinition.MessageDefinition(js)

    def testMessageDefinition1(self):
        inst = self.instantiate_from("messagedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageDefinition instance")
        self.implMessageDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition1(inst2)

    def implMessageDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.category), force_bytes("notification"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org"))
        self.assertEqual(inst.date.date, FHIRDate("2016-11-09").date)
        self.assertEqual(inst.date.as_json(), "2016-11-09")
        self.assertEqual(force_bytes(inst.eventCoding.code), force_bytes("admin-notify"))
        self.assertEqual(force_bytes(inst.eventCoding.system), force_bytes("http://example.org/fhir/message-events"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.name), force_bytes("EXAMPLE"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Defines a base example for other MessageDefinition instances."))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Message definition base example</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Message definition base example"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/MessageDefinition/example"))

    def testMessageDefinition2(self):
        inst = self.instantiate_from("messagedefinition-patient-link-notification.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageDefinition instance")
        self.implMessageDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition2(inst2)

    def implMessageDefinition2(self, inst):
        self.assertEqual(force_bytes(inst.allowedResponse[0].message), force_bytes("MessageDefinition/patient-link-response"))
        self.assertEqual(force_bytes(inst.allowedResponse[0].situation), force_bytes("Optional response message that may provide additional information"))
        self.assertEqual(force_bytes(inst.base), force_bytes("MessageDefinition/example"))
        self.assertEqual(force_bytes(inst.category), force_bytes("notification"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("� HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-02-03").date)
        self.assertEqual(inst.date.as_json(), "2017-02-03")
        self.assertEqual(force_bytes(inst.description), force_bytes("Notification of two patient records that represent the same individual that require an established linkage."))
        self.assertEqual(force_bytes(inst.eventCoding.code), force_bytes("admin-notify"))
        self.assertEqual(force_bytes(inst.eventCoding.system), force_bytes("http://example.org/fhir/message-events"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.focus[0].code), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.focus[0].max), force_bytes("2"))
        self.assertEqual(inst.focus[0].min, 2)
        self.assertEqual(force_bytes(inst.focus[0].profile), force_bytes("StructureDefinition/example"))
        self.assertEqual(force_bytes(inst.id), force_bytes("patient-link-notification"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("United States of America (the)"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.name), force_bytes("PATIENT-LINK-NOTIFICATION"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Notifies recipient systems that two patients have been 'linked' - meaning they represent the same individual"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Link Patients Notification</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Link Patients Notification"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/MessageDefinition/patient-link-notification"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("positive"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/variant-state"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))

    def testMessageDefinition3(self):
        inst = self.instantiate_from("messagedefinition-patient-link-response.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageDefinition instance")
        self.implMessageDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition3(inst2)

    def implMessageDefinition3(self, inst):
        self.assertEqual(force_bytes(inst.base), force_bytes("MessageDefinition/example"))
        self.assertEqual(force_bytes(inst.category), force_bytes("consequence"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("� HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-02-03").date)
        self.assertEqual(inst.date.as_json(), "2017-02-03")
        self.assertEqual(force_bytes(inst.description), force_bytes("Optional response to a patient link notification."))
        self.assertEqual(force_bytes(inst.eventCoding.code), force_bytes("admin-notify"))
        self.assertEqual(force_bytes(inst.eventCoding.system), force_bytes("http://example.org/fhir/message-events"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.focus[0].code), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.focus[0].max), force_bytes("2"))
        self.assertEqual(inst.focus[0].min, 2)
        self.assertEqual(force_bytes(inst.focus[0].profile), force_bytes("StructureDefinition/example"))
        self.assertEqual(force_bytes(inst.id), force_bytes("patient-link-response"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9879"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("United States of America (the)"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.name), force_bytes("PATIENT-LINK-RESPONSE"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Optional response message that may provide additional information on the outcome of the patient link operation."))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Link Patients Response</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Link Patients Response"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/MessageDefinition/patient-link-response"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("positive"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/variant-state"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))

