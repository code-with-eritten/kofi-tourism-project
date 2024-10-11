from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'is_verified', 'profile_image_url',
                  'telephone', 'date_joined']
        read_only_fields = ['id', 'email', 'is_verified', 'date_joined']
