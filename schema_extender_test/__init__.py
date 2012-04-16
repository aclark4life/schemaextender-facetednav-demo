from Products.Archetypes.public import BooleanField
from archetypes.schemaextender.field import ExtensionField

class MyBooleanField(ExtensionField, BooleanField):
    """A trivial field."""
