# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import domainresource

class PractitionerRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.

    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """

    resource_type = "PractitionerRole"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this practitioner's record is in active use.
        Type `bool`. """

        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """

        self.availableTime = None
        """ Times the Service Site is available.
        List of `PractitionerRoleAvailableTime` items (represented as `dict` in JSON). """

        self.code = None
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        practitioner with this role.
        List of `FHIRReference` items referencing `['Endpoint']` (represented as `dict` in JSON). """

        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items referencing `['HealthcareService']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifiers that are specific to a role/location.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `['Location']` (represented as `dict` in JSON). """

        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `PractitionerRoleNotAvailable` items (represented as `dict` in JSON). """

        self.organization = None
        """ Organization where the roles are available.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """

        self.practitioner = None
        """ Practitioner that is able to provide the defined services for the
        organation.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.telecom = None
        """ Contact details that are specific to the role/location/service.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(PractitionerRole, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, "boolean", False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, "string", False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, "PractitionerRoleAvailableTime", True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, "Reference", True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, "Reference", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("location", "location", fhirreference.FHIRReference, "Reference", True, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, "PractitionerRoleNotAvailable", True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, "Reference", False, None, False),
            ("period", "period", period.Period, "Period", False, None, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, "Reference", False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, "ContactPoint", True, None, False),
        ])
        return js


from . import backboneelement

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """

    resource_type = "PractitionerRoleAvailableTime"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allDay = None
        """ Always available? e.g. 24 hour service.
        Type `bool`. """

        self.availableEndTime = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.availableStartTime = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """

        super(PractitionerRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, "boolean", False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, "time", False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, "time", False, None, False),
            ("daysOfWeek", "daysOfWeek", str, "code", True, None, False),
        ])
        return js


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    resource_type = "PractitionerRoleNotAvailable"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Reason presented to the user explaining why time not available.
        Type `str`. """

        self.during = None
        """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """

        super(PractitionerRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, "string", False, None, True),
            ("during", "during", period.Period, "Period", False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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
