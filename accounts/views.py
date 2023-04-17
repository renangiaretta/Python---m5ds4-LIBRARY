from rest_framework.views import APIView, Response, Request, status

from accounts.models import Account
from accounts.serializers import AccountSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView_MODO_MANUAL(APIView):
    """
    1 - POST.
    2 - Validar as credenciais recebidas.
    3 - Retornar o token para o usuário.
    """
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response(
                {'detail': 'Invalid credentials'},
                status.HTTP_403_FORBIDDEN)
        refresh = RefreshToken.for_user(user)
        token_dict = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(token_dict, status.HTTP_200_OK)


class LoginView_MODO_AUTO_1(APIView):
    def post(self, request: Request) -> Response:
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status.HTTP_200_OK)


# class LoginView(TokenObtainPairSerializer):
#     ...


class AccountView(APIView):
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
