from django.contrib import admin
from apps.community.models import Recommendation, Message
# Register your models here.


admin.site.register(Recommendation)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'sender', 'content', )

admin.site.register(Message, MessageAdmin)
