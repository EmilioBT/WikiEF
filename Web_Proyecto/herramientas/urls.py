from django.urls import path
from .views import HerramientasListView, HerramientasDetailView, HerramientasCreate, HerramientasUpdate, HerramientasDelete

herramientas_patterns = ([
    path('', HerramientasListView.as_view(), name='herramientas'),
    path('<int:pk>/<slug:page_slug>/', HerramientasDetailView.as_view(), name='herramientas'),
    path('create/', HerramientasCreate.as_view(), name='create'),
    path('update/<int:pk>/', HerramientasUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', HerramientasDelete.as_view(), name='delete'),
], 'herramientas')