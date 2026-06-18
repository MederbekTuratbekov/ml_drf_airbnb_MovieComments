from modeltranslation.translator import TranslationOptions, register
from .models import Property


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('description',)
