from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
      user = User(**validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user
    
    def update(self, instance, validated_data):
      update_user= super().update(instance, validated_data)
      update_user.set_password(validated_data['password'])
      update_user.save()
      return update_user


class UserListSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
  
  def to_representation(self, instance):
    return {
      'id': instance['id'],
      'username': instance['username'],
      'correo': instance['email'],
      'password': instance['password'],
    }

""" PROCESO DE VALIDACIONES """
""" class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField(allow_blank=True)

    def validate_name(self, value):
        # cusctom validation
        # print(self.context)
        if 'developer' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        return value


    def validate_email(self, value):
        # custom validation
        if value == '':
            raise serializers.ValidationError('Error, este campo no puedo estar en blanco XD')
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('el email no puede contener el nombre XD')
            
        return value

    def validate(self, data):
        return data 
    
    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance """