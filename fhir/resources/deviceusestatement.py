# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """

    resource_type = "DeviceUseStatement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.basedOn = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items referencing `['ServiceRequest']` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.derivedFrom = None
        """ Supporting information.
        List of `FHIRReference` items referencing `['ServiceRequest', 'Procedure', 'Claim', 'Observation', 'QuestionnaireResponse', 'DocumentReference']` (represented as `dict` in JSON). """

        self.device = None
        """ Reference to device used.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.note = None
        """ Addition details (comments, instructions).
        List of `Annotation` items (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why was DeviceUseStatement performed?.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference', 'Media']` (represented as `dict` in JSON). """

        self.recordedOn = None
        """ When statement was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.source = None
        """ Who made the statement.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.status = None
        """ active | completed | entered-in-error +.
        Type `str`. """

        self.subject = None
        """ Patient using device.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.timingDateTime = None
        """ How often  the device was used.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timingPeriod = None
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """

        self.timingTiming = None
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """

        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, "Reference", True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, "Reference", True, None, False),
            ("device", "device", fhirreference.FHIRReference, "Reference", False, None, True),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, "Reference", True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, "Reference", False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, "dateTime", False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, "Period", False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, "Timing", False, "timing", False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
