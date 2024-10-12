from rest_framework import serializers
from .models import Like
from destinations.models import Destination
from django.contrib.auth import get_user_model

User = get_user_model()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display the user's username
    destination = serializers.StringRelatedField()  # Display the destination name

    class Meta:
        model = Like
        fields = ['id', 'user', 'destination']


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['destination', 'user']  # For creating new likes

    def validate(self, data):
        if Like.objects.filter(user=data['user'], destination=data['destination']).exists():
            raise serializers.ValidationError("User has already liked this destination.")
        return data
