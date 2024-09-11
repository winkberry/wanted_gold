from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # 유저 인증 후 JWT 토큰 발급
        return super().post(request, *args, **kwargs)