from django.urls import path
from . import views

# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('',views.all_user),
    path('create-customer/',views.create_customer),
    path('show-customers/',views.show_customers),
    path('retrieve-customer/<int:pk>/',views.retrieve_customer),
    path('login-customer/',views.login_customer),
]

# urlpatterns += [
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]