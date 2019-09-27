from modeltranslation.translator import (
    register,
    TranslationOptions,
)

from apps.landing_page.models import (
    Plan,
    Feature,
    Service,
    Statistic,
    Testimony,
    Slider,
    Magazine,
)


@register([Plan, Feature])
class NameTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Service)
class ServiceTranslationOptions(NameTranslationOptions):
    fields = ('description',)


@register(Statistic)
class StatisticsTranslationOptions(NameTranslationOptions):
    fields = ('value',)


@register(Testimony)
class TestimonyTranslationOptions(TranslationOptions):
    fields = ('comment', 'place')


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Magazine)
class MagazineTranslationOptions(TranslationOptions):
    fields = ('name', )