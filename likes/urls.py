from django.urls import path
from .views import LikeListView, LikeCreateView, LikeDeleteView

urlpatterns = [
    path('likes/', LikeListView.as_view(), name='like-list'),  # List all likes
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),  # Create a like
    path('likes/delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),  # Unlike (delete a like)
]
