from django.contrib import admin
from .models import Event, EventCategory


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'location', 'category']
    list_filter = ['category', 'start_time', 'end_time']
    search_fields = ['title', 'description', 'location']
    ordering = ['-start_time']  # Orders by start time in descending order


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
