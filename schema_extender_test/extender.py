from Products.ATContentTypes.interface import IATDocument
from Products.Archetypes.public import BooleanField
from Products.Archetypes.public import BooleanWidget
from Products.Archetypes.public import LinesField
from Products.Archetypes.public import MultiSelectionWidget
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implements


class MyBooleanField(ExtensionField, BooleanField):
    """A trivial field."""


class PageExtender(object):
    adapts(IATDocument)
    implements(ISchemaExtender)

    fields = [
        MyBooleanField("super_power",
        widget=BooleanWidget(
            label="This page has super powers")),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
