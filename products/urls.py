from django.urls import path
from . import views

urlpatterns = [
    path('show-products/',views.show_products),
    path('update-products/',views.update_products),
    path('delete-products/',views.delete_products),
    path('show-categories/',views.show_categories),
    path('update-categories/',views.update_categories),
    path('delete-categories/',views.delete_categories),
    path('create-product/',views.create_product),
    path('create-categories/',views.create_categories),
    path('retrieve-products/<int:pk>/',views.retrieve_products),
]