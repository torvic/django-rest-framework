from apps.products.models import Product

from rest_framework import serializers
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product 
    exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'description': instance.description,
      'image': instance.imagen if instance.imagen != '' else '',
      'measure_unit': instance.measure_unit.description,
      'category_product': instance.category_product.description
    }