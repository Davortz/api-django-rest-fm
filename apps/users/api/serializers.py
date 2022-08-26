from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    print('Serializer')

    class Meta:
        model = User
        fields = '__all__'
