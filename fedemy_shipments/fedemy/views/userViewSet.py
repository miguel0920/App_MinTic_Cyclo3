from tkinter.messagebox import NO
from unicodedata import name
from webbrowser import get
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from fedemy.models.user import User
from fedemy.serializers.userSerializer import UserSerializer

class UserViewSet(viewsets.ViewSet):
    """
    A viewset that provides the standard actions
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'], name='Create user')
    def create_user(self, request, pk=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create user'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], name='Get Users')
    def users(self, request, pk=None):
        recent_users = User.objects.all()
        serializer = UserSerializer(recent_users, many=True)
        return Response(serializer.data)
