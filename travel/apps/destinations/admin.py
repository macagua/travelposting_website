from django.contrib import admin
from django_summernote.admin import SummernoteModelAdminMixin
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
    Categorie,
    SearchLanding
)

@admin.register(OptionTabData)
class OptionTabDataAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description')
    summernote_fields = ('template',)


class PhotoInline(admin.TabularInline):
    model = Photo
    max_num = 12
    min_num = 0
    extra = 1


class TabDataInline(SummernoteModelAdminMixin, admin.ModelAdmin):
    summernote_fields = ('content',)
    model = TabData
    max_num = 4
    min_num = 0
    extra = 0


class TourDataInline(admin.TabularInline):
    model = TourData
    inlines = [TabDataInline]


class HeaderSectionInline(admin.TabularInline):
    model = HeaderSection


class GeneralDetailInline(admin.TabularInline):
    model = GeneralDetail


class InventarioDetailInline(admin.ModelAdmin):
    model = InventarioDetail


class BookingDetailInline(admin.ModelAdmin):
    model = BookingDetail
    max_num = 10
    min_num = 0
    extra = 1


class DestinationDetailInline(admin.TabularInline):
    model = DestinationDetail
    inlines = [GeneralDetailInline, InventarioDetailInline, BookingDetailInline]


@admin.register(Destination)
class DestinationAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_sku', 'user', 'is_deleted')
    list_filter = (('user', admin.RelatedFieldListFilter), ('is_deleted', admin.BooleanFieldListFilter))
    search_fields = ('user__email', 'user__first_name', 'name', 'description')
    list_select_related = ('user',)
    autocomplete_fields = ('user',)
    inlines = [PhotoInline, TourDataInline, HeaderSectionInline, DestinationDetailInline]

    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save()


@admin.register(Categorie)
class OptionTabDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'image')


admin.site.register(GeneralDetail)
admin.site.register(TourData)
admin.site.register(SearchLanding)
