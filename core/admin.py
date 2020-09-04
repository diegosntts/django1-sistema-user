from django.contrib import admin

from .models import Produto, Cliente, Usuario, Cadastro

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone')
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'endereco', 'cidade')
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cadastro, CadastroAdmin)
