from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer

class MeasureUnitListAPIView(GeneralListAPIView):
  serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListAPIView):
  serializer_class = IndicadorSerializer

class CategoryProductListAPIView(GeneralListAPIView):
  serializer_class = CategoryProductSerializer






















