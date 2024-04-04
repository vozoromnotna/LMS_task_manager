from django.contrib import admin

from django.contrib import admin
from .models import BugReport, FeatureRequest
from tasks.models import *

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'status', 'priority')
    list_filter = ('created_at', 'updated_at', 'status', 'priority') 
    search_fields = ('title', 'description', 'created_at', 'updated_at', 'status', 'priority')
    ordering = ('created_at', )
    date_hierarchy = 'created_at'
    list_editable = ('status', 'priority')
    fields = ('title', 'description', 'status', 'priority', 'project', 'task')

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'status', 'priority')
    list_filter = ('created_at', 'updated_at', 'status', 'priority') 
    search_fields = ('title', 'description', 'created_at', 'updated_at', 'status', 'priority')
    ordering = ('created_at', )
    date_hierarchy = 'created_at'
    list_editable = ('status', 'priority')
    fields = ('title', 'description', 'status', 'priority', 'project', 'task')
