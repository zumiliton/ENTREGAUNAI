from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
import random
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from .models import Usuarios,Establecimiento,Calidad_Establecimiento,Producto,Pedido,Categoria_Producto
from .admin import CustomUserAdmin
from django.contrib.auth.models import User
from datetime import time
from datetime import datetime
from .utils import utils as utilidades
import time
import xml.etree.ElementTree as ET
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import FormularioUser

#MIS VARIABES
carrito=[]
payment=False
added_names=[]
finded=False


# Create your views here.

def prueba(request):
	return HttpResponse("Hello")
def home(request):
	return render(request,'general/home.html')

def contacto(request):
	if request.method == 'POST':
		comentario = request.POST.get('comentario')
		destinatario=request.POST.get('email')
		asunto=request.POST.get('asunto')
		print(utilidades.send_mail(comentario,destinatario,asunto))
		return HttpResponseRedirect(reverse('contacto'))
	return render(request, 'contacto/contacto.html')

def login_sanburger(request):
	if(request.user.is_authenticated==False):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			try:
				user = authenticate(request, username=username, password=password)		
			except Exception as e:
				return HttpResponse(e) 
			if(user is not None):
				login(request,user)
				return HttpResponseRedirect(reverse('calidad'))
				# return HttpResponse(request)
		return render(request,'user/login_user.html')
	else:
		return HttpResponseRedirect(reverse('calidad'))

