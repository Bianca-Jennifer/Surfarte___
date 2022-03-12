# Generated by Django 3.2 on 2022-03-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='detalhes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='numero',
            field=models.IntegerField(unique=True, verbose_name='Número'),
        ),
    ]
