from rest_framework import serializers
from heros.models import Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'group')
