# Generated by Django 4.2.7 on 2023-11-14 12:21

from django.db import migrations, models
import sanburgerapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sanburgerapp', '0017_producto_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='picture',
            field=models.ImageField(default=sanburgerapp.models.default_image, upload_to='static/IMAGES/products/'),
        ),
    ]
