from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('products/<str:branch>/', views.ProductsList.as_view(), name='products'),
    path('product<int:pk>/<str:branch>/', views.ProductDetail.as_view(), name='product'),
]
