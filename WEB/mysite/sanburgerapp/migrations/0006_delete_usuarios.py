# Generated by Django 4.2.7 on 2023-11-07 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0005_rename_contrasena_usuarios_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
