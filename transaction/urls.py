from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='transaction_index'),
    path('new/', views.new, name='new'),
]

