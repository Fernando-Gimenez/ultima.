# Generated by Django 4.2.4 on 2023-08-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaDeBanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoPet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('diaDaReserva', models.DateField()),
                ('observacoes', models.TextField(blank=True)),
            ],
        ),
    ]
