from django.db import models

class ReservaDeBanho(models.Model):
    TAMANHO_OPCOES = ( #tupla
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )
    TURNO_OPCOES =( #tupla
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    )
    # o django cria automaticanente o id primary key 
    nomeDoPet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(verbose_name= 'Telefone', max_length=15)
    email = models.EmailField(verbose_name='E-mail', max_length=70)
    diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
    observacoes = models.TextField(verbose_name='Observações', blank=True)
    turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=10)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    petshop = models.ForeignKey(
        'Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
    
    
    
    class Meta:
        verbose_name = 'Formulário de Reserva de Banho'
        #verbose_name_plural = 'Formulários de Reservas de Banho'

    def __str__(self):
        return f'Nome: {self.nomeDoPet} - Email: {self.email} - Dia: {self.diaDaReserva} - Turno: {self.turno}'
    
    
    
class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=30)
    def __str__(self):
        return f'Petshop: {self.nome} - Rua: {self.rua}'
