from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ERRO 4 ENCONTRADO: foi utilizado texto ("preciso mostrar a página cadastro.html") no lugar de uma view válida.
    # CORREÇÃO: substituído por views.cadastro para renderizar a página cadastro.html.
    path('cadastro/', views.cadastro, name='cadastro'),
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
