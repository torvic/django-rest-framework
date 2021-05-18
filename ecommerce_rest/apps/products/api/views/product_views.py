from django.views import generic
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  serializer_class = ProductSerializer

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state=True) 
    else:
      return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

  def list(self, request):
    print("Hola desde el listado")
    product_serializer = self.get_serializer(self.get_queryset(), many=True)
    return Response(product_serializer.data, status=status.HTTP_200_OK)


  def create(self, request, *args, **kwargs):
    print("Hola desde create")
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, pk=None):
    if self.get_queryset(pk):
      product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
      if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
      return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None, *args, **kwargs):
    product = self.get_queryset().filter(id=pk).first()
    if product:
      product.state = False
      product.save()
      return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    return Response({'error': 'No existe este producto!'}, status=status.HTTP_400_BAD_REQUEST)
  
  
#class ProductListAPIView(GeneralListAPIView):
#  serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = ProductSerializer

  queryset = serializer_class.Meta.model.objects.filter(state=True)

  def post(self, request, *args, **kwargs):
    print("Hola desde create")
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProductSerializer

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state=True) 
    else:
      return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
      

  def patch(self, request, pk=None):
    if self.get_queryset(pk):
      product_serializer = self.serializer_class(self.get_queryset(pk))
      return Response(product_serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No existe este producto!'}, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk=None):
    if self.get_queryset(pk):
      product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
      if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
      return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk=None, *args, **kwargs):
    product = self.get_queryset().filter(id=pk).first()
    if product:
      product.state = False
      product.save()
      return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    return Response({'error': 'No existe este producto!'}, status=status.HTTP_400_BAD_REQUEST)


    