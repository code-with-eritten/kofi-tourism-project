from rest_framework import serializers
from .models import EventCategory, Event

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']

class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'category', 'location', 'start_time', 'end_time', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'location', 'start_time', 'end_time']
