"""pi_2023_3semestre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from core.views import usuario, itens, allItens, login, usuarioCadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login), 
    path('allUsuarios', usuario), 
    path('usuario/<str:id>', usuario), # pega o usuario baseado no id(pelo url)
    path('usuario', usuarioCadastro), # pega o usuario baseado no id(pelo url)
=======
from core.views import usuario, allUsers, login, itens, allItens

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('showUser/<str:id>', showUser)
    path('login/', login), 
    path('allUsers/', allUsers), 
    path('user/<str:id>', usuario), # pega o usuario baseado no id(pelo url)
>>>>>>> 62c5d51 (all-working)
    path('allItens/', allItens), #serve pra pegar todos os items
    path('itens/<str:id>', itens), #serve pra pegar os items especificos do usuario(pelo url)
]
