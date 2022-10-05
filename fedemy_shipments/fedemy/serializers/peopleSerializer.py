# Django REST Framework
from dataclasses import field
import datetime
from rest_framework import serializers

# Models
from fedemy.models.people import People


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        # fields = ['personfirstname', 'personsecondname', 'personlastname', 'personrsecondlastname',
        #           'personaddress', 'personphone', 'personemail', 'persondocumentnumber']
        fields = '__all__'

    def update(self, instance, validated_data):
        personInstance = People.objects.update(**validated_data)
        return personInstance
