from rest_framework import serializers
from Animales.models import Animal, Encontrados, Perdidos, Favoritos
from Animales.models.animal_model import MascotaPersonal


class AdoptadoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'raza', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None


class EncontradoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Encontrados
        fields = ['id', 'nombre', 'localizacion', 'slug', 'categoria', 'raza', 'imagen']

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None


class PerdidoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Perdidos
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'raza', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"

    def get_imagen(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None


class FavoritoSerializer(serializers.ModelSerializer):
    es_refugio_texto = serializers.SerializerMethodField()

    class Meta:
        model = Favoritos
        fields = ['id', 'nombre', 'duenyo', 'edad', 'localizacion', 'descripcion',
                  'slug', 'categoria', 'raza', 'es_refugio_texto', 'imagen']

    def get_es_refugio_texto(self, obj):
        return "Sí" if obj.es_refugio else "No"


# ... (deja tus otros serializers que ya tenías arriba intactos) ...

class CrearAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['nombre', 'duenyo', 'edad', 'localizacion', 'descripcion', 'categoria', 'raza', 'imagen', 'es_refugio']

# NUEVO: Para guardar en Encontrados
class CrearEncontradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encontrados
        # Nota: Me he basado en los campos que tenías en tu EncontradoSerializer.
        # Si en tu modelo de Encontrados hay más campos (como descripcion), añádelos aquí.
        fields = ['nombre', 'localizacion', 'categoria', 'raza', 'imagen']

# NUEVO: Para guardar en Perdidos
class CrearPerdidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perdidos
        fields = ['nombre', 'duenyo', 'edad', 'localizacion', 'descripcion', 'categoria', 'raza', 'imagen', 'es_refugio']


class MascotaPersonalSerializer(serializers.ModelSerializer):
   class Meta:
       model = MascotaPersonal
       fields = ['id', 'nombre', 'edad', 'raza', 'imagen', 'propietario']
       extra_kwargs = {'propietario': {'required': False, 'allow_null': True}}
