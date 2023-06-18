from django.contrib import admin
from django.urls import path
from core.views import allUsers,usuario, itens, allItens, login, usuarioCadastro, itemCadastro, usuarioEmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login), 
    path('allUsers', allUsers), 
    path('userByEmail/<str:email>', usuarioEmail),
    path('user', usuarioCadastro),
    path('user/<str:id>', usuario), # pega o usuario baseado no id(pelo url)
    path('allItens', allItens), #serve pra pegar todos os items
    path('item/<str:id>', itens), #serve pra pegar os items especificos do usuario(pelo url)
    path('item', itemCadastro),
]
