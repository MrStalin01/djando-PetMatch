from django.urls import path
from .views import AdoptadoListAPIView, EncontradoListAPIView, PerdidoListAPIView, FavoritoListAPIView

urlpatterns = [
    path('adoptados/', AdoptadoListAPIView.as_view(), name='adoptados-list'),
    path('encontrados/', EncontradoListAPIView.as_view(), name='encontrados-list'),
    path('perdidos/', PerdidoListAPIView.as_view(), name='perdidos-list'),
    path('favoritos/', FavoritoListAPIView.as_view(), name='favoritos-list'),
]
