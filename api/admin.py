# Django
from django.contrib import admin

# Own
from .models import Task


@admin.action(description='Mark selected todo as completed')
def make_todos_completed(modeladmin, request, queryset):
    queryset.update(completed=True)


@admin.action(description='Mark selected todo as not completed')
def make_todos_not_completed(modeladmin, request, queryset):
    queryset.update(completed=False)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ("title", "completed", "created_at")
    list_display = ("title", "completed")
    list_filter = ("completed", "created_at")
    list_display_links = ("title",)
    readonly_fields = ("created_at",)
    ordering = ('-created_at',)
    actions = (make_todos_completed, make_todos_not_completed)

