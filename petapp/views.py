from django.shortcuts import render
from petapp.forms import ContatoForm
from petapp.forms import ReservaDeBanho
from petapp.models import Contato

# Views: São as funções Python que irão indicar quais funcionalidades têm o sistema, elas irão responder pelas rotas definidas no sistema

# Create your views here.

def inicio(request): # toda view tem que ter um request
    return render(request, 'inicio.html')

def contato(request):
    # print('metodo: ',request.method)
    sucesso = False
    
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome'] #form.cleaned_data é um dicionário que contém os valores dos campos do formulário que passaram na validação. Cada chave no dicionário corresponde a um campo do formulário e o valor associado a essa chave é o valor validado e limpo desse campo.
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem) #Ao chamar a propriedade Contato.objects, temos acesso a algumas funções, 
                                                                              #uma delas (o create) serve para salvar uma nova informação. Para isso,  basta passar como parâmetro o nome do campo e o valor.
            sucesso = True
          
    
    context = {
        'nome': 'fernando',
        'telefone': '(11)94736-8856',
        'form': form,
        'sucesso': sucesso
    }
    
    return render(request, 'contato.html', context)


def reservaDeBanho(request):
    sucesso = False
       
    # formulario igual ao de 'Contato' porem mais simplificado sem o IF e ELSE, e sem passar os parametros do Form.   
    form = ReservaDeBanho(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True   
            
    context = {
        'form': form,
        'sucesso': sucesso  
    }         
    
    return render (request, 'reserva_de_banho.html', context)