from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCategoryListView,
    EventCategoryDetailView
)

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),  # For listing and creating events
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),  # For viewing, updating, and deleting an event by ID
    path('categories/', EventCategoryListView.as_view(), name='event-category-list'),  # For listing and creating event categories
    path('categories/<int:pk>/', EventCategoryDetailView.as_view(), name='event-category-detail'),  # For viewing, updating, and deleting an event category by ID
]
