from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto, Usuario, Cadastro
"""
Faz a requisição e retorna a redenrização dessa requisição com um templete
"""
def index(request):
    """Acessar atributos dos request"""
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)
def contato(request):
    return render(request, 'contato.html')
def login(request):
    return render(request, 'login.html')
def conteudo(request):
    return render(request, 'conteudo.html')
def produto(request, pk):
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf-8', status=404)
def error500(request):
    templete = loader.get_template('500.html')
    return HttpResponse(content=templete.render(), content_type='text/html; charset=utf-8', status=500)
def cadastro(request):
    return render(request, 'cadastro.html')
def usuario(request):
    usuarios = Usuario.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'usuarios': usuarios
    }
    return render(request, 'usuario.html', context)
def cadastro(request):
    cadastros = Cadastro.objects.all()
    context ={
        'cadastros': cadastros,
        'titulo': 'Programação Web com Django Framework'
    }
    return render(request, 'cadastro.html', context)