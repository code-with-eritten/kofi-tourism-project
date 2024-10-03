from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Destination(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = MarkdownxField()
    short_description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='destinations', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    entrance_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
