# Generated by Django 4.2.7 on 2023-11-13 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0015_remove_usuarios_apellido_remove_usuarios_correo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sanburgerapp.usuarios'),
        ),
    ]