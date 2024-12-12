from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TourOperatorViewSet

router = DefaultRouter()
router.register(r'tour-operators', TourOperatorViewSet, basename='tour-operator')

urlpatterns = [
    path('', include(router.urls)),
]
