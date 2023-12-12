from django.urls import path,re_path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('/login', views.login_sanburger, name='login'),
	path('/logout',views.logout_sanburger,name='logout'),
	path('/registro',views.user_register,name='registro'),
	path('/info',views.info,name='info'),
	path('/chat',views.chat,name='chat'),
	path('/contacto',views.contacto,name='contacto'),
	path('/calidad',views.show_bars_categories,name='calidad'),
	path('/<str:categoria>/bares', views.burgershop_view, name='bares'),
	path('/<str:categoria>/bares/<str:establecimiento_pasado>',views.show_types,name='tipos'),
	path('/<str:categoria>/bares/<str:establecimiento_pasado>/<str:tipo_producto>',views.mostrar_hamburgesas,name='burger'),
	path('/<str:categoria>/bares/<str:establecimiento_pasado>/<str:tipo_producto>/<str:selected_product>',views.show_selected_product,name='producto'),
	path('/perfil',views.actualizar_datos_usuario,name='datos_usuario'),
	path('/obtener_datos',views.obtener_datos,name='datos'),
	path('/pago/<str:establecimiento_pasado>',views.pago,name='pago'),
	path('/pago_final/<str:establecimiento_pasado>',views.pago_final,name='pago_final'),
	path('/limpiar_carro',views.limpiar_carro,name='carro')
	]
