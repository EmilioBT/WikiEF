from django.urls import path
from .views import EjerciciosListView, EjerciciosDetailView, EjerciciosCreate, EjerciciosUpdate, EjerciciosDelete

ejercicios_patterns = ([
    path('', EjerciciosListView.as_view(), name='ejercicios'),
    path('<int:pk>/<slug:page_slug>/', EjerciciosDetailView.as_view(), name='ejercicios'),
    path('create/', EjerciciosCreate.as_view(), name='create'),
    path('update/<int:pk>/', EjerciciosUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', EjerciciosDelete.as_view(), name='delete'),
], 'ejercicios')