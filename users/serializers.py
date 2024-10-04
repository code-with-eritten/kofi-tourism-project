from rest_framework import serializers
from django.contrib.auth import get_user_model
from ads.models import Product, Review, Store

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'is_verified', 'profile_image_url',
                  'telephone', 'products_count', 'reviews_count', 'date_joined']
        read_only_fields = ['id', 'email', 'is_verified', 'date_joined']

    def get_products_count(self, obj):
        # Assuming products are related through Store model
        return Product.objects.filter(store__owner=obj).count()

    def get_reviews_count(self, obj):
        return Review.objects.filter(user=obj).count()
