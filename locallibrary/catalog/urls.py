from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet, basename='Book')
router.register(r'author',views.AuthorViewSet, basename='Author')

urlpatterns = [
    path('', include(router.urls)),
]