from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='products-list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products-detail'),
]
