from django.urls import path
from . import views

urlpatterns = [
    path('promotions/',views.promotions),
    path('promotions-details/<int:pk>/',views.promotionDetails),
    path('promotions-create/',views.promotionCreate),
    path('promotions-update/<int:pk>/',views.promotionUpdate),
    path('promotions-delete/<int:pk>/',views.promotionDelete),

]