from django.urls import path
from rest_framework.generics import DestroyAPIView
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView  

urlpatterns = [
  path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
  path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
  path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
  #path('product/list/', ProductListAPIView.as_view(), name='product_list'),
  path('products/', ProductListCreateAPIView.as_view(), name='products'),
  path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product'),
  #path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
  #path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
]
