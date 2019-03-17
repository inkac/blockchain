from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='mine_index'),
    path('start/', views.start, name='mine_start'),
]

