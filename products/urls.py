from django.urls import path
from . import views

urlpatterns = [
    path('show-products/',views.show_products),
    path('update-products/<int:pk>/',views.update_products),
    path('delete-products/<int:pk>/',views.delete_products),
    path('show-categories/',views.show_categories),
    path('update-categories/<int:pk>/',views.update_categories),
    path('delete-categories/<int:pk>/',views.delete_categories),
    path('create-product/',views.create_product),
    path('create-categories/',views.create_categories),
    path('retrieve-products/<int:pk>/',views.retrieve_products),
]