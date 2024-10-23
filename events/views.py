from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, EventCategory
from .serializers import EventSerializer, EventCreateUpdateSerializer, EventCategorySerializer
from .filters import EventFilter  # Import your custom filters

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventCategoryListView(generics.ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [permissions.AllowAny]

class EventCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
