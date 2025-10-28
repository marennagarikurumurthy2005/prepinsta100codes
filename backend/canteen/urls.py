from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, OrderViewSet, PaymentViewSet, admin_dashboard, admin_orders, admin_menu_stats

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menu-item')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/orders/', admin_orders, name='admin-orders'),
    path('admin/menu-stats/', admin_menu_stats, name='admin-menu-stats'),
]
