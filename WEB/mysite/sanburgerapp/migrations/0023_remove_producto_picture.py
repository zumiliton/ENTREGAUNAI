# Generated by Django 4.2.7 on 2023-11-14 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0022_alter_producto_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='picture',
        ),
    ]
