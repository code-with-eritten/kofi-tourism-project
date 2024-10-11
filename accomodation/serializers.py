from rest_framework import serializers
from .models import Hotel, HotelPhoto, Amenity


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name']


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['id', 'image']


class HotelSerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True)
    photos = HotelPhotoSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'slug', 'description', 'location', 'rating', 'price_range', 'email', 'phone',
                  'amenities', 'photos']

    def get_description(self, obj):
        return obj.get_description_as_markdown()
