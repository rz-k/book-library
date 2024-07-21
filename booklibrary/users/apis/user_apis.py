from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from booklibrary.users.services.user_services import UserService
from drf_spectacular.utils import extend_schema

from booklibrary.users.serializers.user_serializers import (
    InputRegisterSerializer, 
    OutPutRegisterSerializer
)

from booklibrary.users.services.user_services import (
    UserService,
)


@extend_schema(tags=['users'])
class RegisterApi(APIView):
    @extend_schema(request=InputRegisterSerializer, responses=OutPutRegisterSerializer)
    def post(self, request):
        serializer = InputRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = UserService.user_create(
                username=serializer.validated_data.get("username"),
                password=serializer.validated_data.get("password")
                )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(OutPutRegisterSerializer(user, context={"request":request}).data)
