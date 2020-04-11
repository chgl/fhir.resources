# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """

    resource_type = "Questionnaire"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.approvalDate = None
        """ When the questionnaire was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.code = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.derivedFrom = None
        """ Instantiates protocol or definition.
        List of `str` items referencing `['Questionnaire']`. """

        self.description = None
        """ Natural language description of the questionnaire.
        Type `str`. """

        self.effectivePeriod = None
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.identifier = None
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.item = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.lastReviewDate = None
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.name = None
        """ Name for this questionnaire (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this questionnaire is defined.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """

        self.title = None
        """ Name for this questionnaire (human friendly).
        Type `str`. """

        self.url = None
        """ Canonical identifier for this questionnaire, represented as a URI
        (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the questionnaire.
        Type `str`. """

        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, "date", False, None, False),
            ("code", "code", coding.Coding, "Coding", True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("copyright", "copyright", str, "markdown", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("derivedFrom", "derivedFrom", str, "canonical", True, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, "Period", False, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("item", "item", QuestionnaireItem, "QuestionnaireItem", True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, "date", False, None, False),
            ("name", "name", str, "string", False, None, False),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("subjectType", "subjectType", str, "code", True, None, False),
            ("title", "title", str, "string", False, None, False),
            ("url", "url", str, "uri", False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """

    resource_type = "QuestionnaireItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.answerOption = None
        """ Permitted answer.
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """

        self.answerValueSet = None
        """ Valueset containing permitted answers.
        Type `str` referencing `['ValueSet']`. """

        self.code = None
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """

        self.definition = None
        """ ElementDefinition - details for the item.
        Type `str`. """

        self.enableBehavior = None
        """ all | any.
        Type `str`. """

        self.enableWhen = None
        """ Only allow data when.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """

        self.initial = None
        """ Initial value(s) when item is first rendered.
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """

        self.item = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """

        self.linkId = None
        """ Unique id for item in questionnaire.
        Type `str`. """

        self.maxLength = None
        """ No more than this many characters.
        Type `int`. """

        self.prefix = None
        """ E.g. "1(a)", "2.5.3".
        Type `str`. """

        self.readOnly = None
        """ Don't allow human editing.
        Type `bool`. """

        self.repeats = None
        """ Whether the item may repeat.
        Type `bool`. """

        self.required = None
        """ Whether the item must be included in data results.
        Type `bool`. """

        self.text = None
        """ Primary text for the item.
        Type `str`. """

        self.type = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """

        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, "QuestionnaireItemAnswerOption", True, None, False),
            ("answerValueSet", "answerValueSet", str, "canonical", False, None, False),
            ("code", "code", coding.Coding, "Coding", True, None, False),
            ("definition", "definition", str, "uri", False, None, False),
            ("enableBehavior", "enableBehavior", str, "code", False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, "QuestionnaireItemEnableWhen", True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, "QuestionnaireItemInitial", True, None, False),
            ("item", "item", QuestionnaireItem, "QuestionnaireItem", True, None, False),
            ("linkId", "linkId", str, "string", False, None, True),
            ("maxLength", "maxLength", int, "integer", False, None, False),
            ("prefix", "prefix", str, "string", False, None, False),
            ("readOnly", "readOnly", bool, "boolean", False, None, False),
            ("repeats", "repeats", bool, "boolean", False, None, False),
            ("required", "required", bool, "boolean", False, None, False),
            ("text", "text", str, "string", False, None, False),
            ("type", "type", str, "code", False, None, True),
        ])
        return js


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """

    resource_type = "QuestionnaireItemAnswerOption"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.initialSelected = None
        """ Whether option is selected by default.
        Type `bool`. """

        self.valueCoding = None
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Answer value.
        Type `int`. """

        self.valueReference = None
        """ Answer value.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.valueString = None
        """ Answer value.
        Type `str`. """

        self.valueTime = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, "boolean", False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", True),
            ("valueInteger", "valueInteger", int, "integer", False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", True),
            ("valueString", "valueString", str, "string", False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", True),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """

    resource_type = "QuestionnaireItemEnableWhen"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.answerBoolean = None
        """ Value for question comparison based on operator.
        Type `bool`. """

        self.answerCoding = None
        """ Value for question comparison based on operator.
        Type `Coding` (represented as `dict` in JSON). """

        self.answerDate = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.answerDateTime = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.answerDecimal = None
        """ Value for question comparison based on operator.
        Type `float`. """

        self.answerInteger = None
        """ Value for question comparison based on operator.
        Type `int`. """

        self.answerQuantity = None
        """ Value for question comparison based on operator.
        Type `Quantity` (represented as `dict` in JSON). """

        self.answerReference = None
        """ Value for question comparison based on operator.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.answerString = None
        """ Value for question comparison based on operator.
        Type `str`. """

        self.answerTime = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.operator = None
        """ exists | = | != | > | < | >= | <=.
        Type `str`. """

        self.question = None
        """ Question that determines whether item is enabled.
        Type `str`. """

        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, "boolean", False, "answer", True),
            ("answerCoding", "answerCoding", coding.Coding, "Coding", False, "answer", True),
            ("answerDate", "answerDate", fhirdate.FHIRDate, "date", False, "answer", True),
            ("answerDateTime", "answerDateTime", fhirdate.FHIRDate, "dateTime", False, "answer", True),
            ("answerDecimal", "answerDecimal", float, "decimal", False, "answer", True),
            ("answerInteger", "answerInteger", int, "integer", False, "answer", True),
            ("answerQuantity", "answerQuantity", quantity.Quantity, "Quantity", False, "answer", True),
            ("answerReference", "answerReference", fhirreference.FHIRReference, "Reference", False, "answer", True),
            ("answerString", "answerString", str, "string", False, "answer", True),
            ("answerTime", "answerTime", fhirdate.FHIRDate, "time", False, "answer", True),
            ("operator", "operator", str, "code", False, None, True),
            ("question", "question", str, "string", False, None, True),
        ])
        return js


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.

    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """

    resource_type = "QuestionnaireItemInitial"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.valueAttachment = None
        """ Actual value for initializing the question.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ Actual value for initializing the question.
        Type `bool`. """

        self.valueCoding = None
        """ Actual value for initializing the question.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ Actual value for initializing the question.
        Type `float`. """

        self.valueInteger = None
        """ Actual value for initializing the question.
        Type `int`. """

        self.valueQuantity = None
        """ Actual value for initializing the question.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Actual value for initializing the question.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.valueString = None
        """ Actual value for initializing the question.
        Type `str`. """

        self.valueTime = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueUri = None
        """ Actual value for initializing the question.
        Type `str`. """

        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, "Attachment", False, "value", True),
            ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, "Coding", False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, "date", False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, "dateTime", False, "value", True),
            ("valueDecimal", "valueDecimal", float, "decimal", False, "value", True),
            ("valueInteger", "valueInteger", int, "integer", False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, "Quantity", False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, "Reference", False, "value", True),
            ("valueString", "valueString", str, "string", False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, "time", False, "value", True),
            ("valueUri", "valueUri", str, "uri", False, "value", True),
        ])
        return js


import sys
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
