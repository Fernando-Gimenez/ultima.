from django.db import models
# Models: São as classes que representam uma tabela no banco de dados. Elas fazem a comunicação de Python com o banco de dados de uma forma mais abstrata
# (não precisamos escrever o código SQL para consultas, inserções, atualizações e remoções)

# para migrar os models para o banco de dados usamos o comando python manage.py makemigrations
# para persistir e realmente salvar no bd usamos posteriormente o comando python manage.py migrate

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True) # auto_now_add=True, vai armazenar o valor da data/hora inserido no banco de forma automática.
    lido = models.BooleanField(default=False, blank=True) # sempre no django o campo boleano 0 é falso e 1 é verdadeiro
    
    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'
    class Meta:
        # altera os nomes exibidos no formulario no django (no caso ele substituiu Contato por Formulario de Contato)
        verbose_name = 'Formulario de Contato'
        # isso serve tambem para nomes no plural o django faz essa definição altomaticamente
        
        # exibi qual vai ser o ordenação com que os dados serao apresentados (ex nome exibiria em ordem alfabetica e data exibiria os primeiros registros, se quiser inverter a ordem basta colocar o sinal de negativo na frente)
        ordering = ['data'] #[-data]
    
class ReservaDeBanho(models.Model):
    nomeDoPet = models.CharField(verbose_name= 'Nome do PET', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=15)
    diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
    observacoes = models.TextField(verbose_name='Observações', blank=True)
# quando definimos o verbose_name no Models não precisamos tratar as labels que estão no Forms e alem disto os nomes tratados no Models já ficam corretos no Django admin.