# Generated by Django 3.2 on 2024-11-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_ticket_ticket_numero_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_numero_cliente',
            field=models.CharField(max_length=50, verbose_name='Nombre usuario'),
        ),
    ]