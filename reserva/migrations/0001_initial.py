# Generated by Django 4.2.4 on 2023-08-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaDeBanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoPet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=70)),
                ('diaDaReserva', models.DateField()),
                ('observacoes', models.TextField(blank=True)),
                ('turno', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde')], max_length=10)),
                ('tamanho', models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')])),
            ],
            options={
                'verbose_name': 'Formulário de Reserva de Banho',
                'verbose_name_plural': 'Formulário de Reservas de Banho',
            },
        ),
    ]
