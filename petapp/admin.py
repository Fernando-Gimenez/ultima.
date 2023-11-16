from django.contrib import admin
from django.contrib import messages #o django.contrib.messages. Ele é responsável por criar essas mensagens de sucesso que ficam no topo do site quando apagamos, adicionamos ou atualizamos algum registro no admin.
from petapp.models import Contato
# Admin: É o arquivo que irá indicar quais models ficarão disponíveis no painel administrativo gerado automaticamente pelo Django

@admin.action(description='Marcar como lido')
def marcar_como_lido(modeladmin, request, queryset): # um "queryset" é um conceito que se refere a uma coleção de registros (ou linhas) de um banco de dados.
    queryset.update(lido=True)
    modeladmin.message_user(request, 'formularios marcados como lido', messages.SUCCESS)

@admin.action(description='Marcar como não lido')
def marcar_como_nao_lido(modeladmin, request, queryset): # um "queryset" é um conceito que se refere a uma coleção de registros (ou linhas) de um banco de dados.
    queryset.update(lido=False)
    modeladmin.message_user(request, 'formularios marcados como não lido', messages.SUCCESS)

# decorator para registro
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    # list_display manipula quais models queremos mostrar no modo admin
    list_display = ['nome', 'email', 'mensagem', 'data', 'lido']
    # search_fields define os campos a serem filtrados
    search_fields = ['nome', 'email']
    # filtro mais especifico e pré determinado no django
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]
    

        