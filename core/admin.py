from django.contrib import admin
from .models import Servico, Cargo, Funcionario, Recurso, Plano, Cliente

# Register your models here.

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo','modificado')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','ativo','modificado')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'ativo', 'modificado')

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('plano','preco','icone','ativo','modificado')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','ativo','modificado')