from bson import ObjectId
from django.shortcuts import render
import json
import jwt
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

# from .models import Usuario, Barraca, Itens
from django.views.decorators.csrf import csrf_exempt

import pymongo
from pymongo import InsertOne

localhost = "mongodb://localhost:27017/"


@csrf_exempt
def login(request):

    if request.method == 'POST':
        conn = conn = pymongo.MongoClient(localhost)
        db = conn["banco"]
        collection = db["barraca"]
        data = json.loads(request.body)

        result = collection.find({"email": data["email"]})

        if result.count() > 0:
            print(result[0])
            if (result[0]['senha'] == data['senha']):

                payload = {
                    'id':  str(result[0]['_id']),
                    'exp': datetime.utcnow() + timedelta(minutes=15)
                }

                print(payload)
                # Gera o tolken
                secret_key = 'stardewgreen'
                token = jwt.encode(payload, secret_key, algorithm='HS256')

                response = HttpResponse(token)

                response["x-access-token"] = token

                return response
            else:
                response = HttpResponse("Acesso não autorizado.")
                response.status_code = 401
                return response
        else:
            return HttpResponseNotFound("usuario não encontrado")


@csrf_exempt
def usuarioCadastro(request):

    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'POST':
        collection = db["barraca"]
        data = json.loads(request.body)

        dictRetorno = {
            "email": data["email"],
            'nome': data["nome"],
            'tipo': data['tipo'],
            'senha': data['senha'],
            'entrega': data['entrega'],
            "cep": data["cep"],
            "rua": data["rua"],
            'cidade': data['cidade'],
            'complemento': data['complemento'],
            'bairro': data['bairro'],
            'numeros': data['numeros'],
            'estado': data['estado'],
            'telefone': data['telefone']
        }
        
        try:
            result = collection.insert_one(data)

            if result.inserted_id:
                return HttpResponse("Cadastro realizada com sucesso!")
            else:
                return HttpResponse("Falha no cadastro.")
        except Exception as e:
            return HttpResponse(f"Erro durante a inserção: {str(e)}")
           


@csrf_exempt
def usuario(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["barraca"]
        usuario = list(collection.aggregate([{"$match": {"_id":  ObjectId(id)}}]))
        result2 = dict(usuario[0])
        print(usuario)
        collection = db["itens"]
        itens = list(collection.aggregate([{"$match": {"id_usuario": id}}]))
        itens2 = []
        for i in itens:
            itens2.append(i)

        dictRetorno = {
            "id": str(result2['_id']),
            "email": result2["email"],
            'tipo': result2['tipo'],
            'senha': result2['senha'],
            'entrega': result2['entrega'],
            'estado': result2['estado'],
            "cep": result2["cep"],
            "rua": result2["rua"],
            'cidade': result2['cidade'],
            'complemento': result2['complemento'],
            'bairro': result2['bairro'],
            'numeros': result2['numeros'],
            'telefone': result2['telefone'],
            'itens': str(itens2)
        }
        return JsonResponse(dictRetorno)
    
@csrf_exempt
def usuarioExclusao(request, id):
    conn = pymongo.MongoClient("localhost")
    db = conn["banco"]

    if request.method == 'DELETE':
        try:
            collection_itens = db["itens"]
            collection_barraca = db["barraca"]

            # Excluir os itens relacionados ao usuário
            result_itens = collection_itens.delete_many({"id_usuario": id})
            # Excluir o usuário
            result_barraca = collection_barraca.delete_one({"_id": ObjectId(id)})

            if result_barraca.deleted_count == 1:
                return HttpResponse("Exclusão realizada com sucesso!")
            else:
                return HttpResponse("Falha na exclusão: usuário não encontrado.")
        except Exception as e:
            return HttpResponse(f"Erro durante a exclusão: {str(e)}")


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

@csrf_exempt
def itens(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]

        itens = list(collection.aggregate([{"$match": {"id_items": id}}]))

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
        try:
            collection = db["itens"]
            result = collection.delete_many({"id_items": id})

            if result.deleted_count > 0:
                return HttpResponse("Exclusão dos itens realizada com sucesso!")
            else:
                return HttpResponse("Falha na exclusão: nenhum item encontrado.")
        except Exception as e:
            return HttpResponse(f"Erro durante a exclusão: {str(e)}")

    elif request.method == 'PUT':
        pass

    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")
