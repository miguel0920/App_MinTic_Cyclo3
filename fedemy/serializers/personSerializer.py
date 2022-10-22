from rest_framework import serializers

# Models
from fedemy.models.people import People


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ['createdatetime', 'updatedatetime', 'isactive', 'personfirstname', 'personsecondname', 'personlastname', 'personrsecondlastname',
                  'personaddress', 'personphone', 'personemail', 'persondocumentnumber']
