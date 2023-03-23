from rest_framework import serializers
from django.contrib.auth.models import User
from .validators import (
    validate_username, 
    validate_email,
    validate_password,
)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        # do not return password after create new user
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    username = serializers.CharField(validators=[validate_username])
    email = serializers.CharField(validators=[validate_email])
    password = serializers.CharField(
        write_only=True,
        min_length = 8,
        max_length = 16,
        style={'input_type': 'password'},
    )
# ???
    def create(self, validated_data):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']

        user.set_password(password)
        user.save()

        return user




        

    




# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .validators import (
#     validate_username, 
#     validate_email,
#     validate_password,
# )

# # User Serializer
# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['id', 'email', 'username', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     username = serializers.CharField(validators=[validate_username])
#     email = serializers.CharField(validators=[validate_email])
#     password = serializers.CharField(
#         write_only=True,
#         min_length = 8,
#         max_length = 16,
#         style={'input_type': 'password'},
#     )

    

#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#         )
#         password=self.validated_data['password']

#         user.set_password(password)
#         # try
#         user.save()

#         return user


#     # def validate(self, data):
#     #     password = data.get('password')
#     #     password2 = data.pop('password2', None)

#     #     if password != password2:
#     #         raise serializers.ValidationError('Passwords do not match')

#     #     return data