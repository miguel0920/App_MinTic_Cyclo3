from tkinter.messagebox import NO
from unicodedata import name
from webbrowser import get

# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from fedemy.models.packages import Packages
from fedemy.serializers.packagesSerializer import PackagesSerializer

class PackageViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated] 

    """
    A viewset that provides the standard actions
    """

    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer

    @action(detail=True, methods=['post'], name='Create package')
    def create_package(self, request, pk=None):
        serializer = PackagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create package'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)