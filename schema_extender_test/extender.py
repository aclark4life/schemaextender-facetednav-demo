from Products.ATContentTypes.interface import IATDocument
from Products.Archetypes.public import BooleanField
from Products.Archetypes.public import BooleanWidget
from Products.Archetypes.public import LinesField
from Products.Archetypes.public import MultiSelectionWidget
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary


def MyVocabularyFactory(context):
   return SimpleVocabulary.fromValues(['one', 'two', 'three'])


class MyBooleanField(ExtensionField, BooleanField):
    """A trivial field."""


class MyStringField(ExtensionField, StringField):
    """Another trivial field."""


class MyLinesField(ExtensionField, LinesField):
    """A non-trivial field."""


class PageExtender(object):
    adapts(IATDocument)
    implements(ISchemaExtender)

    fields = [

        MyBooleanField("super_power",
            widget=BooleanWidget(
                label="This page has super powers"
            )
        ),

        MyStringField("super_power2",
            widget=StringWidget(
                label="This page has super powers too"
            )
        ),

        MyLinesField("super_power3",
            vocabulary_factory='schema_extender_test.MyVocabularyFactory',
            widget=MultiSelectionWidget(
                label="This page has super powers three"
            )
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
