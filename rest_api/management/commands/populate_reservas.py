from django.core.management.base import BaseCommand
from model_bakery import baker # biblioteca para popular banco de dados = model_bakery

from reserva.models import ReservaDeBanho
# aqui populamos nossas tabelas para adicionar dados FAKES ao nosso banco de dados para testes.
class Command(BaseCommand):
    help = 'criar reservas fake para aplicação'
    
    def handle(self, *args, **options):
        quantidade = 20
        
        self.stdout.write(
            self.style.WARNING(f'Gerando {quantidade} reservas fake')
        )
        
        for i  in range(quantidade):
            reserva = baker.make(ReservaDeBanho)
            reserva.save()
            self.stdout.write(
                self.style.WARNING(f'criada a reserva de número{i +1}')
            )
            
        self.stdout.write(
            self.style.SUCCESS('reservas criadas com sucesso')
        )