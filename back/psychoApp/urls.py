from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import welcome, Test, Question
from rest_framework import routers

router = routers.DefaultRouter()
# url to try serializers and views delete once in production
router.register(r"question", Question, basename="question")
router.register(r"test", Test, basename="test")

urlpatterns = [
    path("", welcome, name="welcome"),
    url(r"^", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
