from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_user),
    path('show-products/',views.show_products),
    path('show-categories/',views.show_categories),
    path('create-products/',views.create_products),
    path('create-categories/',views.create_categories),
]