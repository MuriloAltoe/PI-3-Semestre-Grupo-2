from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Usuario, Barraca, Itens
import pymongo




def showUser(request, id):
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn["banco"]
    collection = db["barraca"]

    pipeline = [
    { "$match": { "id": id } },
    ]

    result = list(collection.aggregate(pipeline))
    result2 = dict(result[0])

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
        'itens_id'      : result2['itens_id']
    }
    print(dictRetorno)
    return JsonResponse(dictRetorno)

    
