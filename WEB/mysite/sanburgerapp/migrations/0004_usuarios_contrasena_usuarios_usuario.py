# Generated by Django 4.2.7 on 2023-11-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0003_pedido_establecimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='contrasena',
            field=models.CharField(default='contrasena', max_length=40),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='usuario',
            field=models.CharField(default='usuario', max_length=40),
        ),
    ]