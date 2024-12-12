from rest_framework import generics, filters, status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Category, Destination
from .serializers import (
    CategorySerializer,
    DestinationListSerializer,
    DestinationDetailSerializer
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListView(generics.ListAPIView):
    """
    View to list all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a single category by slug.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class DestinationListView(generics.ListAPIView):
    """
    View to list all destinations with filtering, searching, and ordering.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'location']  # Filter by category and location
    search_fields = ['name', 'short_description', 'location']
    ordering_fields = ['name', 'created_at', 'entrance_fee']


class DestinationRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a single destination by slug.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer
    lookup_field = 'slug'


class DestinationDetailByIDView(generics.RetrieveAPIView):
    """
    View to retrieve a single destination by ID.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer
    lookup_field = 'id'


class PopularDestinationsView(APIView):
    """
    View to list popular destinations based on likes and comments.
    """
    def get(self, request):
        popular_destinations = Destination.objects.annotate(
            like_count=Count('like'),  # Ensure 'like' is the correct related name
            comment_count=Count('comments')
        ).order_by('-like_count', '-comment_count')[:10]

        serializer = DestinationListSerializer(popular_destinations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DestinationsByCategoryView(APIView):
    """
    View to list destinations under a specific category.
    """
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        destinations = Destination.objects.filter(category=category)
        serializer = DestinationListSerializer(destinations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
