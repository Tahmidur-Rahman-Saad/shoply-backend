from django.urls import path
from . import views

urlpatterns = [
    path('show-orders/',views.orders),
    path('show-confirm-orders/',views.ordersConfirmList),
    path('show-cancel-orders/',views.ordersCancelList),
    path('retrieve-order/<int:pk>/',views.orderDetails),
    path('confirm-order/<int:pk>/',views.orderConfirm),
    path('cancel-order/<int:pk>/',views.orderCancel),
    path('retrieve-cartitem/<int:pk>/',views.cartItemDetails),
    path('add-items/<int:pk>/',views.cartItemAdd),
    path('create-cart/',views.cartCreate),
    path('update-cartitem/<int:pk>/',views.cartItemUpdate),
    path('update-order/<int:pk>/',views.orderUpdate),
    path('delete-cartitem/<int:pk>/',views.cartItemDelete),
]