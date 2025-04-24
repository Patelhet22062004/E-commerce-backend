from django.urls import path
from .views import CreateOrderView,VerifyPaymentView,OrderListView,AdminOrderListView,AdminOrderRetriveView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='coffee-payment'),
    path('verify/', VerifyPaymentView.as_view(), name='coffee-payment-3'),
    path('orders/', OrderListView.as_view(), name='coffee-payment-2'),
    path('Admin-orders/', AdminOrderListView.as_view(), name='coffee-payment'),
    path('Admin-orders/<int:pk>/', AdminOrderRetriveView.as_view(), name='coffee-payment-1'),
    
    
    
]