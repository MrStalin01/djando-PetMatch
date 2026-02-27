from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser

from ..models.animal_model import MascotaPersonal
from ..serializers.animales_serializers import CrearAnimalSerializer, CrearEncontradoSerializer, CrearPerdidoSerializer, \
    MascotaPersonalSerializer
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

class FavoritoListAPIView(ListCreateAPIView):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer
    parser_classes = (MultiPartParser, FormParser)


class FavoritoDELListAPIView(APIView):

    def delete(self, request):
        # Obtenemos los parámetros de la URL (Query Params)
        nombre = request.query_params.get('nombre')
        duenyo = request.query_params.get('duenyo')

        if not nombre or not duenyo:
            return Response(
                {"error": "Se requiere nombre y dueño para eliminar"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Buscamos el favorito que coincida
        favorito = Favoritos.objects.filter(nombre=nombre, duenyo=duenyo).first()

        if favorito:
            favorito.delete()
            return Response({"message": "Eliminado de favoritos"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "No se encontró el animal en favoritos"}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        animales = Favoritos.objects.all()
        serializer = FavoritoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):

        serializer = FavoritoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MascotaPersonalListAPIView(generics.ListCreateAPIView):
   queryset = MascotaPersonal.objects.all()
   serializer_class = MascotaPersonalSerializer
   permission_class = [AllowAny]
