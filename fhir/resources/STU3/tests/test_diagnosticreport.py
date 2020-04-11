# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
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
from .. import diagnosticreport
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DiagnosticReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticReport", js["resourceType"])
        return diagnosticreport.DiagnosticReport(js)

    def testDiagnosticReport1(self):
        inst = self.instantiate_from("diagnosticreport-example-f202-bloodculture.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport1(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport1(inst2)

    def implDiagnosticReport1(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("15220000"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Laboratory test"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.coding[1].code), force_bytes("LAB"))
        self.assertEqual(force_bytes(inst.category.coding[1].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("104177005"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Blood culture for bacteria, including anaerobic screen"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].code), force_bytes("428763004"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].display), force_bytes("Bacteremia due to staphylococcus"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("Blood culture tested positive on staphylococcus aureus"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("req"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-03-11T10:28:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-03-11T10:28:00+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport2(self):
        inst = self.instantiate_from("diagnosticreport-example-ghp.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport2(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport2(inst2)

    def implDiagnosticReport2(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("GHP"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("General Health Profile"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://acme.com/labs/reports"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("rtt"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("ltt"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("urine"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("p2"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("r1"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("r2"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("r3"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("r4"))
        self.assertEqual(force_bytes(inst.contained[8].id), force_bytes("r5"))
        self.assertEqual(force_bytes(inst.contained[9].id), force_bytes("r6"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2015-08-16T06:40:17Z").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2015-08-16T06:40:17Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("ghp"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/lab/reports"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ghp-example"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-08-17T06:40:17Z").date)
        self.assertEqual(inst.issued.as_json(), "2015-08-17T06:40:17Z")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2015-08-16T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2015-08-16T10:35:23Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport3(self):
        inst = self.instantiate_from("diagnosticreport-example-lipids.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport3(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport3(inst2)

    def implDiagnosticReport3(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("HM"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("24331-1"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Lipid 1996 panel - Serum or Plasma"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Lipid Panel"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("cholesterol"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("triglyceride"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("hdlcholesterol"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("ldlcholesterol"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("lipids"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/lab/reports"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("5234342"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-01-27T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-01-27T11:45:33+11:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport4(self):
        inst = self.instantiate_from("diagnosticreport-example-f001-bloodexam.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport4(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport4(inst2)

    def implDiagnosticReport4(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("252275004"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Haematology test"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.coding[1].code), force_bytes("HM"))
        self.assertEqual(force_bytes(inst.category.coding[1].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("58410-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Complete blood count (hemogram) panel - Blood by Automated count"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("Core lab"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("req"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.bmc.nl/zorgportal/identifiers/reports"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("nr1239044"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-05-15T19:32:52+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-05-15T19:32:52+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport5(self):
        inst = self.instantiate_from("diagnosticreport-example-ultrasound.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport5(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport5(inst2)

    def implDiagnosticReport5(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("394914008"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Radiology"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.coding[1].code), force_bytes("RAD"))
        self.assertEqual(force_bytes(inst.category.coding[1].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("45036003"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Ultrasonography of abdomen"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Abdominal Ultrasound"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("Unremarkable study"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("ultrasound"))
        self.assertEqual(force_bytes(inst.image[0].comment), force_bytes("A comment about the image"))
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport6(self):
        inst = self.instantiate_from("diagnosticreport-example-f201-brainct.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport6(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport6(inst2)

    def implDiagnosticReport6(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("394914008"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Radiology"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.coding[1].code), force_bytes("RAD"))
        self.assertEqual(force_bytes(inst.category.coding[1].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("429858000"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Computed tomography (CT) of head and neck"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("CT of head-neck"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].code), force_bytes("188340000"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].display), force_bytes("Malignant tumor of craniopharyngeal duct"))
        self.assertEqual(force_bytes(inst.codedDiagnosis[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("CT brains: large tumor sphenoid/clivus."))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport7(self):
        inst = self.instantiate_from("diagnosticreport-genetics-example-2-familyhistory.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport7(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport7(inst2)

    def implDiagnosticReport7(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("15220000"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Laboratory test"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.coding[1].code), force_bytes("LAB"))
        self.assertEqual(force_bytes(inst.category.coding[1].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("55233-1"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Genetic analysis master panel"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("f1-genetics"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2015-05-26T15:30:10+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2015-05-26T15:30:10+01:00")
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/DiagnosticReport-geneticsFamilyMemberHistory"))
        self.assertEqual(force_bytes(inst.id), force_bytes("dg2"))
        self.assertEqual(inst.issued.date, FHIRDate("2014-05-16T10:28:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2014-05-16T10:28:00+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport8(self):
        inst = self.instantiate_from("diagnosticreport-micro1.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport8(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport8(inst2)

    def implDiagnosticReport8(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("MB"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("632-0"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Culture, MRSA"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("obx1-4"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("obx1-5"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("obx2-1"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("obx2-2"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("obx2-4"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("obx2-6"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("obx2-8"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("obx2-10"))
        self.assertEqual(force_bytes(inst.contained[8].id), force_bytes("obx2-12"))
        self.assertEqual(force_bytes(inst.contained[9].id), force_bytes("obx2-14"))
        self.assertEqual(force_bytes(inst.id), force_bytes("micro"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://hnam.org/identifiers/orders"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("290741144"))
        self.assertEqual(inst.issued.date, FHIRDate("2009-08-10T08:25:44+10:00").date)
        self.assertEqual(inst.issued.as_json(), "2009-08-10T08:25:44+10:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport9(self):
        inst = self.instantiate_from("diagnosticreport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport9(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport9(inst2)

    def implDiagnosticReport9(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("HM"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("58410-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Complete blood count (hemogram) panel - Blood by Automated count"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.coding[1].code), force_bytes("CBC"))
        self.assertEqual(force_bytes(inst.code.coding[1].display), force_bytes("MASTER FULL BLOOD COUNT"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Complete Blood Count"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("r1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("r2"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("r3"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("r4"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("r5"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("r6"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("r7"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("r8"))
        self.assertEqual(force_bytes(inst.contained[8].id), force_bytes("r9"))
        self.assertEqual(force_bytes(inst.contained[9].id), force_bytes("r10"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/lab/reports"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("5234342"))
        self.assertEqual(inst.issued.date, FHIRDate("2011-03-04T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2011-03-04T11:45:33+11:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("01"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("Needs Review"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://example.org/fhir/CodeSystem/workflow-codes"))
        self.assertEqual(force_bytes(inst.presentedForm[0].contentType), force_bytes("application/pdf"))
        self.assertEqual(force_bytes(inst.presentedForm[0].language), force_bytes("en-AU"))
        self.assertEqual(force_bytes(inst.presentedForm[0].title), force_bytes("HTML Report"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testDiagnosticReport10(self):
        inst = self.instantiate_from("diagnosticreport-example-papsmear.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport10(inst)

        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport10(inst2)

    def implDiagnosticReport10(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("47527-7"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2013-02-11T10:33:33+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2013-02-11T10:33:33+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("pap"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-02-13T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-02-13T11:45:33+11:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

