from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel
from .serializers import HotelSerializer


class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['price_range']  # Filter by price range
    search_fields = ['name', 'location', 'amenities__name']  # Search by name, location, and amenities
    ordering_fields = ['rating', 'price_range']  # Allow sorting by rating or price range
