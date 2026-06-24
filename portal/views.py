from django.shortcuts import render

# GET, POST, PUT, DELETE
# REQUEST <-> RESPONSE
# RENDER -> RENDERIZAR

# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request):  # É a request feita pelo usuário

    # ERRO 2 ENCONTRADO: caminho do template informado com "/" no início, o Django procura templates de forma relativa à pasta templates.
    # CORREÇÃO: alterado de '/portal/index.html' para 'portal/index.html'.
    
    # ERRO 2 ENCONTRADO: terceiro parâmetro do render() estava recebendo '/portal/cadastro.html', mas esse parâmetro é destinado ao contexto (dict), não a outro template.
    # CORREÇÃO: removido '/portal/cadastro.html'. Cada template deve possuir sua própria view.
    return render(
        request,
        'portal/index.html'
    )


# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA DE CADASTRO
def cadastro(request):  # É a request feita pelo usuário

    # ERRO 8 ENCONTRADO: não existia uma view específica para renderizar o template de cadastro.
    # CORREÇÃO: criada a função cadastro() para renderizar 'portal/cadastro.html'.
    return render(
        request,
        'portal/cadastro.html'
    )