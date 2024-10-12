from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination')  # Display both user and destination in the admin list view
    search_fields = ('user__username', 'destination__name')  # Allow searching by username and destination
    list_filter = ('destination',)  # Add filtering by destination
