from django.contrib import admin
from django.urls import path
from core.views import health, products, product_detail
urlpatterns = [path('api/health/', health, name='health'), path('api/products/', products, name='products'), path('api/products/<int:product_id>/', product_detail, name='product-detail'), path('staff/', admin.site.urls)]
