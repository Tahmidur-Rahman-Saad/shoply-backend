
from django.contrib import admin
from django.urls import path,include
from users import urls
from orders import urls
from products import urls

#used for simple JWT authentiaction
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('orders/',include('orders.urls')),
    path('products/',include('products.urls')),

    #used for simple JWT authentiaction
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
]
