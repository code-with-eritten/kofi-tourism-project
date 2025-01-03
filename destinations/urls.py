from django.urls import path
from .views import (
    CategoryListView,
    CategoryRetrieveView,
    DestinationListView,
    DestinationRetrieveView,
    DestinationDetailByIDView,  # Added import
    PopularDestinationsView,
    DestinationsByCategoryView,
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryRetrieveView.as_view(), name='category-detail'),
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
    path('destinations/<slug:slug>/', DestinationRetrieveView.as_view(), name='destination-detail-by-slug'),  # Updated name
    path('destinations/<int:id>/', DestinationDetailByIDView.as_view(), name='destination-detail-by-id'),  # New endpoint
    path('popular-destinations/', PopularDestinationsView.as_view(), name='popular-destinations'),
    path('destinations/category/<slug:slug>/', DestinationsByCategoryView.as_view(), name='destinations-by-category'),
]
