#from apps.base.api import GeneralListAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer
from apps.products.models import MeasureUnit, CategoryProduct, Indicator

class MeasureUnitViewSet(viewsets.GenericViewSet):
  serializer_class = MeasureUnitSerializer

  def get_queryset(self):
    return self.get_serializer().Meta.model.objects.filter(state=True)
  
  def list(self, request):
    data = self.get_queryset()
    data_serializer = self.get_serializer(data, many=True)
    return Response(data_serializer.data)

class IndicatorViewSet(viewsets.GenericViewSet):
  serializer_class = IndicadorSerializer
  queryset = Indicator.objects.filter(state=True)

  def list(self, request):
    """ 
    Hola desde Indicator class
    """
    data = self.get_queryset()
    data_serializer = self.get_serializer(data, many=True)
    return Response(data_serializer.data)

class CategoryProductViewSet(viewsets.GenericViewSet):
  serializer_class = CategoryProductSerializer
  queryset = CategoryProduct.objects.filter(state=True)

  def list(self, request):
    data = self.get_queryset()
    data_serializer = self.get_serializer(data, many=True)
    return Response(data_serializer.data)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)





















