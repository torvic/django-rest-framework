from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from heros.models import Hero
from heros.serializers import HeroSerializer

@api_view(['GET', 'POST'])
def heros_api_view(request):
    
    if request.method == 'GET':
        queryset = Hero.objects.all()
        queryset_serializer = HeroSerializer(queryset, many=True)
        return Response(queryset_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = HeroSerializer(data=request.data)

        #validacion
        if data.is_valid():
            data.save()
            return Response({'message':'Hero creted!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def one_hero_api_view(request, pk=None):
    # queryset-one-hero
    hero = Hero.objects.filter(id=pk).first()
    
    if hero:
        if request.method == 'GET':
            hero_serializer = HeroSerializer(hero)
            return Response(hero_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            hero_serializer = HeroSerializer(hero, data=request.data)
            if hero_serializer.is_valid():
                hero_serializer.save()
                return Response(hero_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            hero.delete()
            return Response({'message': 'Hero removed!'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'There is no hero!'}, status=status.HTTP_400_BAD_REQUEST)
            
            
    
    
    


