from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import welcome, locura, Test_to_do, Questions
from rest_framework import routers

router = routers.DefaultRouter()
# url to try serializers and views delete once in production
router.register(r"test_serializer", Questions, basename="questions")

urlpatterns = [
    path("", welcome, name="welcome"),
    path("locura/", locura, name="locura"),
    url(r"^", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
