from django.contrib import admin

from core.models import RhubarbTask


@admin.register(RhubarbTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = 'created', 'name', 'params', 'is_done', 'result'
    list_filter = 'is_done', 'name',
