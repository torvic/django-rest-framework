""" Declarando Serializers """

from datetime import datetime

# importamos serializador
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

# Instanciamos un objeto
comment = Comment(email='example@gmail.com', content='hello world') 

# serializador
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer = CommentSerializer(comment)
print(serializer.data)
    





























