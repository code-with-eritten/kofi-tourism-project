from rest_framework import serializers
from .models import Category, Destination, DestinationImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']


class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['id', 'image']
        read_only_fields = ['id']


class DestinationListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'slug', 'short_description', 'location', 'category']
        read_only_fields = ['id']


class DestinationDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = DestinationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'slug', 'description', 'short_description', 'location',
                  'category', 'video_url', 'entrance_fee', 'opening_hours',
                  'latitude', 'longitude', 'created_at', 'updated_at', 'images']
        read_only_fields = ['id', 'created_at', 'updated_at']


class DestinationCreateUpdateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    images = DestinationImageSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = ['name', 'slug', 'description', 'short_description', 'location',
                  'category', 'video_url', 'entrance_fee', 'opening_hours',
                  'latitude', 'longitude', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        destination = Destination.objects.create(**validated_data)
        for image_data in images_data:
            DestinationImage.objects.create(destination=destination, **image_data)
        return destination

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance = super(DestinationCreateUpdateSerializer, self).update(instance, validated_data)

        if images_data:
            instance.images.all().delete()
            for image_data in images_data:
                DestinationImage.objects.create(destination=instance, **image_data)

        return instance
