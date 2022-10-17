"""cv_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from cvsite import views
from django.http import Http404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cvsite, name='home'),
    
    path('curriculum/', views.curriculum, name='curriculum'),
    path('index/',views.index,name='index'),
    path('detail/<int:cvelement_id>', views.detail, name="detail"),
    
]
