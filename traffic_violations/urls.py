from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('citizens/', views.citizens, name='citizens')
]