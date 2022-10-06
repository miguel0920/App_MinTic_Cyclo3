from rest_framework import generics
from rest_framework.response import Response

from fedemy.models.people import People

from fedemy.serializers.peopleSerializer import PeopleSerializer

class PeopleListViewSet(generics.ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        queryset = People.objects.all()
        persondocumentnumber = self.request.query_params.get('persondocumentnumber')
        if persondocumentnumber is not None:
            queryset = queryset.filter(persondocumentnumber=persondocumentnumber, isactive=True)
        return queryset
