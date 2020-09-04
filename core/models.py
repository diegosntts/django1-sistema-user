from django.db import models

class Produto(models.Model):
     nome = models.CharField('Nome', max_length=100)
     preco = models.DecimalField('Preco', decimal_places=2, max_digits=9)
     estoque = models.DecimalField('Quantidade em Estoque', decimal_places=2, max_digits=9)
     def __str__(self):
          return self.nome

class Cliente(models.Model):
     nome = models.CharField('Nome', max_length=100)
     sobrenome = models.CharField('Sobrenome', max_length=100)
     email = models.EmailField('Email', max_length=100)
     def __str__(self):
          return self.nome

class Usuario(models.Model):
     nome = models.CharField('Nome', max_length=100)
     sobrenome = models.CharField('Sobrenome', max_length=100)
     telefone = models.DecimalField('Telefone', decimal_places=2, max_digits=9)
     def __str__(self):
          return self.nome
class Cadastro(models.Model):
     nome = models.CharField('Nome', max_length=100)
     sobrenome = models.CharField('Sobrenome', max_length=100)
     email = models.CharField('Email', max_length=100)
     endereco = models.CharField('endereco', max_length=100)
     cidade = models.CharField('cidade', max_length=100)
     def __str__(self):
          return self.nome