# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import resource

class Bundle(resource.Resource):
    """ Contains a collection of resources.

    A container for a collection of resources.
    """

    resource_type = "Bundle"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.entry = None
        """ Entry in the bundle - will have a resource or information.
        List of `BundleEntry` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Persistent identifier for the bundle.
        Type `Identifier` (represented as `dict` in JSON). """

        self.link = None
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """

        self.signature = None
        """ Digital Signature.
        Type `Signature` (represented as `dict` in JSON). """

        self.timestamp = None
        """ When the bundle was assembled.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.total = None
        """ If search, the total number of matches.
        Type `int`. """

        self.type = None
        """ document | message | transaction | transaction-response | batch |
        batch-response | history | searchset | collection.
        Type `str`. """

        super(Bundle, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("entry", "entry", BundleEntry, "BundleEntry", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", False, None, False),
            ("link", "link", BundleLink, "BundleLink", True, None, False),
            ("signature", "signature", signature.Signature, "Signature", False, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, "instant", False, None, False),
            ("total", "total", int, "unsignedInt", False, None, False),
            ("type", "type", str, "code", False, None, True),
        ])
        return js


from . import backboneelement

class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource or information.

    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """

    resource_type = "BundleEntry"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.fullUrl = None
        """ URI for resource (Absolute URL server address or URI for UUID/OID).
        Type `str`. """

        self.link = None
        """ Links related to this entry.
        List of `BundleLink` items (represented as `dict` in JSON). """

        self.request = None
        """ Additional execution information (transaction/batch/history).
        Type `BundleEntryRequest` (represented as `dict` in JSON). """

        self.resource = None
        """ A resource in the bundle.
        Type `Resource` (represented as `dict` in JSON). """

        self.response = None
        """ Results of execution (transaction/batch/history).
        Type `BundleEntryResponse` (represented as `dict` in JSON). """

        self.search = None
        """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """

        super(BundleEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("fullUrl", "fullUrl", str, "uri", False, None, False),
            ("link", "link", BundleLink, "BundleLink", True, None, False),
            ("request", "request", BundleEntryRequest, "BundleEntryRequest", False, None, False),
            ("resource", "resource", resource.Resource, "Resource", False, None, False),
            ("response", "response", BundleEntryResponse, "BundleEntryResponse", False, None, False),
            ("search", "search", BundleEntrySearch, "BundleEntrySearch", False, None, False),
        ])
        return js


class BundleEntryRequest(backboneelement.BackboneElement):
    """ Additional execution information (transaction/batch/history).

    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """

    resource_type = "BundleEntryRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.ifMatch = None
        """ For managing update contention.
        Type `str`. """

        self.ifModifiedSince = None
        """ For managing cache currency.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.ifNoneExist = None
        """ For conditional creates.
        Type `str`. """

        self.ifNoneMatch = None
        """ For managing cache currency.
        Type `str`. """

        self.method = None
        """ GET | HEAD | POST | PUT | DELETE | PATCH.
        Type `str`. """

        self.url = None
        """ URL for HTTP equivalent of this entry.
        Type `str`. """

        super(BundleEntryRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("ifMatch", "ifMatch", str, "string", False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirdate.FHIRDate, "instant", False, None, False),
            ("ifNoneExist", "ifNoneExist", str, "string", False, None, False),
            ("ifNoneMatch", "ifNoneMatch", str, "string", False, None, False),
            ("method", "method", str, "code", False, None, True),
            ("url", "url", str, "uri", False, None, True),
        ])
        return js


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Results of execution (transaction/batch/history).

    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """

    resource_type = "BundleEntryResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.etag = None
        """ The Etag for the resource (if relevant).
        Type `str`. """

        self.lastModified = None
        """ Server's date time modified.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.location = None
        """ The location (if the operation returns a location).
        Type `str`. """

        self.outcome = None
        """ OperationOutcome with hints and warnings (for batch/transaction).
        Type `Resource` (represented as `dict` in JSON). """

        self.status = None
        """ Status response code (text optional).
        Type `str`. """

        super(BundleEntryResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("etag", "etag", str, "string", False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, "instant", False, None, False),
            ("location", "location", str, "uri", False, None, False),
            ("outcome", "outcome", resource.Resource, "Resource", False, None, False),
            ("status", "status", str, "string", False, None, True),
        ])
        return js


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.

    Information about the search process that lead to the creation of this
    entry.
    """

    resource_type = "BundleEntrySearch"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.mode = None
        """ match | include | outcome - why this is in the result set.
        Type `str`. """

        self.score = None
        """ Search ranking (between 0 and 1).
        Type `float`. """

        super(BundleEntrySearch, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, "code", False, None, False),
            ("score", "score", float, "decimal", False, None, False),
        ])
        return js


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.

    A series of links that provide context to this bundle.
    """

    resource_type = "BundleLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relation = None
        """ See http://www.iana.org/assignments/link-relations/link-
        relations.xhtml#link-relations-1.
        Type `str`. """

        self.url = None
        """ Reference details for the link.
        Type `str`. """

        super(BundleLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, "string", False, None, True),
            ("url", "url", str, "uri", False, None, True),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
