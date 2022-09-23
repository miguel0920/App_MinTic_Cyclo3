# Django REST Framework
from rest_framework import serializers

# Models
from fedemy.models.usercompanies import UserCompanies

class UserCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompanies  
        fields = '__all__'