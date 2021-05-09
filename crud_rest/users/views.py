from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from users.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        queryset = User.objects.all()
        queryset_serializer = UserSerializer(queryset, many=True)
        return Response(queryset_serializer.data)
    
    if request.method == 'POST':
        user = UserSerializer(data=request.data)

        # validacion
        if user.is_valid():
            user.save()
            return Response({'message':'Usuario creado correctamente'})
        
        return Response(user.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    #queryset
    user = User.objects.filter(id=pk).first()

    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        
        if request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors)
        
        if request.method == 'DELETE':
            user.delete()
            return Response({'message':'Mensaje Eliminado correctamente'}, status=status.HTTP_200_OK)
    
    return Response({'message':'No existe el usuario'}, status=status.HTTP_400_BAD_REQUEST)


