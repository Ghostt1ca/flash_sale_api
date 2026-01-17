from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Product, Order
from django.db.models import Sum, F
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
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_stoc = self.get_queryset().aggregate(
            valoare_totala=Sum(F('price') * F('stock'))
        )
        return Response({
            "mesaj": "Raport inventar",
            "date": total_stoc
        })