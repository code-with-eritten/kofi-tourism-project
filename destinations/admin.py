from django.contrib import admin
from django.db.models import Count
from .models import Category, Destination, DestinationImage

class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1  # Allows one extra empty form for adding new images

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'category', 'created_at', 'get_popularity']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'location', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [DestinationImageInline]  # Add images inline for easy editing

    def get_popularity(self, obj):
        like_count = obj.like_set.count()
        comment_count = obj.comments.count()
        return like_count + comment_count

    get_popularity.short_description = 'Popularity Score'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            like_count=Count('like'),
            comment_count=Count('comments')
        )

@admin.register(DestinationImage)
class DestinationImageAdmin(admin.ModelAdmin):
    list_display = ['destination', 'image']
    list_filter = ['destination']
    search_fields = ['destination__name']
