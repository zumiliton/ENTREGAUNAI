# Generated by Django 4.2.7 on 2023-11-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0021_alter_producto_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/IMAGES/products/'),
        ),
    ]