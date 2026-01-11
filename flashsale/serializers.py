from rest_framework import serializers
from django.db import transaction
from .models import Product, Order
from django.core.signals import request_finished
from .signals import stock_zero
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    def validate(self, data):
        product = data['product']
        amount = data['amount']

        if amount <= 0:
            raise serializers.ValidationError({
                "amount": "Invalid amount!"
            })

        if amount > product.stock:
            raise serializers.ValidationError({
                "amount": f"Not enough stock. Available: {product.stock}"
            })
        
        return data

    @transaction.atomic
    def create(self, validated_data):
        product = Product.objects.select_for_update().get(
            id=validated_data['product'].id
        )
    
        amount = validated_data['amount']
        product.stock -= amount
        product.save()
    
        if product.stock == 0:
            stock_zero.send(
                sender=self.__class__,
                product_name=product.name
            )
    
        validated_data['price_at_purchase'] = product.price
        return Order.objects.create(**validated_data)

    class Meta:
        model = Order
        fields = '__all__'
