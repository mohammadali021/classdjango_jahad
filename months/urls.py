from django.urls import path

from months import views

urlpatterns = [
    path('', views.ViewMonths)
]
