# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ConceptMap
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """

    resource_type = "ConceptMap"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the concept map.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.group = None
        """ Same source and target systems.
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for concept map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this concept map (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this concept map is defined.
        Type `str`. """

        self.sourceCanonical = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str` referencing `['ValueSet']`. """

        self.sourceUri = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.targetCanonical = None
        """ The target value set which provides context for the mappings.
        Type `str` referencing `['ValueSet']`. """

        self.targetUri = None
        """ The target value set which provides context for the mappings.
        Type `str`. """

        self.title = None
        """ Name for this concept map (human friendly).
        Type `str`. """

        self.url = None
        """ Canonical identifier for this concept map, represented as a URI
        (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the concept map.
        Type `str`. """

        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("copyright", "copyright", str, "markdown", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("description", "description", str, "markdown", False, None, False),
            ("experimental", "experimental", bool, "boolean", False, None, False),
            ("group", "group", ConceptMapGroup, "ConceptMapGroup", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("name", "name", str, "string", False, None, False),
            ("publisher", "publisher", str, "string", False, None, False),
            ("purpose", "purpose", str, "markdown", False, None, False),
            ("sourceCanonical", "sourceCanonical", str, "canonical", False, "source", False),
            ("sourceUri", "sourceUri", str, "uri", False, "source", False),
            ("status", "status", str, "code", False, None, True),
            ("targetCanonical", "targetCanonical", str, "canonical", False, "target", False),
            ("targetUri", "targetUri", str, "uri", False, "target", False),
            ("title", "title", str, "string", False, None, False),
            ("url", "url", str, "uri", False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, "UsageContext", True, None, False),
            ("version", "version", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class ConceptMapGroup(backboneelement.BackboneElement):
    """ Same source and target systems.

    A group of mappings that all have the same source and target system.
    """

    resource_type = "ConceptMapGroup"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.element = None
        """ Mappings for a concept from the source set.
        List of `ConceptMapGroupElement` items (represented as `dict` in JSON). """

        self.source = None
        """ Source system where concepts to be mapped are defined.
        Type `str`. """

        self.sourceVersion = None
        """ Specific version of the  code system.
        Type `str`. """

        self.target = None
        """ Target system that the concepts are to be mapped to.
        Type `str`. """

        self.targetVersion = None
        """ Specific version of the  code system.
        Type `str`. """

        self.unmapped = None
        """ What to do when there is no mapping for the source concept.
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """

        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, "ConceptMapGroupElement", True, None, True),
            ("source", "source", str, "uri", False, None, False),
            ("sourceVersion", "sourceVersion", str, "string", False, None, False),
            ("target", "target", str, "uri", False, None, False),
            ("targetVersion", "targetVersion", str, "string", False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, "ConceptMapGroupUnmapped", False, None, False),
        ])
        return js


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """

    resource_type = "ConceptMapGroupElement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Identifies element being mapped.
        Type `str`. """

        self.display = None
        """ Display for the code.
        Type `str`. """

        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """

        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, "code", False, None, False),
            ("display", "display", str, "string", False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, "ConceptMapGroupElementTarget", True, None, False),
        ])
        return js


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """

    resource_type = "ConceptMapGroupElementTarget"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Code that identifies the target element.
        Type `str`. """

        self.comment = None
        """ Description of status/issues in mapping.
        Type `str`. """

        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """

        self.display = None
        """ Display for the code.
        Type `str`. """

        self.equivalence = None
        """ relatedto | equivalent | equal | wider | subsumes | narrower |
        specializes | inexact | unmatched | disjoint.
        Type `str`. """

        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """

        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, "code", False, None, False),
            ("comment", "comment", str, "string", False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, "ConceptMapGroupElementTargetDependsOn", True, None, False),
            ("display", "display", str, "string", False, None, False),
            ("equivalence", "equivalence", str, "code", False, None, True),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, "ConceptMapGroupElementTargetDependsOn", True, None, False),
        ])
        return js


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """

    resource_type = "ConceptMapGroupElementTargetDependsOn"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.display = None
        """ Display for the code (if value is a code).
        Type `str`. """

        self.property = None
        """ Reference to property mapping depends on.
        Type `str`. """

        self.system = None
        """ Code System (if necessary).
        Type `str` referencing `['CodeSystem']`. """

        self.value = None
        """ Value of the referenced element.
        Type `str`. """

        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("display", "display", str, "string", False, None, False),
            ("property", "property", str, "uri", False, None, True),
            ("system", "system", str, "canonical", False, None, False),
            ("value", "value", str, "string", False, None, True),
        ])
        return js


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ What to do when there is no mapping for the source concept.

    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """

    resource_type = "ConceptMapGroupUnmapped"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Fixed code when mode = fixed.
        Type `str`. """

        self.display = None
        """ Display for the code.
        Type `str`. """

        self.mode = None
        """ provided | fixed | other-map.
        Type `str`. """

        self.url = None
        """ canonical reference to an additional ConceptMap to use for mapping
        if the source concept is unmapped.
        Type `str` referencing `['ConceptMap']`. """

        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, "code", False, None, False),
            ("display", "display", str, "string", False, None, False),
            ("mode", "mode", str, "code", False, None, True),
            ("url", "url", str, "canonical", False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
