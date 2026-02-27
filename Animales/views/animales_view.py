from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from ..serializers.animales_serializers import CrearAnimalSerializer, CrearEncontradoSerializer, CrearPerdidoSerializer
from rest_framework.generics import ListAPIView
from ..models import Animal, Encontrados, Perdidos, Favoritos
from rest_framework.generics import ListCreateAPIView
from ..serializers.animales_serializers import (
    AdoptadoSerializer,
    EncontradoSerializer,
    PerdidoSerializer,
    FavoritoSerializer
)
class CrearAdoptadoAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = CrearAnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok", "mensaje": "Adoptado creado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrearEncontradoAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = CrearEncontradoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok", "mensaje": "Encontrado creado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            print("Error en Encontrado:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrearPerdidoAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = CrearPerdidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok", "mensaje": "Perdido creado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            print("Error en Perdido:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdoptadoListAPIView(ListAPIView):
    serializer_class = AdoptadoSerializer

    def get_queryset(self):
        return Animal.objects.all()

class EncontradoListAPIView(ListAPIView):
    queryset = Encontrados.objects.all()
    serializer_class = EncontradoSerializer

class PerdidoListAPIView(ListAPIView):
    queryset = Perdidos.objects.all()
    serializer_class = PerdidoSerializer

# En tu archivo views.py de Django
# En tu archivo views.py de Django
class FavoritoListAPIView(ListCreateAPIView):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer  # <-- ESTA LÍNEA DEBE ESTAR BIEN IDENTADA
    parser_classes = (MultiPartParser, FormParser)