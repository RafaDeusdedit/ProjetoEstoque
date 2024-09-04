from django.contrib import admin
from django.urls import path
from estoqueApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paginaInicial, name='paginaInicial'),
    path('cadastro/', views.paginaCadastro, name='paginaCadastro'),
    path('caixa/', views.paginaCaixa, name='paginaCaixa'),
    path('estoque/', views.paginaEstoque, name='paginaEstoque'),
    path('relatorio/', views.paginaRelatorio, name='paginaRelatorio'),
    
]
