from django.shortcuts import render

from reserva.forms import ReservaDeBanhoForm


# Create your views here.
def criar_reserva_banho(request):
    sucesso = False
       
    # formulario igual ao de 'Contato' porem mais simplificado sem o IF e ELSE, e sem passar os parametros do Form.   
    form = ReservaDeBanhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True   
            
    context = {
        'form': form,
        'sucesso': sucesso  
    }         
    
    return render (request, 'reserva_de_banho.html', context)