from django.urls import path
from .views import ProductDetail, ProductList, OrderDetail, OrderList

urlpatterns = [
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('order/', OrderList.as_view(), name='product-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='product-detail')
]