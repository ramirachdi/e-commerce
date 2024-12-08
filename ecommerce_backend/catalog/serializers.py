from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock'] 

    def validate_price(self, value):
        """Ensure price is positive."""
        if value <= 0:
            raise serializers.ValidationError("The price must be a positive number.")
        return value

    def validate_stock(self, value):
        """Ensure stock is non-negative."""
        if value < 0:
            raise serializers.ValidationError("The stock cannot be negative.")
        return value
