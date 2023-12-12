# Generated by Django 4.2.7 on 2023-11-03 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calidad_establecimiento', models.CharField(max_length=20)),
                ('nombre_establecimiento', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('hora_apertura', models.TimeField()),
                ('hora_cierre', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('correo', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('domicilio', models.CharField(max_length=50)),
                ('numero_tarjeta', models.IntegerField()),
                ('titular_tarjeta', models.CharField(max_length=30)),
                ('caducidad_tarjeta', models.DateField()),
                ('cvv_tarjeta', models.IntegerField()),
                ('password_tarjeta', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('pan', models.CharField(max_length=50)),
                ('carne', models.CharField(max_length=50)),
                ('salsa', models.CharField(max_length=50)),
                ('queso', models.CharField(max_length=50)),
                ('lechuga', models.BooleanField()),
                ('categoria', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=5)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanburgerapp.establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_pedido', models.TimeField()),
                ('fecha_pedido', models.DateField()),
                ('precio_pedido', models.DecimalField(decimal_places=3, max_digits=5)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanburgerapp.producto')),
            ],
        ),
    ]
