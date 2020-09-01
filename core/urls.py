from django.urls import path
from .views import index, contato, login, cadastro, conteudo, produto
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('conteudo', conteudo, name='conteudo'),
    path('produto/<int:pk>', produto, name='produto'),
]
