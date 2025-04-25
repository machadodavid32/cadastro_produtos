from django.shortcuts import render, redirect
from .forms import ProdutoForm
from django.contrib import messages

def pagina_inicial(request):
    return render(request, 'produtos/index.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('pagina_inicial')  # Ajustei para redirecionar corretamente
    else:
        form = ProdutoForm()
    
    # Este é o único return correto para esta função
    return render(request, 'produtos/cadastrar.html', {'form': form})

       