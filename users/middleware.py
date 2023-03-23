# from datetime import datetime, timedelta
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import RefreshToken

# class UpdateTokenMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path == '/api/v1/token/':
#             response = self.get_response(request)
#             # print(response)
#             return response

#         # try:
#         #     auth_header = request.headers.get('Authorization', '').split()
#         #     print(auth_header)
#         #     if auth_header[0].lower() != 'bearer':
#         #         raise InvalidToken('Invalid token header. No Bearer token found.')
#         # except:
#         #     print('hi!')
            
#         #     access_token = auth_header[1]
#         #     # print(auth_header[1])
#         #     # print(access_token)
#         #     decoded_token = JWTAuthentication().get_validated_token(access_token)
#         #     # print(decoded_token)
#         #     expiry_time = datetime.fromtimestamp(decoded_token['exp'])
#         #     current_time = datetime.now()
#         #     if current_time + timedelta(minutes=1) > expiry_time:
#         #         refresh_token = RefreshToken(decoded_token['refresh'])
#         #         new_access_token = str(refresh_token.access_token)
#         #         request.headers['Authorization'] = 'Bearer ' + new_access_token
#         # except TokenError as e:
#         #     # Handle token error
#         #     pass
#         # response = self.get_response(request)
#         # return response
