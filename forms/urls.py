from django.urls import path

from forms import views

app_name = 'forms'
urlpatterns = [
    # path("" , views.index, name='view-form')
    path("",views.viewoky , name="view-form"),
]