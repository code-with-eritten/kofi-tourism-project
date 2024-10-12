from django.urls import path
from .views import (
    CommentListCreateView,
    CommentDetailView,
    ReplyListCreateView,
    ReplyDetailView,
)

urlpatterns = [
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    # List all comments or create a comment
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    # Retrieve, update, or delete a comment

    path('replies/', ReplyListCreateView.as_view(), name='reply-list-create'),  # List all replies or create a reply
    path('replies/<int:pk>/', ReplyDetailView.as_view(), name='reply-detail'),  # Retrieve, update, or delete a reply
]
