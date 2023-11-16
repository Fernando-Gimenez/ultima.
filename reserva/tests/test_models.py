import pytest
from reserva.models import ReservaDeBanho
# from pytest_django.asserts import assertTemplateUsed
# from model_bakery import baker  #biblioteca para popular banco de dados


def test_config():
    assert 1 == 1
    
# @pytest.mark.django_db    O recurso de marcar os testes nos ajuda a subir um banco de dados para testes e realizar as operações nele, depois disso o banco é excluído. 
#                           A vantagem é que não precisamos de dados reais e podemos utilizar os dados isolados para cada um dos nossos testes.
    