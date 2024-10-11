from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/', include('destinations.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # Djoser JWT URLs
    path('authenticate/', TokenObtainPairView.as_view(), name='token'),
    path('users/', include('users.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
