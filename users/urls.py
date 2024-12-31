from django.urls import path
from . import views


urlpatterns = [
    path('create-customer/',views.create_customer),
    path('create-admin/',views.create_admininfo),
    path('show-customers/',views.show_customers),
    path('show-admin/',views.show_admininfos),
    path('retrieve-customer/<int:pk>/',views.retrieve_customer),
    path('retrieve-admin/<int:pk>/',views.retrieve_admininfo),
    path('login-user/',views.login_user),
    path('create-user&customer/',views.create_user_customer),
    path('create-user&admin/',views.create_user_admininfo),
    path('reset-password/',views.reset_password),
    path('update_customer/',views.update_customer),
    path('delete_customer/',views.delete_customer),
    path('update_admin/',views.update_admininfo),
    path('delete_admin/',views.delete_admininfo),

]
