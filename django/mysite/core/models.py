from django.db import models

# Create your models here.


class Biblioteca(models.Model):
    titulo = models.CharField(max_length=50)
    nome_autor= models.CharField(max_length=50)
    assunto = models.CharField(max_length=200)
    editora = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    data= models.DateField()

    def __str__(self):
        return self.titulo

class Despesa(models.Model):
    data_criacao = models.CharField(max_length=50)
    tipo_despesa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    forma_pagamento = models.CharField(max_length=50)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def __str__(self):
        return self.descricao

class Compras(models.Model):
    nome = models.CharField(max_length =50)
    descricaoProduto = models.CharField(max_length=50)
    unidadeCompra = models.CharField(max_length =10)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMaximo = models.FloatField()

    def __str__(self):
        return self.nome

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartos = models.IntegerField()
    proprietario = models.CharField(max_length=10)
    valorCondominio = models.FloatField()


    def __str__(self):
        return self.proprietario

class Anuncio(models.Model):
    cliente = models.CharField(max_length=50)
    textoTitulo = models.CharField(max_length=10)
    preco = models.FloatField()
    textoAnuncio = models.CharField(max_length=50)
    nomeContato= models.CharField(max_length=50)
    telefone = models.CharField(max_length=13)
    secao = models.CharField(max_length=50)
    tipoAnucio = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente