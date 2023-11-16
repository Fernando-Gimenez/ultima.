from django.shortcuts import render
from reserva.models import Petshop
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from petapp.models import Contato
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_api.serializers import ReservaDeBanho, ContatoModelSerializer, PetshopNesteModelSerializer, PetshopModelSerializer
from rest_api.serializers import AgendamentoModelSerializer
from rest_framework.authentication import TokenAuthentication # forma de authentificação da API se o usuario nao estiver logado não pode auterar os dados
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
                                                                                # IsAdminUser permite que apenas o Admin altere os dados
                                                                                # IsAuthenticated verifica a authentificação LOGIN, SENHA e permite alterações caso logado
                                                                                # IsAuthenticatedOrReadOnly  permite apenas leitura dos dados para consumo da API


# feito no modelviewSet com serializer o modelviewSet. CRUD(Create/Criar, Read/ler, Update/Atualizar, Delete/Deletar):
class AgendamentoModelViewSet(ModelViewSet):
    queryset = ReservaDeBanho.objects.all()
    serializer_class = AgendamentoModelSerializer # adequa o codigo python pra ser consumido em uma API em JSON
    #authentication_classes = [TokenAuthentication] # forma de authentificação da API se o usuario nao estiver logado não pode auterar os dados
    permission_classes = [IsAuthenticated] # verifica a authentificação dos dados LOGIN, SENHA etc uma vez logado permite alterações na API
    
    
class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()    
    serializer_class = ContatoModelSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]  # IsAuthenticatedOrReadOnly  permite apenas leitura dos dados para consumo da API
    
class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopNesteModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]        

# toda API retorna um Json (dicionário em python por padrão do Django)
# feito manualmente sem o ModelviewSet
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        nome = request.data.get('nome')
        return Response({ 'mensagem': f'Óla, {nome}!!'})
    
    return Response({'Hello':'hello world!'})

@api_view(['GET'])
def listar_contatos(request):
    contatos = Contato.objects.all()
    contatosFormatados = []
    
    for contato in contatos:
        contatosFormatados.append({ 
            'nome': contato.nome, 
            'email': contato.email,
            'id': contato.id
            })
    
    return Response({ 'contato': contatosFormatados})

@api_view(['GET', 'PUT'])
def obter_contatos_pelo_id(request, id):
    contato = Contato.objects.filter(id=id)
    
    if len(contato) == 0:
        return Response({'mensagem': 'Id não encontrado'})
    
    contatoFormatado = {
        'nome': contato[0].nome,
        'email': contato[0].email,
        'id': contato[0].id
    }
        
    return Response({'contato': contatoFormatado })
    
    
