from django.shortcuts import render
from django.http import JsonResponse
from .models import MyModel



def mymodel_list(request):
    mymodels = MyModel.objects.filter()
    data = {'results': list(mymodels.values())}
    return JsonResponse(data)
