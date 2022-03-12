# Generated by Django 3.2 on 2022-03-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20220307_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FRESHMAN', max_length=2),
        ),
    ]