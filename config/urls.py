"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from bbsnote import views # 404떠서 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbsnote/', include('bbsnote.urls')), # url 분리, bbsnote에 urls.py 만들어준 것
    path('common/', include('common.urls')),
    path('', views.index, name='index',)
]
