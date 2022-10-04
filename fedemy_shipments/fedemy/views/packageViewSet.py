# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import (
    api_view, 
    permission_classes, 
    parser_classes, 
    throttle_classes, 
    renderer_classes,
)
from rest_framework import (
    permissions, 
    parsers, 
    throttling, 
    renderers,
)
from fedemy.models.packages import Packages
from fedemy.serializers.packagesSerializer import PackagesSerializer

class PackageViewSet(APIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer

    @api_view(['POST'])
    @permission_classes([permissions.IsAuthenticated])
    @parser_classes([parsers.JSONParser])
    @throttle_classes([throttling.UserRateThrottle])
    @renderer_classes([renderers.JSONRenderer])
    def create_package(self, request, format=None):
        serializer = PackagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create package'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)