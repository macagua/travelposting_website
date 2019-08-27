from django.contrib import admin

from apps.payments.models.paypal import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'end_date', 'active')
    list_editable = ('active',)
    list_filter = ('start_date', 'end_date', 'active', 'plan')
    search_fields = ('name', 'code', 'plan')
