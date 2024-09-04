from django.shortcuts import render, HttpResponse

def paginaInicial(request):
    return render(request,'estoque/inicial.html') 

def paginaCadastro(request):
    return render(request, 'estoque/cadastro.html')

def paginaEstoque(request):
    return render(request,'estoque/estoque.html')

def paginaCaixa(request):
    return render(request,'estoque/caixa.html')

def paginaRelatorio(request):
    return render(request,'estoque/relatorio.html')
