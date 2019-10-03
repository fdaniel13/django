from django.contrib import admin
from .models import *

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nome_autor', 'assunto', 'editora', 'isbn', 'data')

admin.site.register(Biblioteca, BibliotecaAdmin)
# Register your models here.
class DespesaAdmin(admin.ModelAdmin):
    list_display=( 'data_criacao','tipo_despesa','descricao')

admin.site.register(Despesa, DespesaAdmin)

class ComprasAdmin(admin.ModelAdmin):
    list_display=( 'nome','descricaoProduto','unidadeCompra')

admin.site.register(Compras, ComprasAdmin)

class ApartamentoAdmin(admin.ModelAdmin):
    list_display=( 'numero','qtdQuartos','proprietario')

admin.site.register(Apartamento, ApartamentoAdmin)

class AnuncioAdmin(admin.ModelAdmin):
    list_display=( 'cliente','textoTitulo','preco')

admin.site.register(Anuncio, AnuncioAdmin)



class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula', 'data_nascimento')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('data_devolucao','data_retirada','aluno','devolvido')
    filter_horizontal = ['livros']

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)