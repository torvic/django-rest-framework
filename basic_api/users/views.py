from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from users.serializer import UserSerializer

@api_view(['GET'])
def user_api_view(request):

    if request.method == 'GET':    
        queryset = User.objects.all()
        queryset_serializer = UserSerializer(queryset, many=True)
        return Response(queryset_serializer.data)


