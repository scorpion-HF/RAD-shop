from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('cart/<str:branch>/', views.UserCart.as_view(), name='user-cart'),
    path('remove_item/<int:pk>/', views.RemoveFromCart.as_view(), name='remove-item'),
    path('create_order/<str:branch>/', views.CreateOrder.as_view(), name='create-order'),
    path('user_orders/', views.OrdersList.as_view(), name='orders'),
    path('remove_order/<int:pk>/', views.RemoveOrder.as_view(), name='remove-order'),
    path('order_detail/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
]
