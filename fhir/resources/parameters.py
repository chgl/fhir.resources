# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.

    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """

    resource_type = "Parameters"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.parameter = None
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """

        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, "ParametersParameter", True, None, False),
        ])
        return js


from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.

    A parameter passed to or received from the operation.
    """

    resource_type = "ParametersParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Name from the definition.
        Type `str`. """

        self.part = None
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """

        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """

        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """

        self.valueAge = None
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """

        self.valueAnnotation = None
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueBoolean = None
        """ If parameter is a data type.
        Type `bool`. """

        self.valueCanonical = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueCode = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueContactDetail = None
        """ If parameter is a data type.
        Type `ContactDetail` (represented as `dict` in JSON). """

        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.valueContributor = None
        """ If parameter is a data type.
        Type `Contributor` (represented as `dict` in JSON). """

        self.valueCount = None
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """

        self.valueDataRequirement = None
        """ If parameter is a data type.
        Type `DataRequirement` (represented as `dict` in JSON). """

        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """

        self.valueDistance = None
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """

        self.valueDosage = None
        """ If parameter is a data type.
        Type `Dosage` (represented as `dict` in JSON). """

        self.valueDuration = None
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """

        self.valueExpression = None
        """ If parameter is a data type.
        Type `Expression` (represented as `dict` in JSON). """

        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """

        self.valueId = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """

        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """

        self.valueMarkdown = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueMeta = None
        """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """

        self.valueMoney = None
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """

        self.valueOid = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueParameterDefinition = None
        """ If parameter is a data type.
        Type `ParameterDefinition` (represented as `dict` in JSON). """

        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """

        self.valuePositiveInt = None
        """ If parameter is a data type.
        Type `int`. """

        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """

        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """

        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueRelatedArtifact = None
        """ If parameter is a data type.
        Type `RelatedArtifact` (represented as `dict` in JSON). """

        self.valueSampledData = None
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """

        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """

        self.valueString = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """

        self.valueTriggerDefinition = None
        """ If parameter is a data type.
        Type `TriggerDefinition` (represented as `dict` in JSON). """

        self.valueUnsignedInt = None
        """ If parameter is a data type.
        Type `int`. """

        self.valueUri = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueUrl = None
        """ If parameter is a data type.
        Type `str`. """

        self.valueUsageContext = None
        """ If parameter is a data type.
        Type `UsageContext` (represented as `dict` in JSON). """

        self.valueUuid = None
        """ If parameter is a data type.
        Type `str`. """

        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, "string", False, None, True),
            ("part", "part", ParametersParameter, "ParametersParameter", True, None, False),
            ("resource", "resource", resource.Resource, "Resource", False, None, False),
            ("valueAddress", "valueAddress", address.Address, "Address", False, "value", False),
            ("valueAge", "valueAge", age.Age, "Age", False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, "Annotation", False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, "Attachment", False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, "base64Binary", False, "value", False),
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", False),
            ("valueCanonical", "valueCanonical", str, "canonical", False, "value", False),
            ("valueCode", "valueCode", str, "code", False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, "ContactDetail", False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, "ContactPoint", False, "value", False),
            ("valueContributor", "valueContributor", contributor.Contributor, "Contributor", False, "value", False),
            ("valueCount", "valueCount", count.Count, "Count", False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, "DataRequirement", False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, "dateTime", False, "value", False),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", False),
            ("valueDistance", "valueDistance", distance.Distance, "Distance", False, "value", False),
            ("valueDosage", "valueDosage", dosage.Dosage, "Dosage", False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, "Duration", False, "value", False),
            ("valueExpression", "valueExpression", expression.Expression, "Expression", False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, "HumanName", False, "value", False),
            ("valueId", "valueId", str, "id", False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, "Identifier", False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, "instant", False, "value", False),
            ("valueInteger", "valueInteger", int, "integer", False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, "markdown", False, "value", False),
            ("valueMeta", "valueMeta", meta.Meta, "Meta", False, "value", False),
            ("valueMoney", "valueMoney", money.Money, "Money", False, "value", False),
            ("valueOid", "valueOid", str, "oid", False, "value", False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, "ParameterDefinition", False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, "Period", False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, "positiveInt", False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, "Quantity", False, "value", False),
            ("valueRange", "valueRange", range.Range, "Range", False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, "Ratio", False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, "RelatedArtifact", False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, "SampledData", False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, "Signature", False, "value", False),
            ("valueString", "valueString", str, "string", False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, "Timing", False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, "TriggerDefinition", False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, "unsignedInt", False, "value", False),
            ("valueUri", "valueUri", str, "uri", False, "value", False),
            ("valueUrl", "valueUrl", str, "url", False, "value", False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, "UsageContext", False, "value", False),
            ("valueUuid", "valueUuid", str, "uuid", False, "value", False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + '.meta']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
