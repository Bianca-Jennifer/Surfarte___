# Generated by Django 2.2.12 on 2022-04-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
