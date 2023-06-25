from django.contrib import admin
from django.urls import path
from core.views import allUsers,usuario, itens, allItens, login, usuarioCadastro, itemCadastro, usuarioEmail, findUserByFilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name='login'), 
    path('allUsers', allUsers, name='allUsers'), 
    path('userByEmail/<str:email>', usuarioEmail, name='userByEmail'),
    path('user', usuarioCadastro, name='usercadastro'),
    path('user/<str:id>', usuario, name='user'), # pega o usuario baseado no id(pelo url)
    path('allItens', allItens, name='allItens'), #serve pra pegar todos os items
    path('item/<str:id>', itens, name='itens'), #serve pra pegar os items especificos do usuario(pelo url)
    path('item', itemCadastro, name='itemcadastro'),
    path('userByFilter', findUserByFilter),
]
