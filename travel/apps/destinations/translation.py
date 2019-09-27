from modeltranslation.translator import (
    register,
    TranslationOptions,
)

from apps.destinations.models import (
    Categorie,
    Destination,
    Photo,
    Badge,
    OptionTabData,
)

@register(Categorie)
class CategorieTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description','status',)

@register(Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = ('name','short_description','description',)

@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('name','description',)

@register(Badge)
class BadgeTranslationOptions(TranslationOptions):
    fields = ('name','description',)

@register(OptionTabData)
class OptionTabDataTranslationOptions(TranslationOptions):
    fields = ('name','description','template',)
