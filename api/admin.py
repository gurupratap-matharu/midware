from django.contrib import admin

from api.models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'method', 'endpoint', 'response_code', 'exec_time', 'remote_address', 'body_request',)
    list_filter = ('method', 'date', 'exec_time',)
    search_fields = ('endpoint',)


admin.site.register(Request, RequestAdmin)