def logout_sanburger(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

def add_proof(dni_newUser):
	if(Usuarios.objects.filter(dni=dni_newUser) is not None):
		return False
	return True



def user_register(request):
	if(request.user.is_authenticated==False):
		if request.method == 'POST':
			username=request.POST['username']
			password=request.POST['password']
			email=request.POST['email']
			first_name=request.POST['first_name']
			last_name=request.POST['last_name']
			dni=request.POST['dni']
			edad=request.POST['edad']
			telefono=request.POST['telefono']
			domicilio=request.POST['domicilio']
			numero_tarjeta=request.POST['numero_tarjeta']
			titular_tarjeta=request.POST['titular_tarjeta']
			caducidad_tarjeta=request.POST['caducidad_tarjeta']
			cvv_tarjeta=request.POST['cvv_tarjeta']
			password_tarjeta=request.POST['password_tarjeta']
			if((dni or edad or email or telefono or domicilio or numero_tarjeta or titular_tarjeta or caducidad_tarjeta or cvv_tarjeta or password_tarjeta) is None):
				return HttpResponse("datos vacios")
			else:
				if((authenticate(request, username=username, password=password) is None) and add_proof(dni)==False):
					usuario=User.objects.create_superuser(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
					custom_user = Usuarios.objects.create(
						user=usuario,
						dni=dni,
						edad=edad,
						telefono=telefono,
						correo=email,
						domicilio=domicilio,
						numero_tarjeta=numero_tarjeta,
						titular_tarjeta=titular_tarjeta,
						caducidad_tarjeta=caducidad_tarjeta,
						cvv_tarjeta=cvv_tarjeta,
						password_tarjeta=password_tarjeta)
					custom_user.save()
					return HttpResponseRedirect(reverse('calidad'))
				else:
					context={"error":True,
					"texto_error":"Lo siento,no se ha podido crear el usuario con los datos introducidos,prueba con otros"}
					return render(request,'user/user_register.html',context)
		return render(request,'user/user_register.html')
	else:
		return HttpResponseRedirect(reverse('calidad'))



def show_bars_categories(request):
	global carrito
	if(request.user.is_authenticated):
		carrito=[]
		try:
			categorias=Calidad_Establecimiento.objects.all()
		except Exception as e:
			raise e
		context={"lista_categorias":categorias}
		return render(request,"bares/bars_categories.html",context)
	else:
		return HttpResponseRedirect(reverse('home'))



def burgershop_view(request,categoria):
	global carrito
	if(request.user.is_authenticated):
		try:
			bares = Establecimiento.objects.filter(calidad_establecimiento__nombre=categoria.upper())
		except Exception as e:
			raise e
			time_format="%H:%M:%S"
		carrito=[]
		estados_bares={}
		hora_actual_objeto = datetime.now().time()
		hora_actual_str = hora_actual_objeto.strftime("%H:%M:%S")
		hora_actual_time = datetime.strptime(str(hora_actual_str), "%H:%M:%S").time()
		for b in bares:
			if(b.hora_cierre < hora_actual_time or hora_actual_time<b.hora_apertura):
				estados_bares[b]=False
			else:
				estados_bares[b]=True
				
		context={"establecimientos":estados_bares,
				"nombre_categoria":categoria}
		return render(request,'bares/show_bars.html',context)
	else:
		return HttpResponseRedirect(reverse('home'))


		
def show_types(request,establecimiento_pasado,categoria):
	if(request.user.is_authenticated):
		try:
			categorias_producto=Categoria_Producto.objects.all()
		except Exception as e:
			raise e
		context={
			"categorias_producto":categorias_producto,
			"establecimiento":establecimiento_pasado,
			"categoria":categoria,
			"carrito":carrito
		}
		return render(request,"productos/type_products.html",context)
	else:
		return HttpResponseRedirect(reverse('home'))

def mostrar_hamburgesas(request,establecimiento_pasado,categoria,tipo_producto):
	if(request.user.is_authenticated):
		try:
			burgers=Producto.objects.filter(establecimiento__nombre_establecimiento=establecimiento_pasado.upper(),categoria__nombre=tipo_producto)
		except Exception as e:
			raise e
		context={"burgers":burgers,
				"establecimiento":establecimiento_pasado,
				"categoria":categoria,
				"tipo_producto":tipo_producto,
				"carrito":carrito}
		return render(request,'productos/show_products.html',context)
	else:
		return HttpResponseRedirect(reverse('home'))

def show_selected_product(request,establecimiento_pasado,categoria,tipo_producto,selected_product):
	global carrito
	global payment
	if(request.user.is_authenticated):
		try:
			producto_seleccionado=Producto.objects.filter(establecimiento__nombre_establecimiento=establecimiento_pasado.upper(),categoria__nombre=tipo_producto,nombre_producto=selected_product)
		except Exception as e:
			raise e
		context={"producto":producto_seleccionado,"carrito":carrito,"establecimiento":establecimiento_pasado}
		return render(request,'productos/inside_product.html',context)
	else:
		return HttpResponseRedirect(reverse('home'))


@login_required
def actualizar_datos_usuario(request):
	usuario = request.user
	try:
		datosUsuario = Usuarios.objects.get(user=usuario)
		print(datosUsuario.user.username)
	except Usuarios.DoesNotExist:
		datosUsuario = Usuarios(user=usuario)
	if request.method == 'POST':
		formulario = FormularioUser(request.POST)
		if formulario.is_valid():
			for campo, valor_formulario in formulario.cleaned_data.items():
				print(f"{campo}-{getattr(datosUsuario,campo)}")
				# Verifica si el valor del formulario es diferente al valor actual antes de actualizar
				if(valor_formulario=='' or valor_formulario is None):
					continue
				else:
					if (getattr(datosUsuario, campo) != valor_formulario):
						setattr(datosUsuario, campo, valor_formulario)
					else:
						continue
			datosUsuario.save()
			return  HttpResponseRedirect(reverse('datos_usuario'))
	else:
		formulario = FormularioUser(instance=datosUsuario)
	return render(request, 'user/user_profile.html', {'formulario': formulario})

def limpiar_carro(request):
	global carrito
	global added_names
	print(f"Este es el de borrar:{carrito}")
	if(request.user.is_authenticated):
		if(request.method == 'POST'):
			carrito=[]
			added_names=[]
	return JsonResponse({})
			



def obtener_datos(request):
	global carrito
	global payment
	global added_names
	global finded
	print("incio")
	print(payment)
	if(payment):
		carrito=[]
		payment=False
	if(request.user.is_authenticated):
		if(request.method == 'POST'):
			# carrito_recibido = request.POST['0']
			if(len(carrito)==0):
				carrito.append(request.POST['0'])
				added_names.append(request.POST['0'].split(":")[0])
			else:	
				value_searched=(request.POST['0'])
				name_searched=value_searched.split(":")[0]
				if(name_searched in added_names):
					print(carrito)
					print("si esta")
					finded=True#no hace falta en principio
					for x in range(0,len(carrito)):
						if(carrito[x].split(":")[0]==name_searched):
							carrito.pop(x)
							carrito.append(value_searched)
				else:
					print(carrito)
					print("si no esta")
					carrito.append(request.POST['0'])
					added_names.append(request.POST['0'].split(":")[0])
		print("carrito")
		print(carrito)
	return JsonResponse({})


def pago(request,establecimiento_pasado):
	carrito_formateado={}
	filtered_user=Usuarios.objects.filter(user__username=request.user.username,user__password=request.user.password)[0]
	if(request.user.is_authenticated):
		global carrito
		global payment
		for valores in carrito:
			if(valores.split(":")[0] not in  carrito_formateado.keys()):
				carrito_formateado[valores.split(":")[0]]={}
			carrito_formateado[valores.split(":")[0]]['importe']=valores.split(":")[1]
			carrito_formateado[valores.split(":")[0]]['cantidad']=valores.split(":")[2]
			carrito_formateado[valores.split(":")[0]]['url']=valores.split(":")[3]

		context={"carrito":carrito_formateado,"establecimiento":establecimiento_pasado,"user":filtered_user}
		return render(request,"productos/chekout.html",context)

def pago_final(request,establecimiento_pasado):
	importe_total=0
	all_users=Usuarios.objects.all()
	all_establecimientos=Establecimiento.objects.all()
	#############################
	json_carrito=[]
	selected_user=None
	selected_bar=None
	ahora=timezone.now()
	hora_actual=ahora.time()
	dia_actual=ahora.date()
	#################################
	if(request.user.is_authenticated):
		global carrito
		global payment
		context={"carrito":carrito,"establecimiento":establecimiento_pasado}
		if(len(carrito)!=0):
			for c in carrito:
				importe_total+=float(c.split(":")[1])
				producto_json={"nombre":c.split(":")[0],"precio":c.split(":")[1],"cantidad":c.split(":")[2]}
				json_carrito.append(producto_json)
			for establecimiento in all_establecimientos:
				if (establecimiento.nombre_establecimiento==establecimiento_pasado):
					selected_bar=establecimiento
			for user in all_users:
				if(user.user.username==request.user.username):
					selected_user=user
					print(selected_user.user.username)

			pedido_creado=Pedido.objects.create(producto=json_carrito,establecimiento=selected_bar,hora_pedido=hora_actual,fecha_pedido=dia_actual,precio_pedido=importe_total,usuario=selected_user)
			pedido_creado.save()
		payment=True
		return render(request,"user/congrats.html",context)



def info(request):
	return render(request,"general/info.html")

def chat(request):
	return render(request,"user/index.html")