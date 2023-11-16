from typing import Any
from django.core.management import BaseCommand 
from reserva.models import Petshop, ReservaDeBanho
import random

class Command(BaseCommand):
    help = 'Sorteia reservas de forma automatica'
    
    def list_petshop(self):
        return Petshop.objects.all().values_list('pk', flat=True) # pk primary key do pet shop neste caso   
    
    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs="?",
            default=5,
            type=int,
            help='Quantidade de reservas a serem Sorteadas'
        )
        
        parser.add_argument(
            '-petshop',
            required=True, # required significa que o valor tem obrigatoriamente ser informado
            type=int,
            choices=self.list_petshop(),  # Choices=(opções)
            help='Id do petshop para Reserva'
        )    
        
    def escolher_reservas(self, lista_de_reservas_query_set, quantity):
        lista_de_reservas_list = list(lista_de_reservas_query_set) 
        
        if quantity > len(lista_de_reservas_list):
            quantity = len(lista_de_reservas_list) 
            
        return random.sample(lista_de_reservas_list, quantity)   
    
    def imprimir_petshop(self, petshop_id):
        self.stdout.write(
            self.style.HTTP_INFO('Dados do petshop que serão sorteadas as reservas')
        )
    
        petshop = Petshop.objects.get(pk=petshop_id)  
        self.stdout.write(f'{str(petshop)}') 
        self.stdout.write() # artificio utilizado para pular uma linha no comando via terminal

    def imprimir_reservas(self, reservas):
        self.stdout.write(
            self.style.HTTP_INFO('Reservas selecionadas')
        )
        
        self.stdout.write('=' * 35) # para dar uma separação no texto   
        
        for reserva in reservas:
            self.stdout.write(f'Nome do PET: {reserva.nomeDoPet}')
            self.stdout.write(f'Telefone do Tutor: {reserva.telefone}')
            self.stdout.write(f'Email do Tutor: {reserva.email}')
            self.stdout.write()
        
        self.stdout.write('=' * 35)
        
    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']
        
        reservas = ReservaDeBanho.objects.filter(petshop=petshop_id)
        
        reservas_escolhidas = self.escolher_reservas(reservas, quantity)
        self.stdout.write(
            self.style.SUCCESS('O sorteio foi concluido com sucesso!')
        )
           
        self.imprimir_petshop(petshop_id)   
        self.imprimir_reservas(reservas_escolhidas)    
