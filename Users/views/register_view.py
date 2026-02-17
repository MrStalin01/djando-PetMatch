"""
Descargamos:
    - djangorestframework
    - djangorestframework-simplejwt
    - django-cors-headers

    comandos:
        - pip install djangorestframework
        - pip install djangorestframework-simplejwt
        - pip install django-cors-headers

    Métodos de solicitudes:
        - get -> Genérico, pero no encripta datos
        - post -> Genérico y encripta datos
        - put -> Crear elementos y funciona a través de POST
        - patch -> Lo utilizamos para actualizar uno o varios valores, pero no todos y funciona con POST.
        - delete -> Funciona con POST lo unico que este se utiliza solo para borrar datos
"""
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Users.serializers import RegisterSerializer

from Users.models import User
from Users.serializers import RegisterSerializer


from rest_framework.permissions import IsAuthenticated

class PruebaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuarios3 = User.objects.filter(
            is_active=True,
            is_staff=True
        ).order_by("-first_name")

        data2 = [
            {
                "email": usuario.email,
                "first_name": usuario.first_name,
                "last_name": usuario.last_name
            }
            for usuario in usuarios3
        ]

        return Response(
            {"success": True, "data": data2},
            status=status.HTTP_200_OK
        )



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # 🔐 Generar token
            refresh = RefreshToken.for_user(user)

            return Response({
                "success": True,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)