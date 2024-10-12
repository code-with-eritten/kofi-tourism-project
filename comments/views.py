from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer


# List all comments or create a new one (authentication required for creation)
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Public can view, login required to post

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, update, or delete a specific comment (authentication required)
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Must be authenticated to edit/delete


# List all replies or create a new reply (authentication required for creation)
class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Public can view, login required to post

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, update, or delete a specific reply (authentication required)
class ReplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Must be authenticated to edit/delete
