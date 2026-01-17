from django.urls import path, include
from .views import ProductDetail, ProductList, OrderDetail, OrderList, ProductViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('order/', OrderList.as_view(), name='product-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='product-detail')
]