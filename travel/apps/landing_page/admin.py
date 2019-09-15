from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationBaseModelAdmin
from mptt.admin import MPTTModelAdmin

from apps.landing_page.models import (
    Plan,
    Feature,
    Statistic,
    Service,
    Testimony,
    Slider,
    PlanFeature,
    PriceType,
    Price,
    Magazine
)

BASE_LIST = ('order', 'active')


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 1


@admin.register(Plan)
class PlanAdmin(TranslationAdmin):
    list_display = ('name',) + BASE_LIST
    list_filter = ('active',)
    search_fields = ('name', 'features__name')
    inlines = [PlanFeatureInline]
    exclude = ('features',)
    list_editable = BASE_LIST


@admin.register(Feature)
class FeatureAdmin(TranslationBaseModelAdmin, MPTTModelAdmin):
    list_display = ('name',) + BASE_LIST
    list_editable = BASE_LIST
    list_filter = ('active',)
    search_fields = ('name', 'children__name')
    list_select_related = ('parent', 'validated_plan')


@admin.register(Statistic)
class StatisticAdmin(TranslationAdmin):
    list_display = ('name', 'icon') + BASE_LIST
    list_editable = BASE_LIST
    list_filter = ('active',)
    search_fields = ('name', 'value')


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', 'icon') + BASE_LIST
    list_editable = BASE_LIST
    list_filter = ('active',)
    search_fields = ('name', 'description')


@admin.register(Testimony)
class TestimonyAdmin(TranslationAdmin):
    list_display = ('author', 'place') + BASE_LIST
    list_editable = BASE_LIST
    list_filter = ('active',)
    search_fields = ('comment', 'author', 'place')


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ('title', 'type') + BASE_LIST
    list_editable = BASE_LIST
    list_filter = ('active', 'type')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'image', 'active', 'order')}),
        (_('Company'), {'fields': ('type', 'site')})
    )


class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    list_filter = ('type',)
    search_fields = ['type']

admin.site.register(PriceType, PriceTypeAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('type','value',)
    list_display_links = ('type','value',)
    list_filter = ('type','value',)
    search_fields = ['type']

admin.site.register(Price, PriceAdmin)

class MagazineAdmin(admin.ModelAdmin):
    list_display = ('name', 'editor', 'files', 'status', 'order',)
    list_display_links = ('name',  'files', 'order',)
    list_filter = ('name','editor',)
    search_fields = ['name', 'editor', 'status']
admin.site.register(Magazine, MagazineAdmin)
