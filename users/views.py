from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import views
from django.contrib.auth.models import User
from rest_framework import permissions
from users.serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework import status


class CreateUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer


class UserLoginView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

