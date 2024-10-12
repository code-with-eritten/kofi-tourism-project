from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from destinations.models import Destination


# Create your models here.


class Like(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('destination', 'user')  # Ensure a user can't like the same destination multiple times

    def __str__(self):
        return f'{self.user.username} likes {self.destination.name}'
