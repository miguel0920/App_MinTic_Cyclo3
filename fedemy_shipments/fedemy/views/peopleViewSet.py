# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from fedemy.models.people import People
from fedemy.serializers.peopleSerializer import PeopleSerializer

from django.http import Http404
import datetime

from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination): #check pagination, Example: https://medium.com/@fk26541598fk/django-rest-framework-apiview-implementation-pagination-mixin-c00c34da8ac2
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class PeopleViewSet(APIView, CustomPagination):
    permission_classes = [IsAuthenticated]

    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    pagination_class = CustomPagination #check pagination

    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def get(self, request):
        objects = People.objects.filter(
            isactive=True).order_by('-createdatetime')
        serializer = PeopleSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        pk = self.get_object(pk)
        request = request.data
        pk.personfirstname = request.get('personfirstname', pk.personfirstname)
        pk.personsecondname = request.get(
            'personsecondname', pk.personsecondname)
        pk.personlastname = request.get('personlastname', pk.personlastname)
        pk.personrsecondlastname = request.get(
            'personrsecondlastname', pk.personrsecondlastname)
        pk.personaddress = request.get('personaddress', pk.personaddress)
        pk.personphone = request.get('personphone', pk.personphone)
        pk.personemail = request.get('personemail', pk.personemail)
        pk.updatedatetime = request.get(
            'updatedatetime', datetime.datetime.now().date())
        pk.save()
        serializer = PeopleSerializer(pk)
        return Response(serializer.data)

    def delete(self, request, pk):
        pk = self.get_object(pk)
        request = request.data
        pk.updatedatetime = request.get(
            'updatedatetime', datetime.datetime.now().date())
        pk.isactive = request.get('isactive', False)
        pk.save()
        return Response(status=status.HTTP_200_OK)
