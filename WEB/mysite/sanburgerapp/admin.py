from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import User
from django.contrib import admin
from .models import  Establecimiento,Producto,Pedido,Calidad_Establecimiento,Categoria_Producto,Usuarios
from django.contrib.auth.admin import User,UserAdmin

class UsuariosInline(admin.StackedInline):
	model=Usuarios
	can_delete=False
	verbose_name_plural='Usuarios'
	fk_name='user'

class CustomUserAdmin(UserAdmin):
	inlines=(UsuariosInline,)
	list_display = ('username', 'password','email', 'first_name', 'last_name', 'is_staff', 'is_active')
	list_select_related=('usuarios',)

	def get_dni(self,instance):
		return instance.usuarios.dni
	get_dni.short_description='DNI'
	
	def get_inline_instances(self,request,obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin,self).get_inline_instances(request,obj)



admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
admin.site.register(Establecimiento)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Calidad_Establecimiento)
admin.site.register(Categoria_Producto)



