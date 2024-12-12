from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'



class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug']  # Add this to filter by category slug
    search_fields = ['name', 'short_description', 'location']
    ordering_fields = ['name', 'created_at', 'entrance_fee']
class DestinationRetrieveView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer
    lookup_field = 'slug'


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Destination
from .serializers import DestinationListSerializer

class PopularDestinationsView(APIView):
    """
    View to list popular destinations based on likes and comments.
    """

    def get(self, request):
        popular_destinations = Destination.objects.annotate(
            like_count=Count('like'),  # Adjusted from 'likes' to 'like'
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
