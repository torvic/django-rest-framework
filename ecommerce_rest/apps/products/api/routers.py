from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename="products")
router.register(r'measure-unit', MeasureUnitViewSet, basename="measure-unit")
router.register(r'indicator', IndicatorViewSet, basename="indicator")
router.register(r'category-product', CategoryProductViewSet, basename="category-product")
urlpatterns = router.urls