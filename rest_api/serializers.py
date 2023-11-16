# Serializers são responsáveis por converterem os dados como instâncias de Models e/ou querysets para o formato JSON ou outros formatos.
# O serializer também faz o caminho oposto, ou seja, ele também converte de JSON ou outros formatos para instâncias e querysets. 
# from termios import CDSUSP

from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField, ValidationError

from reserva.models import ReservaDeBanho, Petshop
from petapp.models import Contato
from reserva.models import ReservaDeBanho

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

class PetshopNesteModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'
        
class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopNesteModelSerializer(read_only=True) 
    class Meta:
        model = ReservaDeBanho
        fields = '__all__'           
        
class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'        
        

                