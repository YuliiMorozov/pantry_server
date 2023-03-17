from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class UserSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer


class UserEditProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser, ]
    # queryset = User.objects.all()    
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = User.objects.filter(id=pk)
        return queryset