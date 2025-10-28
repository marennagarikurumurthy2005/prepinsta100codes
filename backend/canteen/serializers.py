from rest_framework import serializers
from .models import MenuItem, Order, OrderItem, Payment


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'category', 'price', 'image_url', 
                  'is_available', 'rating', 'reviews_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity', 'price', 'created_at']
        read_only_fields = ['created_at', 'price']

    def create(self, validated_data):
        menu_item_id = validated_data.pop('menu_item_id')
        menu_item = MenuItem.objects.get(id=menu_item_id)
        validated_data['menu_item'] = menu_item
        validated_data['price'] = menu_item.price
        return super().create(validated_data)


class OrderItemCreateSerializer(serializers.Serializer):
    menu_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'customer_name', 'table_number', 'phone_number', 
                  'email', 'status', 'payment_method', 'payment_status', 
                  'special_instructions', 'subtotal', 'tax', 'delivery_charge', 
                  'total_amount', 'items', 'created_at', 'updated_at']
        read_only_fields = ['order_id', 'created_at', 'updated_at']


class OrderCreateSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=100)
    table_number = serializers.IntegerField(min_value=1)
    phone_number = serializers.CharField(max_length=15)
    email = serializers.EmailField(required=False, allow_blank=True)
    payment_method = serializers.ChoiceField(choices=['online', 'cod'])
    special_instructions = serializers.CharField(required=False, allow_blank=True)
    items = OrderItemCreateSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Order must contain at least one item.")
        return value


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'payment_status']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'transaction_id', 'amount', 'payment_method', 
                  'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class PaymentCreateSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    transaction_id = serializers.CharField(max_length=100)
    payment_method = serializers.CharField(max_length=20)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
