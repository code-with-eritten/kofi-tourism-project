from django.db import models


# Create your models here.

class TourOperator(models.Model):
    name = models.CharField(max_length=255)
    description = MarkdownxField()
    contact_info = models.TextField()
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='tour_operators/', blank=True, null=True)

    def str(self):
        return self.name
