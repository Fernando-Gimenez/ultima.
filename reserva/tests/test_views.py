from pytest_django.asserts import assertTemplateUsed

def test_reserva_criar_deve_retornar_tamplate_correto(client):
    response = client.get('/reserva/criar/')
    
    assert response.status_code == 200 # testara o status code da pagina
    assertTemplateUsed(response, 'reserva_de_banho.html') # testara se o tamplate esta correto