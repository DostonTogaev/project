from django.contrib import admin
from django.urls import path
from app.views import index, product_detail, customer, customer_detail,delete_customer, add_customer

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('customer/', customer, name='customer'),
    path('detail/', customer_detail, name='customer_detail'),
    path('detail/<int:customer_id>/', delete_customer, name='delete'),
    path('add-customer/', add_customer, name='add_customer')
]
