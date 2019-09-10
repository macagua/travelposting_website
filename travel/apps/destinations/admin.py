import nested_admin
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdminMixin
from jet.admin import CompactInline

from .models import (
    OptionTabData,
    Destination,
    Photo,
    TourData,
    HeaderSection,
    DestinationDetail,
    TabData,
    GeneralDetail,
    InventarioDetail,
    BookingDetail,
)


class NestedCompactInline(nested_admin.NestedInlineModelAdminMixin, CompactInline):
    pass


@admin.register(OptionTabData)
class OptionTabDataAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description')
    summernote_fields = ('template',)


class PhotoInline(NestedCompactInline):
    model = Photo
    max_num = 12
    min_num = 0
    extra = 1


class TabDataInline(SummernoteModelAdminMixin, nested_admin.NestedStackedInline):
    summernote_fields = ('content',)
    model = TabData
    max_num = 4
    min_num = 0
    extra = 0


class TourDataInline(nested_admin.NestedStackedInline):
    model = TourData
    inlines = [TabDataInline]


class HeaderSectionInline(nested_admin.NestedTabularInline):
    model = HeaderSection


class GeneralDetailInline(nested_admin.NestedStackedInline):
    model = GeneralDetail


class InventarioDetailInline(nested_admin.NestedStackedInline):
    model = InventarioDetail


class BookingDetailInline(nested_admin.NestedStackedInline):
    model = BookingDetail
    max_num = 10
    min_num = 0
    extra = 1


class DestinationDetailInline(nested_admin.NestedTabularInline):
    model = DestinationDetail
    inlines = [GeneralDetailInline, InventarioDetailInline, BookingDetailInline]


@admin.register(Destination)
class DestinationAdmin(SummernoteModelAdminMixin, nested_admin.NestedModelAdmin):
    list_display = ('name', 'get_sku', 'user', 'is_deleted')
    list_filter = (('user', admin.RelatedFieldListFilter), ('is_deleted', admin.BooleanFieldListFilter))
    search_fields = ('user__email', 'user__first_name', 'name', 'description')
    list_select_related = ('user',)
    autocomplete_fields = ('user',)
    inlines = [PhotoInline, TourDataInline, HeaderSectionInline, DestinationDetailInline]

    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save()
