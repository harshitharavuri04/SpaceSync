# admin.py
from django.contrib import admin
from .models import Workspace


class WorkspaceAdmin(admin.ModelAdmin):
    list_display = (
        'location', 'capacity', 'workspace_type', 'days_available', 'time_start', 'end_start', 'price_per_hour')
    list_filter = ('location', 'workspace_type', 'days_available')
    search_fields = ('location', 'workspace_type', 'days_available')


admin.site.register(Workspace, WorkspaceAdmin)
