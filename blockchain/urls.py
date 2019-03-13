from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:block_id>/', views.read, name='read'),
    path('write/', views.write, name='write'),
]
