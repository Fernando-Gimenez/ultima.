from django.urls import path

from rest_api.views import * # o * importa todas as views (hello_world, listar_contatos, obter_contatos_pelo_id)
from rest_framework.routers import SimpleRouter #SimpleRouter por padrão adiciona uma “/” no final da URL
from rest_framework.routers import DefaultRouter # DefaultRouter faz uma 'lista' de todas as rotas da api


app_name = 'rest_api'

router = DefaultRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoModelViewSet)
router.register('petshop', PetshopModelViewSet)


urlpatterns = [
#   path('hello_world', hello_world, name='hello_world_api'),
#   path('contato', listar_contatos, name='listar_contatos'),
#   path('contato/<int:id>', obter_contatos_pelo_id, name='obter_contato')
    
]

urlpatterns += router.urls
# ou urlpatterns = urlpatterns + router.urls