# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from fedemy.models.people import People
from fedemy.serializers.peopleSerializer import PeopleSerializer

from django.http import Http404
import datetime

class PeopleViewSet(APIView):
    permission_classes = [IsAuthenticated]

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        pk = self.get_object(pk)
        print(datetime.datetime.now())
        request = request.data
        pk.personfirstname = request.get('personfirstname', pk.personfirstname)
        pk.personsecondname = request.get('personsecondname', pk.personsecondname)
        pk.personlastname = request.get('personlastname', pk.personlastname)
        pk.personrsecondlastname = request.get('personrsecondlastname', pk.personrsecondlastname)
        pk.personaddress = request.get('personaddress', pk.personaddress)
        pk.personphone = request.get('personphone', pk.personphone)
        pk.personemail = request.get('personemail', pk.personemail)
        pk.updatedatetime = request.get('updatedatetime', datetime.datetime.now().date())
        pk.save()
        serializer = PeopleSerializer(pk)
        return Response(serializer.data)
