from django.urls import path, include
from django.conf.urls.static import static
from djoser.views import UserViewSet
from rest_framework import routers
from skymarket import settings


user_router = routers.SimpleRouter()
user_router.register('users', UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

