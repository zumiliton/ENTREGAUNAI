# Generated by Django 4.2.7 on 2023-11-10 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0014_alter_usuarios_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='username',
        ),
    ]