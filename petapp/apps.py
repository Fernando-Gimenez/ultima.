from django.apps import AppConfig


class PetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petapp'
    
    # 'verbose_name' sempre que queremos mudar visual para o usuário no painel de controle do django usamos essa palavra reservada
    