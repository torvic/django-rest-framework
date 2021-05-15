from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
  serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
  serializer_class = ProductSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
      
