from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatoViewSet, FormularioAdopcionViewSet, VisitaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'candidatos', CandidatoViewSet)
router.register(r'formularios', FormularioAdopcionViewSet)
router.register(r'visitas', VisitaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
#urlpatterns = [
#    path('', inicio, name='inicio'),
#]