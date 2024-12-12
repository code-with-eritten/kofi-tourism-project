from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import TourOperator
from .serializers import TourOperatorSerializer


class TourOperatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing and listing Tour Operators.
    """
    queryset = TourOperator.objects.all()
    serializer_class = TourOperatorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Adding filtering, search, and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Define which fields can be filtered
    filterset_fields = ['active', 'featured', 'rating', 'location']
    
    # Define search fields
    search_fields = ['name', 'description', 'location']
    
    # Define ordering fields
    ordering_fields = ['created_at', 'updated_at', 'rating', 'name']
    ordering = ['-created_at']  # Default ordering

    def get_queryset(self):
        """
        Customize the queryset with additional logic, if necessary.
        """
        queryset = super().get_queryset()

        # Additional filtering logic can go here
        return queryset
