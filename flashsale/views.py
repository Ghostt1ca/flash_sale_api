from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Product, Order
from django.db.models import Sum, F, Avg
from .serializers import ProductSerializer, OrderSerializer
# Create your views here.

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_produse = self.get_queryset().count()

        statistics = self.get_queryset().aggregate(
            valoare_totala=Sum(F('price') * F('stock')),
            stoc_mediu = Avg('stock')
        )
        return Response({
            "total_produse": total_produse,
            "inventar": statistics
        })