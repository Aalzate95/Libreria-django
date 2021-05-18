from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet, basename='Book')

urlpatterns = [
    path('', include(router.urls)),
]