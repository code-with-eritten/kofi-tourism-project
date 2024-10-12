from rest_framework import serializers
from .models import Comment, Reply


class ReplySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')  # Show user email

    class Meta:
        model = Reply
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')  # Show user email
    replies = ReplySerializer(many=True, read_only=True)  # Nested replies

    class Meta:
        model = Comment
        fields = ['id', 'user', 'destination', 'content', 'created_at', 'updated_at', 'replies']
