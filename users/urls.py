from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_user),
    path('create-user/',views.create_user),
    path('show-users/',views.show_users),
    path('retrieve-user/<int:pk>/',views.retrieve_user),
]
