from django.urls import path
from .views import (
    CategoryListView,
    CategoryRetrieveView,
    DestinationListView,
    DestinationRetrieveView,
    PopularDestinationsView
)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryRetrieveView.as_view(), name='category-detail'),
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
    path('destinations/<slug:slug>/', DestinationRetrieveView.as_view(), name='destination-detail'),
    path('popular-destinations/', PopularDestinationsView.as_view(), name='popular-destinations'),
]
