from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from destinations.models import Destination


# Create your models here.


class Like(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.destination.name
