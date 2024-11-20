from django.urls import path
from .views import HabitosListView, HabitosDetailView, HabitosCreate, HabitosUpdate, HabitosDelete

habitos_patterns = ([
    path('', HabitosListView.as_view(), name='habitos'),
    path('<int:pk>/<slug:page_slug>/', HabitosDetailView.as_view(), name='habito'),
    path('create/', HabitosCreate.as_view(), name='create'),
    path('update/<int:pk>/', HabitosUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', HabitosDelete.as_view(), name='delete'),
], 'habitos')