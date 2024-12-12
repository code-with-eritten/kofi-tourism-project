from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field()
    location = models.CharField(max_length=200)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    price_range = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_photos')
