from django.urls import path
from . import views
urlpatterns = [
        path('', views.index),
        path('details/', views.details),
        path('signin/', views.signin),
        path('home/', views.home),
        path('error/', views.error),
]