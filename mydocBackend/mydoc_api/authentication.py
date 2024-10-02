import firebase_admin
from firebase_admin import auth
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        id_token = request.headers.get('Authorization')
        if not id_token:
            return None
        
        if id_token.startswith('Bearer '):
            id_token = id_token.split(' ')[1]

        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            user = User.objects.get(username=uid)
            return (user, None)
        except auth.InvalidIdTokenError:
            raise AuthenticationFailed('Invalid ID token')
        
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            user = User.objects

        return (user, None)