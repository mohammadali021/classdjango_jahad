from django.urls import path

from customers import views

urlpatterns = [
    path('', views.index),
    path('/<slug:s>', views.info, name='etelaat'),
]
