# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from fedemy.models.user import User
from fedemy.serializers.userSerializer import UserSerializer
from fedemy.serializers.userSerializer import UserLoginSerializer

class UserViewSet(APIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, pk=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create user'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def getusers(self, request, pk=None):
        recent_users = User.objects.all()
        serializer = UserSerializer(recent_users, many=True)
        return Response(serializer.data)

    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid(raise_exception=True):
            user, token = serializer.save()
            data = {
                'user': UserLoginSerializer(user).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_401_UNAUTHORIZED)

        