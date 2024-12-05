from django.urls import path
from . import views

urlpatterns = [
    path('show-orders/',views.show_orders),
    path('retrieve-order/<int:pk>/',views.retrieve_order),
    path('confirm-order/<int:pk>/',views.confirm_order),
    path('retrieve-cartitem/<int:pk>/',views.retrieve_cartitem),
    path('add-items/<int:pk>/',views.add_to_cartitems),
    path('create-cart/',views.create_cart),
    path('update-cartitem/<int:pk>/',views.update_cartitem),
    path('update-order/<int:pk>/',views.update_order),
    path('delete-cartitem/<int:pk>/',views.delete_cartitem),
]