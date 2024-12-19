from django.urls import path
from . import views


urlpatterns = [
    path('',views.all_user),
    path('create-customer/',views.create_customer),
    path('show-customers/',views.show_customers),
    path('retrieve-customer/<int:pk>/',views.retrieve_customer),
    path('login-user/',views.login_user),
    path('create-user&customer/',views.create_user_customer),
    path('create-user&admin/',views.create_user_admininfo),
]
