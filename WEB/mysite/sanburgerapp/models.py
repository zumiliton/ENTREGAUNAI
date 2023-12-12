from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.




# class Usuarios(models.Model):
# 	USERNAME_FIELD = 'usuario'
# 	REQUIRED_FIELDS = ['usuario']
# 	usuario=models.CharField(max_length=40,default="usuario")
# 	contrasena=models.CharField(max_length=40,default="contrasena")
# 	dni=models.CharField(max_length=8)
# 	nombre=models.CharField(max_length=20)
# 	apellido=models.CharField(max_length=20)
# 	edad=models.IntegerField()
# 	correo=models.CharField(max_length=40)
# 	telefono=models.IntegerField()
# 	domicilio=models.CharField(max_length=50)
# 	numero_tarjeta=models.IntegerField()
# 	titular_tarjeta=models.CharField(max_length=30)
# 	caducidad_tarjeta=models.DateField()
# 	cvv_tarjeta=models.IntegerField()
# 	password_tarjeta=models.CharField(max_length=20)
User = get_user_model()

class Usuarios(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)  # Clave foránea que apunta al modelo de usuario personalizado
	dni=models.CharField(max_length=8)
	edad=models.IntegerField()
	telefono=models.IntegerField()
	correo=models.CharField(max_length=30,default="sin correo")
	domicilio=models.CharField(max_length=50)
	numero_tarjeta=models.IntegerField()
	titular_tarjeta=models.CharField(max_length=30)
	caducidad_tarjeta=models.DateField()
	cvv_tarjeta=models.IntegerField()
	password_tarjeta=models.CharField(max_length=20)

# Create your models here.

class Calidad_Establecimiento(models.Model):
	nombre=models.CharField(max_length=20)
class Categoria_Producto(models.Model):
	nombre=models.CharField(max_length=20)
#no generamos clave de establecimiento,usamos gestion django
#no habra dos restaurantes que se llamen igual
class Establecimiento(models.Model):
	calidad_establecimiento=models.ForeignKey(Calidad_Establecimiento,on_delete=models.SET_NULL,null=True)
	nombre_establecimiento=models.CharField(max_length=50)
	ubicacion=models.CharField(max_length=50)
	hora_apertura=models.TimeField()
	hora_cierre=models.TimeField()

#PONEMOS CATEGORIA COMOA TRIBUTO DEL PRODUCTO,Y LUEGO FILTRAMOS EN EL TEMPLATe

def default_image():
	return "static/IMAGES/san_logo.png"

class Producto(models.Model):
	#Si eliminamos bar eliminamos producto
	establecimiento=models.ForeignKey(Establecimiento,on_delete=models.CASCADE)
	nombre_producto=models.CharField(max_length=50)
	pan=models.CharField(max_length=50)
	carne=models.CharField(max_length=50)
	salsa=models.CharField(max_length=50)
	queso=models.CharField(max_length=50)
	lechuga=models.BooleanField()
	categoria=models.ForeignKey(Categoria_Producto,on_delete=models.SET_NULL,null=True)
	precio=models.DecimalField(decimal_places=3,max_digits=5)
	picture=models.ImageField(upload_to='static/IMAGES/products/',null=True)
#En la foreing key creo que se puede poner mas de un producto
#dentro de producto
#>>> r.article_set.all()-->Hacemos asignacion clasica y podemos ver
#con esto cuantos productos hay en nuestro pedido

class Pedido(models.Model):
	producto=models.JSONField(null=True, blank=True)
	establecimiento=models.ForeignKey(Establecimiento,on_delete=models.SET_NULL,null=True)
	hora_pedido=models.TimeField()
	fecha_pedido=models.DateField()
	precio_pedido=models.DecimalField(decimal_places=3,max_digits=5)
	usuario=models.ForeignKey(Usuarios,on_delete=models.CASCADE,default=None)
	



