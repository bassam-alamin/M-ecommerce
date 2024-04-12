from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductListCreateAPIView,
    ProductRetrieveAPIView,
    OrderListCreateAPIView,
    OrderRetrieveAPIView,
    PromotionListAPIView,
    ReviewListCreateAPIView, UserProfileView, ChangePasswordView, CartItemViewSet,
)

router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    # cart items
    path('', include(router.urls)),

    # Product Endpoints
    path('products', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductRetrieveAPIView.as_view(), name='product-detail'),

    # User Profile Endpoints
    path('profile', UserProfileView.as_view(), name='user-profile'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),

    # Order Endpoints
    path('orders', OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>', OrderRetrieveAPIView.as_view(), name='order-detail'),

    # Promotion Endpoints
    path('promotions', PromotionListAPIView.as_view(), name='promotion-list'),

    # Review Endpoints
    path('reviews', ReviewListCreateAPIView.as_view(), name='review-list'),
]