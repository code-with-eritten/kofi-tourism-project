from rest_framework import serializers
from .models import TourOperator


class TourOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourOperator
        fields = [
            'id', 'name', 'slug', 'description', 'contact_email', 
            'contact_phone', 'location', 'rating', 'active', 
            'featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
