from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class TourOperator(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()  # General description of the tour operator
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)  # Enhanced phone number field with validation
    location = models.CharField(max_length=255, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        default=1.0
    )
    active = models.BooleanField(default=True)  # For enabling/disabling tour operators
    featured = models.BooleanField(default=False)  # Flag for highlighting a tour operator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # Latest created operators appear first
        verbose_name_plural = "Tour Operators"
