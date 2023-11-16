from django.contrib import admin

from reserva.models import ReservaDeBanho

# Register your models here.
@admin.register(ReservaDeBanho)
class ResevaDeBanhoAdmin(admin.ModelAdmin):
    list_display = ['nomeDoPet', 'email', 'diaDaReserva', 'observacoes', 'turno', 'tamanho', 'petshop' ]
    search_fields = ['nomeDoPet', 'email',]
    list_filter = ['diaDaReserva', 'turno', 'tamanho']