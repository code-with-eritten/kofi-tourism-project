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
    path('api-v1/', include('likes.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('events/', include('events.urls')),
    path('api-v1/', include('utils.urls')),
    path('api-v1/', include('accomodation.urls')),
    path('api-v1/', include('tour_operators.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
