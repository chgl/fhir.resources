# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """

    resource_type = "EnrollmentResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.disposition = None
        """ Disposition Message.
        Type `str`. """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """

        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `['EnrollmentRequest']` (represented as `dict` in JSON). """

        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("disposition", "disposition", str, "string", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, "Reference", False, None, False),
            ("outcome", "outcome", str, "code", False, None, False),
            ("request", "request", fhirreference.FHIRReference, "Reference", False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, "Reference", False, None, False),
            ("status", "status", str, "code", False, None, False),
        ])
        return js


import sys
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
