from django.urls import path
from .views import index, contato, login, conteudo, produto, cadastro, usuario
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('login', login, name='login'),
    path('conteudo', conteudo, name='conteudo'),
    path('produto/<int:pk>', produto, name='produto'),
    path('cadastro', cadastro, name='cadastro'),
    path('usuario', usuario, name='usuario')
]
