
from django.contrib import admin
from django.urls import path,include
from users import urls
from orders import urls
from products import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('orders/',include('orders.urls')),
    path('products/',include('products.urls')),
]
