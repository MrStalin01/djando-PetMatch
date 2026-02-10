from rest_framework.views import APIView
from rest_framework.response import Response
from Animales.models import Animal, Encontrados, Perdidos, Favoritos
from Animales.serializers import AdoptadoSerializer, EncontradoSerializer, PerdidoSerializer, FavoritoSerializer

class AdoptadoListAPIView(APIView):
    def get(self, request):
        animales = Animal.objects.all()
        serializer = AdoptadoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

class EncontradoListAPIView(APIView):
    def get(self, request):
        animales = Encontrados.objects.all()
        serializer = EncontradoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

class PerdidoListAPIView(APIView):
    def get(self, request):
        animales = Perdidos.objects.all()
        serializer = PerdidoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)

class FavoritoListAPIView(APIView):
    def get(self, request):
        animales = Favoritos.objects.all()
        serializer = FavoritoSerializer(animales, many=True, context={'request': request})
        return Response(serializer.data)
