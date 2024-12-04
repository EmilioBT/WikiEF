"""
URL configuration for Web_Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pages.urls import pages_patterns
from habitos.urls import habitos_patterns
from herramientas.urls import herramientas_patterns
from ejercicios.urls import ejercicios_patterns
from core import views as core_views
from ejercicios import views as ejercicios_views
from habitos import views as habitos_views
from herramientas import views as herramientas_views
from proyectos import views as proyectos_views
from django.conf import settings


urlpatterns = [
    path('', core_views.home, name="home"), 
    path('pages', include(pages_patterns)), 
    path('habitos', include(habitos_patterns)),
    path('ejercicios', include(ejercicios_patterns)),
    path('herramientas', include(herramientas_patterns)),
    path('tipoEjercicios', ejercicios_views.tipoEjercicios, name="tipoEjercicios"),
    path('proyectos', proyectos_views.proyectos, name="proyectos"),
    path('login', core_views.login, name="login"),
    path('admin/', admin.site.urls),

    #Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
