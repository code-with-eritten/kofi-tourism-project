from django.contrib.auth import get_user_model
from django.db import models
from destinations.models import Destination

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Updates on edits

    def __str__(self):
        return f'Comment by {self.user.email} on {self.destination.name}'


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_replies')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Updates on edits

    def __str__(self):
        return f'Reply by {self.user.email} on {self.comment.id}'
