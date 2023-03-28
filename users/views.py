from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate


class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserSignIn(APIView):
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


class UserSignOut(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

        except:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)



class UserEditProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    # queryset = User.objects.all()    
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = User.objects.filter(id=pk)
        return queryset
    

# class ForgotPasswordView(APIView):
#     permission_classes = [AllowAny,]
    
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

#         user = User.objects.filter(email=email).first()
#         if not user:
#             return Response({'error': 'User does not exist with this email.'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)