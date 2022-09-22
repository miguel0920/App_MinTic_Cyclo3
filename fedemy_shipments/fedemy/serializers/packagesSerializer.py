# Django REST Framework
from rest_framework import serializers
from fedemy.models import packages

# Models
from fedemy.models.packages import Packages

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'

    def create(self, validated_data):
        print('😁😁',validated_data)
        userInstance = Packages.objects.create(**validated_data)
        return userInstance

    def getUsers():
        users = Packages.objects.all()
        return users
