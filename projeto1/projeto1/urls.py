"""
URL configuration for projeto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic.base import RedirectView

# Importe a view index do seu novo aplicativo 'core'
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('votacao/', include('votacao.urls')),
    path('blog/', include('blog.urls')),

    # URL para a página de entrada principal (ex: http://localhost:8000/index/)
    path('index/', core_views.index, name='main_index'),

    # Redireciona a URL raiz (/) para a página de entrada /index/
    path('', RedirectView.as_view(url='/index/', permanent=False), name='root_redirect'),
]
