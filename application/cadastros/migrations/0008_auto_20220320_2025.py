# Generated by Django 2.2.12 on 2022-03-20 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_auto_20220320_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
