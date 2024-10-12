from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer, LikeCreateSerializer

# List all likes (optional, for admin or detailed view)
class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
#    permission_classes = [IsAuthenticated]  # Only authenticated users can view likes

# Create a like
class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeCreateSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can like destinations

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Unlike a destination (delete a like)
class LikeDeleteView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure the user can only delete their own likes
        return Like.objects.filter(user=self.request.user)
