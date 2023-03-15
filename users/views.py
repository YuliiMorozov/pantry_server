from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from rest_framework import generics


class UserRegister(generics.CreateAPIView):
    serializer_class = UserSerializer


# class UserRegister(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, format=None):
        
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# from django.contrib.auth.models import User
# from rest_framework import viewsets, permissions
# from .serializers import UserSerializer
# from .services import users


# # User Viewset
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UserSerializer




# from django.shortcuts import render
# # from services import register

# from django.http import HttpResponse



# def sign_up(request):
#     # return register(request)
#     pass

# def sign_in(request):
#     pass

# def sign_out(request):
#     pass

# def index(request):
#     return HttpResponse('Hello!')