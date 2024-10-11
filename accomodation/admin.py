from django.contrib import admin
from django.utils.html import format_html
from .models import Hotel, Amenity, HotelPhoto


class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating', 'price_range', 'email', 'phone')
    list_filter = ('rating', 'amenities')
    search_fields = ('name', 'location', 'description')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('amenities',)
    inlines = [HotelPhotoInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'location')
        }),
        ('Details', {
            'fields': ('rating', 'price_range', 'email', 'phone')
        }),
        ('Amenities', {
            'fields': ('amenities',)
        }),
    )

    def get_amenities(self, obj):
        return ", ".join([a.name for a in obj.amenities.all()])

    get_amenities.short_description = 'Amenities'


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class HotelPhotoAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image_preview')
    list_filter = ('hotel',)
    search_fields = ('hotel__name',)

    def image_preview(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)

    image_preview.short_description = 'Image Preview'


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(HotelPhoto, HotelPhotoAdmin)
