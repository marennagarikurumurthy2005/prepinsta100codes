from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404
from django.utils import timezone
import uuid
from django.db.models import Sum, Count, Q
from datetime import timedelta

from .models import MenuItem, Order, OrderItem, Payment
from .serializers import (
    MenuItemSerializer, OrderSerializer, OrderCreateSerializer,
    OrderUpdateSerializer, PaymentSerializer, PaymentCreateSerializer
)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'category']
    ordering_fields = ['price', 'rating', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        category = self.request.query_params.get('category', None)
        is_available = self.request.query_params.get('is_available', None)

        if category:
            queryset = queryset.filter(category=category)
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')

        return queryset

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get menu items grouped by category"""
        categories = MenuItem.CATEGORY_CHOICES
        result = {}
        for category_code, category_name in categories:
            items = MenuItem.objects.filter(category=category_code)
            result[category_code] = MenuItemSerializer(items, many=True).data
        return Response(result)

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get only available menu items"""
        available_items = MenuItem.objects.filter(is_available=True)
        serializer = self.get_serializer(available_items, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

    def get_queryset(self):
        queryset = Order.objects.all()
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

    def create(self, request, *args, **kwargs):
        """Create a new order with items"""
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate unique order ID
        order_id = f"ORD-{timezone.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"

        # Calculate totals
        items_data = serializer.validated_data.pop('items')
        subtotal = 0
        order_items = []

        for item_data in items_data:
            menu_item = get_object_or_404(MenuItem, id=item_data['menu_item_id'])
            quantity = item_data['quantity']
            item_total = menu_item.price * quantity
            subtotal += item_total
            order_items.append({
                'menu_item': menu_item,
                'quantity': quantity,
                'price': menu_item.price
            })

        # Calculate tax and delivery
        tax = subtotal * 0.05  # 5% tax
        delivery_charge = 0 if subtotal > 500 else 50  # Free delivery above 500

        # Create order
        order = Order.objects.create(
            order_id=order_id,
            subtotal=subtotal,
            tax=tax,
            delivery_charge=delivery_charge,
            total_amount=subtotal + tax + delivery_charge,
            **serializer.validated_data
        )

        # Create order items
        for item in order_items:
            OrderItem.objects.create(order=order, **item)

        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['patch'])
    def update_status(self, request, order_id=None):
        """Update order status"""
        order = self.get_object()
        serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_table(self, request):
        """Get orders by table number"""
        table_number = request.query_params.get('table_number', None)
        if not table_number:
            return Response(
                {'error': 'table_number parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        orders = Order.objects.filter(table_number=table_number)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def track(self, request, order_id=None):
        """Track order status"""
        order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(serializer.data)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'transaction_id'

    @action(detail=False, methods=['post'])
    def process_payment(self, request):
        """Process payment for an order"""
        serializer = PaymentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = get_object_or_404(Order, id=serializer.validated_data['order_id'])

        # Create payment record
        payment = Payment.objects.create(
            order=order,
            transaction_id=serializer.validated_data['transaction_id'],
            amount=serializer.validated_data['amount'],
            payment_method=serializer.validated_data['payment_method'],
            status='completed'
        )

        # Update order payment status
        order.payment_status = 'completed'
        order.status = 'confirmed'
        order.save()

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['get'])
    def by_order(self, request):
        """Get payment by order ID"""
        order_id = request.query_params.get('order_id', None)
        if not order_id:
            return Response(
                {'error': 'order_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        payment = get_object_or_404(Payment, order_id=order_id)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)


@api_view(['GET'])
def admin_dashboard(request):
    """Get admin dashboard statistics"""
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)

    total_orders = Order.objects.count()
    today_orders = Order.objects.filter(created_at__date=today).count()
    pending_orders = Order.objects.filter(status='pending').count()
    completed_orders = Order.objects.filter(status='completed').count()

    total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    today_revenue = Order.objects.filter(created_at__date=today).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    week_revenue = Order.objects.filter(created_at__date__gte=week_ago).aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    popular_items = OrderItem.objects.values('menu_item__name').annotate(
        count=Count('id')
    ).order_by('-count')[:5]

    payment_methods = Order.objects.values('payment_method').annotate(
        count=Count('id')
    )

    return Response({
        'total_orders': total_orders,
        'today_orders': today_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
        'total_revenue': float(total_revenue),
        'today_revenue': float(today_revenue),
        'week_revenue': float(week_revenue),
        'popular_items': list(popular_items),
        'payment_methods': list(payment_methods),
    })


@api_view(['GET'])
def admin_orders(request):
    """Get all orders for admin with filtering"""
    status_filter = request.query_params.get('status', None)
    date_filter = request.query_params.get('date', None)

    orders = Order.objects.all()

    if status_filter:
        orders = orders.filter(status=status_filter)

    if date_filter:
        orders = orders.filter(created_at__date=date_filter)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def admin_menu_stats(request):
    """Get menu item statistics"""
    total_items = MenuItem.objects.count()
    available_items = MenuItem.objects.filter(is_available=True).count()
    unavailable_items = MenuItem.objects.filter(is_available=False).count()

    items_by_category = MenuItem.objects.values('category').annotate(
        count=Count('id'),
        avg_price=Sum('price') / Count('id')
    )

    return Response({
        'total_items': total_items,
        'available_items': available_items,
        'unavailable_items': unavailable_items,
        'items_by_category': list(items_by_category),
    })
