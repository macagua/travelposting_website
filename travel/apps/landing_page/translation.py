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
