"""Neiroexpert_WEb URL Configuration

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
from django.urls import path,include
from mainapp import views as mainapp
from authapp import views as authapp
from projektapp import views as projektapp
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as mainapp

app_name = 'mainapp' 

urlpatterns = [
    path( '' , mainapp.main, name = 'main'),
    path( 'damage_neiro/<int:pk>' , mainapp.damage_neiro_calculate, name = 'damage_neiro' ),
    path( 'damage_metoda/' , mainapp.damage_metoda_calculate, name = 'damage_metoda'),
    path( 'in_progress/' , mainapp.in_progress, name = 'in_progress'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
