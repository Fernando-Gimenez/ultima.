from django import forms
from datetime import date

from reserva.models import ReservaDeBanho


class ReservaDeBanhoForm(forms.ModelForm):
    class Meta:
        model = ReservaDeBanho
        fields = ['nomeDoPet', 'telefone', 'email', 'diaDaReserva', 'turno', 'tamanho', 'observacoes', 'petshop']
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
        
    def clean_diaDaReserva(self): # para personalizar a excessão usamos clean_ e o nome do campo 
        DiaDaReservaSelecionado = self.cleaned_data['diaDaReserva'] # self.cleaned é um atributo da classe self de um dicionario [] ele pega o valor do campo no caso ['diaDaReserva']
        hoje = date.today()  
        
        if DiaDaReservaSelecionado < hoje:
            raise forms.ValidationError('Não é possivel escolher esta Data')
        
        quantidadeParaODia = ReservaDeBanho.objects.filter(diaDaReserva=DiaDaReservaSelecionado).count()
        
        if quantidadeParaODia >= 2:
            raise forms.ValidationError('Quantidade Máxima do dia Atingida')
        
        return DiaDaReservaSelecionado    