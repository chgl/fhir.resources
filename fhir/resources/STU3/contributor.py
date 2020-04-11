# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contributor
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import element

class Contributor(element.Element):
    """ Contributor information.

    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """

    resource_type = "Contributor"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details of the contributor.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.name = None
        """ Who contributed the content.
        Type `str`. """

        self.type = None
        """ author | editor | reviewer | endorser.
        Type `str`. """

        super(Contributor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, "ContactDetail", True, None, False),
            ("name", "name", str, "string", False, None, True),
            ("type", "type", str, "code", False, None, True),
        ])
        return js


import sys
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
