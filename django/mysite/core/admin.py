from django.contrib import admin
from .models import Biblioteca
from .models import Despesa
from .models import Compras
from  .models import Anuncio
from  .models import Apartamento

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