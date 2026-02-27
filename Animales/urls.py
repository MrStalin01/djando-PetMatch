from django.urls import path
from .views.crear_animal import CrearAnimalAPIView
from .views import CrearAdoptadoAPIView, CrearEncontradoAPIView, CrearPerdidoAPIView
from .views.animales_view import (
    AdoptadoListAPIView,
    EncontradoListAPIView,
    PerdidoListAPIView,
    FavoritoDELListAPIView
)

urlpatterns = [
    path('adoptados/', AdoptadoListAPIView.as_view(), name='adoptados_list'),
    path('encontrados/', EncontradoListAPIView.as_view(), name='encontrados_list'),
    path('perdidos/', PerdidoListAPIView.as_view(), name='perdidos_list'),
    path('favoritos/', FavoritoDELListAPIView.as_view(), name='favoritos_list'),
    path('crear_animal/', CrearAnimalAPIView.as_view(), name='crear_animal'),  # POST
    path('crear_adoptado/', CrearAdoptadoAPIView.as_view(), name='crear_adoptado'),
    path('crear_encontrado/', CrearEncontradoAPIView.as_view(), name='crear_encontrado'),
    path('crear_perdido/', CrearPerdidoAPIView.as_view(), name='crear_perdido'),

]