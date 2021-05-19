"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('master', include('master.urls')),
    path('api-token-auth/',obtain_auth_token),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
#include('rest_framework.urls',namespace='rest_framework'),
#urlpatterns = [path("v1/", include(urlpatterns))]