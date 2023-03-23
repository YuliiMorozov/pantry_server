from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate

class UserSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer


# class UserSignIn(generics.CreateAPIView):
#     permission_classes = [AllowAny, ]
#     serializer_class = UserSerializer



class UserSignIn(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Incorrect credentials'}, status=status.HTTP_400_BAD_REQUEST)
        

            #     user = User.objects.filter(username=username).first()

    #     if user is None:
    #         raise AuthenticationFailed('User not found!')
        
    #     if not user.check_password(password):
    #         raise AuthenticationFailed('Incorrect password!')
        
    #     return Response({
    #         'message': 'success'
    #     })
        
class UserSignOut(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except:
            return Response({"message": "Invalid token"}, status=400)
        
        return Response({"message": "Successfully logged out"})



class UserEditProfile(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, ]
    # queryset = User.objects.all()    
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = User.objects.filter(id=pk)
        return queryset
    