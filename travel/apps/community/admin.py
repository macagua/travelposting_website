from django.contrib import admin
from apps.community.models import Recommendation, Referral
# Register your models here.

admin.site.register(Recommendation)

admin.site.register(
    Referral,
    list_display=[
        "user",
        "referredBy",
    ],
    readonly_fields=["code", "created_at"],
    list_filter=["created_at"],
    search_fields=["user__first_name", "user__last_name",
                   "user__email", "user__username", "code"]
)


