from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdminMixin

from .forms import DestinationMapForm
from .models import (
    OptionTabData,
    Destination,
    Photo,
    Video,
    TourData,
    HeaderSection,
    DestinationDetail,
    TabData,
    GeneralDetail,
    InventarioDetail,
    BookingDetail,
    Categorie,
    SearchLanding,
    Booking,
    DestinationMap,
    Itinerary,
    BookingStats,
    SocialNetwork,
    DestinationVisitor,
    Advertising,
    MessageDashboard,
    BookingQuestion,
    BookingChoice
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


class VideoInline(admin.TabularInline):
    model = Video
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


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

    for destination in queryset:
        subject = _('Destination was published')

        ctx = {
            'user' : destination.user,
            'destination' : destination,
        }

        #Notify owner
        message_user = _('Congratulations your destination was published.')
        html_message_user = render_to_string(
            'pages/published_email_user.html',
            context=ctx
        )

        send_mail(
            subject,
            message_user,
            settings.DEFAULT_FROM_EMAIL,
            [destination.user.email,],
            fail_silently=True,
            html_message=html_message_user,
        )

        #Notify managers
        message = _('if you want see the admin site https://travelposting.com/admin/ ')
        html_managers_message = render_to_string(
            'pages/published_email.html',
            context=ctx
        )

        mail_managers(
            subject,
            message,
            fail_silently=True,
            html_message=html_managers_message,
        )
make_published.short_description = _("publish destinations")


def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = _("unpublish destinations")


@admin.register(Destination)
class DestinationAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'is_published', 'user', 'get_sku', 'is_deleted')
    list_filter = (('user', admin.RelatedFieldListFilter), ('is_deleted', admin.BooleanFieldListFilter))
    search_fields = ('user__email', 'user__first_name', 'name', 'description')
    list_select_related = ('user',)
    autocomplete_fields = ('user',)
    inlines = [PhotoInline, VideoInline, TourDataInline, HeaderSectionInline, DestinationDetailInline]
    actions = [make_published, make_unpublished]

    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save()


@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'image')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ('destination__name',)
    list_filter = ['process_status',]
    list_display = [
        'destination',
        'cellphone',
        'mail',
        'seen_status',
        'process_status',
    ]


@admin.register(DestinationVisitor)
class VisitorsAdmin(admin.ModelAdmin):
    search_fields = ('destination__name',)
    list_filter = ['date_time', 'country_name']
    list_display = [
        'destination',
        'dma_code',
        'country_name',
        'date_time',
    ]


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    search_fields = ('name', 'company')
    list_display = [
        'name',
        'company',
        'from_date',
        'to_date',
        'status',
        'position'
    ]

class MessageAdmin(admin.ModelAdmin):
    model = MessageDashboard
    list_display = ('id', 'sender', 'subject', 'content', )


@admin.register(DestinationMap)
class DestinationMapAdmin(admin.ModelAdmin):
    form = DestinationMapForm


class BookingChoiceInline(admin.TabularInline):
    model = BookingChoice
    max_num = 12
    min_num = 0
    extra = 1


class BookingQuestionAdmin(admin.ModelAdmin):
    model = BookingQuestion
    inlines = [BookingChoiceInline]
    search_fields = ('question_text',)
    list_filter = ['question_text', 'pub_date']
    list_display = ('question_text', 'pub_date', )


admin.site.register(MessageDashboard, MessageAdmin)
admin.site.register(GeneralDetail)
admin.site.register(TourData)
admin.site.register(SearchLanding)
admin.site.register(Itinerary)
admin.site.register(BookingStats)
admin.site.register(SocialNetwork)
admin.site.register(BookingQuestion, BookingQuestionAdmin)
