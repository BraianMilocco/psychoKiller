from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from .views import welcome, locura, test_to_do

urlpatterns = [
    path("", welcome, name="welcome"),
    path("locura/", test_to_do, name="locura"),
    path("form/", test_to_do, name="test_to_do")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
