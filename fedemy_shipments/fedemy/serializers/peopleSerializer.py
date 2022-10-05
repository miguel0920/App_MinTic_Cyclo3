# Django REST Framework
from rest_framework import serializers

# Models
from fedemy.models.people import People


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = '__all__'

    def update(self, instance, validated_data):
        personInstance = People.objects.update(**validated_data)
        return personInstance

    