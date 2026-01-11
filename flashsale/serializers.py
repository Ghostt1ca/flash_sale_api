from rest_framework import serializers
from django.db import transaction
from .models import Product, Order

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
        
        with transaction.atomic():
            product = Product.objects.select_for_update().get(id=validated_data['product'].id)
        # product = validated_data['product']
        amount = validated_data['amount']

        product.stock -= amount
        product.save()

        return Order.objects.create(**validated_data)

    class Meta:
        model = Order
        fields = '__all__'
