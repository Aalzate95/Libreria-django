from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register('users',views.UserViewSet, basename='User')
router.register('register', views.RegisterView, basename='auth_register')

urlpatterns = [
    path('', include(router.urls)),
]