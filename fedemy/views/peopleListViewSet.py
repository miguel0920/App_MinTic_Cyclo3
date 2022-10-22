from asyncio import constants
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from fedemy.models.people import People

from fedemy.serializers.peopleSerializer import PeopleSerializer
from fedemy.serializers.personSerializer import PersonSerializer

import datetime


class PeopleListViewSet(generics.ListAPIView):
    serializer_class = PeopleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = People.objects.all()
        persondocumentnumber = self.request.query_params.get(
            'persondocumentnumber')
        if persondocumentnumber is not None:
            queryset = queryset.filter(
                persondocumentnumber=persondocumentnumber, isactive=True)
        else:
            personid = self.request.query_params.get(
                'personid')
            queryset = queryset.filter(
                personid=personid, isactive=True)
        return queryset

    def post(self, request, format=None):
        request.data['createdatetime'] = datetime.datetime.now()
        request.data['isactive'] = True
        print(request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
