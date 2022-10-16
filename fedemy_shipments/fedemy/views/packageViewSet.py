# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from fedemy.models.packages import Packages
from fedemy.serializers.packagesSerializer import PackagesSerializer

import datetime

class PackageViewSet(APIView):
    permission_classes = [IsAuthenticated]

    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer

    def post(self, request, format=None):
        request.data['createdatetime'] = datetime.datetime.now().date()
        request.data['isactive'] = True
        serializer = PackagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create package'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)