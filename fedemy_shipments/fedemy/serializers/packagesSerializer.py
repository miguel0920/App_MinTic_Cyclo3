# Django REST Framework
from rest_framework import serializers

# Models
from fedemy.models.packages import Packages
from fedemy.models.packagetypes import PackageTypes
from fedemy.models.usercompanies import UserCompanies


class PackagesSerializer(serializers.ModelSerializer):
    usercompanyid = serializers.SlugRelatedField(
        queryset=UserCompanies.objects.all(), slug_field='usercompanyid')
    packagetypeid = serializers.SlugRelatedField(
        queryset=PackageTypes.objects.all(), slug_field='packagetypeid')

    class Meta:
        model = Packages
        fields = ['packageid', 'usercompanyid', 'packagetypeid', 'packagedescription',
                  'packageprice', 'packagequantity', 'createdatetime', 'isactive']

    def create(self, validated_data):
        packageInstance = Packages.objects.create(**validated_data)
        return packageInstance

    def getPackages():
        users = Packages.objects.all()
        return users
