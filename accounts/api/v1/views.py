from django.contrib.auth import get_user_model
from .serializers import AccountSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

user_model = get_user_model()

class CreateAccountView(CreateAPIView):
    model = get_user_model()
    serializer_class = AccountSerializer
    permission_classes = (AllowAny, )

class ListAccountView(ListAPIView):
    model = get_user_model()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return user_model.objects.filter(username=self.request.user.username)

class Logout(APIView):
    def get_queryset(self):
        return user_model.objects.filter(username=self.request.user.username)

    def get(self, request, format=None):
        self.request.user.auth_token.delete()
        return Response({"detail": "You have been successfully logged out."}, status=status.HTTP_200_OK)