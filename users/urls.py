from django.urls import path
from . import views

# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('',views.all_user),
    path('create-user/',views.create_user),
    path('show-users/',views.show_users),
    path('retrieve-user/<int:pk>/',views.retrieve_user),
    path('login-user/',views.login_user),
]

# urlpatterns += [
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]