from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_user),
    path('show-products/',views.show_products),
    path('show-categories/',views.show_categories),
    path('create-product/',views.create_product),
    path('create-categories/',views.create_categories),
    path('retrieve-products/<int:pk>/',views.retrieve_products),
]