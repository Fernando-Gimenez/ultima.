from django import forms
from petapp.models import Contato
from petapp.models import ReservaDeBanho

# Forms: São classes Python que irão fazer as validações dos dados enviados pelos usuários para o sistema, através de formulários nas páginas

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        
    # qunado importamos os models nnão precisamos mais usar a estrutura abaixo. em vez de exportamos de 'Form' importamos de 'ModelForm' na classe     
    # nome = forms.CharField()
    # email = forms.EmailField()
    # mensagem = forms.CharField(widget=forms.Textarea)
    
class ReservaDeBanho(forms.ModelForm):
    class Meta:
        model = ReservaDeBanho
        fields = ['nomeDoPet', 'telefone', 'diaDaReserva', 'observacoes']
        # labels = sao os tratamentos do forms como são apresentados ao usuario
        # labels = {
        #    'nomeDoPet': 'Nome do PET',
        #    'telefone': 'Telefone',
        #    'diaDaReserva': 'Dia da Reserva',
        #    'observacoes': 'Observações'
        #}
        widgets = {
            'diaDaReserva': forms.DateInput(attrs={'type': 'date'})
        }
    
    # nomeDoPet = forms.CharField(label= 'Nome do PET')
    # telefone = forms.CharField(label= 'Telefone')
    # diaDaReserva = forms.DateField(label= 'Dia da Reserva',
                                # widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # observacoes = forms.CharField(label= 'Observações',
                                # widget=forms.Textarea)    