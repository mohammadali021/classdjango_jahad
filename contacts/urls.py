from django.urls import path, include
from contacts import views
# app_name = 'contanct'
urlpatterns = [
    path('' , views.ViewContactUs , name='contact_us' ),
    path('login/' , views.ViewLogin, name='login'),
    path('logout/' , views.Viewlogout , name='logout'),
    path('cp/' , views.ViewChangePass , name='change_pass'),
]