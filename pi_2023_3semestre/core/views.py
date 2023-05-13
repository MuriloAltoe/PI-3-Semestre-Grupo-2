from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MyModel
from .models import Usuario, Barraca, Itens



def mymodel_list(request):
    mymodels = MyModel.objects.filter()
    data = {'results': list(mymodels.values())}
    return JsonResponse(data)

#CRUD

# Delete do Usuário
def deleteUser(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return HttpResponse('Usuário deletado com sucesso!!')

# Delete da Barraca
def deleteBarraca(request, id):
    barraca = Barraca.objects.get(id=id)
    barraca.delete()
    return HttpResponse('Barraca deletado com sucesso!!')

# Delete dos Itens
def deleteItens(request, id):
    itens = Itens.objects.get(id=id)
    itens.delete()
    return HttpResponse('Item deletado com sucesso!!')


# Update do Usuário
def updateUser(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST['email']
        
        usuario.email = email
        usuario.save()
        return HttpResponse('Usuário atualizado com sucesso!!')
    else:
        return render(request, 'update.html', {'usuario': usuario})
    

    
