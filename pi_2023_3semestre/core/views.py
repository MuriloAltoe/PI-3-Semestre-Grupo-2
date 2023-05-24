from django.shortcuts import render
import json
import jwt
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
# from .models import Usuario, Barraca, Itens
from django.views.decorators.csrf import csrf_exempt

import pymongo
from pymongo import InsertOne

localhost="mongodb://localhost:27017/"

@csrf_exempt
def login(request):

    if request.method == 'POST':
        conn = conn = pymongo.MongoClient(localhost)
        db = conn["banco"]
        collection = db["barraca"]
        data = json.loads(request.body)

        result = collection.find({
            "email" : data["email"],
            "senha" : data["senha"],
        })
        # find = list(result)

        # print(dict(find[0]))

        if result.count() > 0:
            payload = {
                'user_id': result[0]['id'],
                'exp': datetime.utcnow() + timedelta(minutes=15)
            }
            # Gera o tolken
            secret_key = 'stardewgreen'
            token = jwt.encode(payload, secret_key, algorithm='HS256')

            response = HttpResponse(token)

            response["x-access-token"] = token

            return response
        else:
            return HttpResponse("usuario não encontrado")

        return JsonResponse(dict(find[0]))


@csrf_exempt
def usuario(request, id):

    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]
    
    if request.method == 'POST':
        collection = db["barraca"]
        data = json.loads(request.body)

        # print(data["usuario"])
        
        dictRetorno = {   
            "id"            : data["id"],
            "email"         : data["email"],
            'produtor'      : data['produtor'],
            'senha'         : data['senha'],
            'entrega'       : data['entrega'],

            "cep"           : data["cep"],
            "rua"           : data["rua"],
            'cidade'        : data['cidade'],
            'complemento'   : data['complemento'],
            'bairro'        : data['bairro'],
            'numeros'       : data['numeros'],
            'itens_id'      : str(itens2)
        }

        collection.InsertOne(dictRetorno)

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
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]

        itens = list(collection.aggregate([])) 

        itens2 = []
        for i in itens:
            itens2.append(i)

        print(itens2)

        return HttpResponse(itens2)

    # elif request.method == 'POST':
    #     pass

    # elif request.method == 'DELETE':
    #     pass

    # elif request.method == 'PUT':
    #     pass
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")

@csrf_exempt
def itens(request, id):
    conn = pymongo.MongoClient(localhost)
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

        return JsonResponse(data)

        pass

    elif request.method == 'DELETE':
        pass

    elif request.method == 'PUT':
        pass
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")
