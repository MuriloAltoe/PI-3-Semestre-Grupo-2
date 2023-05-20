from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import MyModel
from .models import Usuario, Barraca, Itens
import pymongo




def showUser(request, id):
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn["banco"]
    collection = db["usuarios"]

    pipeline = [
    { "$match": { "ObjectId": id } },
    ]

    result = list(collection.aggregate(pipeline))
    result2 = dict(result[0])
    dictRetorno = {
        "pk": result2["primary_key"],
        "email": result2["email"],
    }
    print(result2)
    return JsonResponse(dictRetorno)

    
