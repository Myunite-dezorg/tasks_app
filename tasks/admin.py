from django.contrib import admin
from .models import Task, SubTask

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]
    list_display = ('name', 'content', 'start_date', 'is_deadline', 'deadline_date')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'name', 'completed',)