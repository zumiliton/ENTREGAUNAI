# Generated by Django 4.2.7 on 2023-11-09 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sanburgerapp', '0011_alter_usuarios_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]