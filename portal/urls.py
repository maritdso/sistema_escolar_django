from django.urls import path

from portal import views

# exemplo: path('index/', views.index)
urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro),  # ERRO 8 ENCONTRADO: a view 'cadastro' não existia no arquivo views.py, causando referência inválida na URL.
                                        # CORREÇÃO: a view foi criada em views.py ou a linha foi removida/corrigida para apontar para uma view existente.
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
