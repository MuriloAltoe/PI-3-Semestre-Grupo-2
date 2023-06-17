from django.contrib import admin
from django.urls import path
from core.views import allUsers,usuario, itens, allItens, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login), 
    path('allUsers', allUsers), 
    path('user/<str:id>', usuario), # pega o usuario baseado no id(pelo url)
    path('allItens/', allItens), #serve pra pegar todos os items
    path('itens/<str:id>', itens), #serve pra pegar os items especificos do usuario(pelo url)
]
