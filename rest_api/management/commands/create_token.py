from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token # usado para importar o Token criado


class Command(BaseCommand):
    help = 'Criar um Token para o Usuário'
    # vai definir usuario e senha
    def add_arguments(self, parser): # para que possamos criar um novo usuário e token. Para adicionarmos estes parâmetros, devemos declarar uma nova função chamada add_arguments 
                                     # que recebe um parâmetro chamado parser para que no corpo da função possamos adicionar quais parâmetros gostaríamos que fossem passados para o comando:
        parser.add_argument('--usuario', required=True) #significa que o usuário tem que existir é obrigatório 
        parser.add_argument('--senha', required=True)  #significa que a senha tem que existir é obrigatório
        
    def handle(self, *args, **options):
        usuario = options['usuario']
        senha = options['senha']
        
        # printando Usuario
        self.stdout.write(
            self.style.WARNING(f'criando usuario {usuario} com senha {senha}')
        )
        
        user = User(username=usuario)
        user.set_password(senha)
        user.save()
        
        # salvando informações no banco de dados
        token = Token.objects.create(user=user)
        
        # printando senha gerada
        self.stdout.write(
            self.style.WARNING(f'usuario Criado')
        )
        
        # printando Toke no terminal
        self.stdout.write(
            self.style.WARNING(f'Token: {token}')
        )
        
#PARA EXECUTAR O COMANDO TEMOS QUE EXECUTAR O NOME DO ARQUIVO, NESTE CASO (create_token) python .\manage.py create_token  depois passamos os parametros:
# --usuario{digite o nome} e --senha {digite a senha}   ou   python manage.py create_token--username NOME_USUARIO--password SENHA_USUARIO
#LEMBRADO QUE A PASTA DEVE ESTAR DENTRO DA PASTA commands