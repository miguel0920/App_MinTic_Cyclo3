from unicodedata import name
from rest_framework import serializers
from fedemy.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def getUsers():
        users = User.objects.all()
        return users