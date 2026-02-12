from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from ..serializers.animales_serializers import CrearAnimalSerializer

class CrearAnimalAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # Para recibir imagen + datos

    def post(self, request):
        serializer = CrearAnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok", "mensaje": "Animal creado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # esto muestra por qué falla
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
