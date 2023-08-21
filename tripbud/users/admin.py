from django.contrib import admin
from .models import CustomUser
from django.contrib.sessions.models import Session


class sessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

# Register your models here.

admin.site.register(Session, sessionAdmin)
admin.site.register(CustomUser)

