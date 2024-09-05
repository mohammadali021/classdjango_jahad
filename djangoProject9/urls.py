from django.contrib import admin
from django.urls import path, include

from months import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Month', include('months.urls')),
    path('product', include('products.urls')),
    path('customers', include('customers.urls')),
    path('forms', include('forms.urls', namespace="forms")),
    path('contacts/', include('contacts.urls')),
]
