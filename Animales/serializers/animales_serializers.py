from rest_framework import serializers
from Animales.models import Animal, Encontrados, Perdidos, Favoritos

# Adoptados
class AdoptadoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None

# Encontrados
class EncontradoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Encontrados
        fields = ['id', 'nombre', 'localizacion', 'slug', 'categoria', 'imagen']

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None

# Perdidos
class PerdidoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Perdidos
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None

# Favoritos
class FavoritoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Favoritos
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None
