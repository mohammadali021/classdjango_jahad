from django.urls import include, path

from products import views


urlpatterns = [
    path("/<int:num>", views.show_details),
    path("/<slug:s>", views.ViewProductdetails , name='viewpro'),
    path("/<str:mobile>", views.show_mobile),
    path("", views.show_product),
]
