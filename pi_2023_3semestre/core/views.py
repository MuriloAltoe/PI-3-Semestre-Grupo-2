from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
# from .models import Usuario, Barraca, Itens
from django.views.decorators.csrf import csrf_exempt

import pymongo

# def showUser(request, id):
#     conn = pymongo.MongoClient("mongodb://localhost:27017/")
#     db = conn["banco"]
#     collection = db["barraca"]
#     usuario = list(collection.aggregate([{ "$match": { "id": id } }])) 
#     # print(usuario)
#     result2 = dict(usuario[0])

#     collection = db["itens"]
#     itens = list(collection.aggregate([{ "$match": { "id_items": id } }])) 
#     itens2 = []
#     for i in itens:
#         itens2.append(i)
#         # print(i)
    

#     dictRetorno = {   
#         "id"            : result2["id"],
#         "email"         : result2["email"],
#         'produtor'      : result2['produtor'],
#         'senha'         : result2['senha'],
#         'entrega'       : result2['entrega'],

#         "cep"           : result2["cep"],
#         "rua"           : result2["rua"],
#         'cidade'        : result2['cidade'],
#         'complemento'   : result2['complemento'],
#         'bairro'        : result2['bairro'],
#         'numeros'       : result2['numeros'],
#         'itens_id'      : str(itens2)
#     }
#     return JsonResponse(dictRetorno)


@csrf_exempt
def usuario(request, id):

    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn["banco"]
    
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)
        
        # Fazer algo com os dados recebidos
        # ...

        return HttpResponse("Requisição POST processada com sucesso!")
    
    elif request.method == 'GET':

        collection = db["barraca"]
        usuario = list(collection.aggregate([{ "$match": { "id": id } }])) 
        result2 = dict(usuario[0])

        collection = db["itens"]
        itens = list(collection.aggregate([{ "$match": { "id_items": id } }])) 
        itens2 = []
        for i in itens:
            itens2.append(i)       

        dictRetorno = {   
            "id"            : result2["id"],
            "email"         : result2["email"],
            'produtor'      : result2['produtor'],
            'senha'         : result2['senha'],
            'entrega'       : result2['entrega'],

            "cep"           : result2["cep"],
            "rua"           : result2["rua"],
            'cidade'        : result2['cidade'],
            'complemento'   : result2['complemento'],
            'bairro'        : result2['bairro'],
            'numeros'       : result2['numeros'],
            'itens_id'      : str(itens2)
        }
        return JsonResponse(dictRetorno)
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")
    
@csrf_exempt
def allItens(request):
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]

        itens = list(collection.aggregate([])) 

        itens2 = []
        for i in itens:
            itens2.append(i)

        print(itens2)

        return HttpResponse(itens2)

    elif request.method == 'POST':
        pass

    elif request.method == 'DELETE':
        pass

    elif request.method == 'PUT':
        pass
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")

@csrf_exempt
def itens(request, id):
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]

        itens = list(collection.aggregate([{ "$match": { "id_items": id } }])) 

        itens2 = []
        for i in itens:
            itens2.append(i)

        return HttpResponse(itens2)

    elif request.method == 'POST':

        data = json.loads(request.body)

        print(data)
        
        # Fazer algo com os dados recebidos
        # ...

        return HttpResponse(data)

        pass

    elif request.method == 'DELETE':
        pass

    elif request.method == 'PUT':
        pass
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")
