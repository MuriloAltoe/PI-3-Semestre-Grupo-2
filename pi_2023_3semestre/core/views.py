from django.shortcuts import render
import json
import jwt
import pymongo
from bson import ObjectId
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

localhost = "mongodb://localhost:27017/"


@csrf_exempt
def login(request):
    conn = conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'POST':
        collection = db["barraca"]
        data = json.loads(request.body)
        
        pipeline = [
            {"$match": {"email": data["email"], "senha": data["senha"]}},
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    "email": "$email",
                    "nome": "$nome",
                    "tipo": "$tipo",
                    "senha": "$senha",
                    "entrega": "$entrega",
                    "cep": "$cep",
                    "rua": "$rua",
                    "cidade": "$cidade",
                    "complemento": "$complemento",
                    "bairro": "$bairro",
                    "numero": "$numero",
                    "estado": "$estado",
                    "telefone": "$telefone"
                }
            }
        ]
        result = list(collection.aggregate(pipeline))

        if len(result) > 0:
            if (result[0]['senha'] == data['senha']):

                payload = {
                    'user': result[0],
                    'exp': datetime.utcnow() + timedelta(minutes=15)
                }
               
                secret_key = 'stardewgreen'
                token = jwt.encode(payload, secret_key, algorithm='HS256')
                response = HttpResponse()
                response["x-access-token"] = token
                response.content = json.dumps({'token': token})
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
        try:
            result = collection.insert_one(data)
            if result.inserted_id:
                objeto_id = str(result.inserted_id)
                response = HttpResponse(status=201)
                response['Location'] = f'/user/{objeto_id}'
                return response
            else:
                return HttpResponse("Falha no cadastro.", status=400)
        except Exception as e:
            return HttpResponse(f"Erro durante a inserção: {str(e)}", status=500)


@csrf_exempt
def usuario(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db["barraca"]
        objId = ObjectId(id)
        pipeline = [
            {"$match": {"_id": objId}},
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    "email": "$email",
                    "nome": "$nome",
                    "tipo": "$tipo",
                    "senha": "$senha",
                    "entrega": "$entrega",
                    "cep": "$cep",
                    "rua": "$rua",
                    "cidade": "$cidade",
                    "complemento": "$complemento",
                    "bairro": "$bairro",
                    "numero": "$numero",
                    "estado": "$estado",
                    "telefone": "$telefone"
                }
            }
        ]
        barraca = list(collection.aggregate(pipeline))
        if len(barraca) > 0:
            collection = db["itens"]
            pipeItens = [
                {"$match": {"id_barraca": barraca[0]["_id"]}},
                {"$sort": {"_id": -1}},
                {
                    "$project": {
                        "_id": {"$toString": "$_id"},
                        "nome": "$nome",
                        "preco": "$preco",
                        "medida": "$medida",
                        "categoria": "$categoria",
                        "quantidade": "$quantidade",
                        "id_barraca": "$id_barraca"
                    }
                }
            ]
            itens = list(collection.aggregate(pipeItens))
            itens2 = []
            for item in itens:
                itens2.append(item)

            barraca[0]["itens"] = itens2
            retorno = json.dumps(barraca[0])
            return HttpResponse(retorno, content_type='application/json')
        else:
            return HttpResponseNotFound("usuario não encontrado")

    elif request.method == 'PUT':
        collection = db["barraca"]
        data = json.loads(request.body)
        dictRetorno = {}
        if 'email' in data:
            dictRetorno['email'] = data['email']
        if 'rua' in data:
            dictRetorno['nome'] = data['nome']
        if 'tipo' in data:
            dictRetorno['tipo'] = data['tipo']
        if 'senha' in data:
            dictRetorno['senha'] = data['senha']
        if 'entrega' in data:
            dictRetorno['entrega'] = data['entrega']
        if 'cep' in data:
            dictRetorno['cep'] = data['cep']
        if 'rua' in data:
            dictRetorno['rua'] = data['rua']
        if 'cidade' in data:
            dictRetorno['cidade'] = data['cidade']
        if 'complemento' in data:
            dictRetorno['complemento'] = data['complemento']
        if 'bairro' in data:
            dictRetorno['bairro'] = data['bairro']
        if 'numero' in data:
            dictRetorno['numero'] = data['numero']
        if 'estado' in data:
            dictRetorno['estado'] = data['estado']
        if 'telefone' in data:
            dictRetorno['telefone'] = data['telefone']

        result = collection.update_one(
            {'_id': ObjectId(id)}, {'$set': dictRetorno})

        if result.modified_count > 0:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        collection = db["barraca"]
        data = json.loads(request.body)

        result = collection.delete_one({"_id": ObjectId(id)})

        if result.deleted_count > 0:
            return HttpResponse(status=204)
        else:
            return HttpResponseNotFound("usuario não encontrado")


@csrf_exempt
def itemCadastro(request):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'POST':
        collection = db["itens"]
        data = json.loads(request.body)
        try:
            result = collection.insert_one(data)
            if result.inserted_id:
                objeto_id = str(result.inserted_id)
                response = HttpResponse(status=201)
                response['Location'] = f'/item/{objeto_id}'
                return response
            else:
                return HttpResponse("Falha no cadastro.", status=400)
        except Exception as e:
            return HttpResponse(f"Erro durante a inserção: {str(e)}", status=500)


@csrf_exempt
def itens(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]
        objId = ObjectId(id)

        pipeline = [
            {'$match': {"_id": objId}},
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    "nome": "$nome",
                    "preco": "$preco",
                    "medida": "$medida",
                    "categoria": "$categoria",
                    "quantidade": "$quantidade",
                    "id_barraca": "$id_barraca"
                }
            }
        ]

        item = list(collection.aggregate(pipeline))
        if len(item) > 0:
            return HttpResponse(json.dumps(item[0]), content_type='application/json')
        else:
            return HttpResponseNotFound("item não encontrado")

    elif request.method == 'DELETE':
        collection = db["itens"]
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return HttpResponse(status=204)
        else:
            return HttpResponseNotFound("item não encontrado")

    elif request.method == 'PUT':
        collection = db["itens"]
        data = json.loads(request.body)
        update_data = {}
        if 'nome' in data:
            update_data['nome'] = data['nome']
        if 'preco' in data:
            update_data['preco'] = data['preco']
        if 'medida' in data:
            update_data['medida'] = data['medida']
        if 'categoria' in data:
            update_data['categoria'] = data['categoria']
        if 'quantidade' in data:
            update_data['quantidade'] = data['quantidade']

        result = collection.update_one(
            {'_id': ObjectId(id)}, {'$set': update_data})
        if result.modified_count > 0:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404, content='Nenhum documento atualizado.')


@csrf_exempt
def allUsers(request):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db['barraca']
        pipeline = [{
            '$project': {
                '_id': {'$toString': '$_id'},
                "email": "$email",
                "nome": "$nome",
                "tipo": "$tipo",
                "senha": "$senha",
                "entrega": "$entrega",
                "cep": "$cep",
                "rua": "$rua",
                "cidade": "$cidade",
                "complemento": "$complemento",
                "bairro": "$bairro",
                "numero": "$numero",
                "estado": "$estado",
                "telefone": "$telefone"
            }
        }]
        barraca = list(collection.aggregate(pipeline))

        barraca2 = []
        for i in barraca:
            collection = db["itens"]
            pipeItens = [
                {"$match": {"id_barraca": i["_id"]}},
                {"$sort": {"_id": -1}},
                {"$limit": 3},
                {
                    "$project": {
                        "_id": {"$toString": "$_id"},
                        "nome": "$nome",
                        "preco": "$preco",
                        "medida": "$medida",
                        "categoria": "$categoria",
                        "quantidade": "$quantidade",
                        "id_barraca": "$id_barraca"
                    }
                }
            ]
            itens = list(collection.aggregate(pipeItens))
            itens2 = []
            for item in itens:
                itens2.append(item)

            i["itens"] = itens2
            barraca2.append(i)

        retorno = json.dumps(barraca2)

        return HttpResponse(retorno, content_type='application/json')


@csrf_exempt
def allItens(request):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db["itens"]
        pipeline = [
            {"$sort": {"_id": -1}},
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    "nome": "$nome",
                    "preco": "$preco",
                    "medida": "$medida",
                    "categoria": "$categoria",
                    "quantidade": "$quantidade",
                    "id_barraca": "$id_barraca"
                }
            }
        ]

        itens = list(collection.aggregate(pipeline))
        itens2 = []

        for i in itens:
            itens2.append(i)

        retorno = json.dumps(itens2)

        return HttpResponse(retorno, content_type='application/json')

    else:
        return HttpResponse("Método não permitido. Use GET para enviar dados.")


@csrf_exempt
def usuarioEmail(request, email):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db["barraca"]
        pipeline = [
            {"$match": {"email": email}},
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    "email": "$email",
                    "nome": "$nome",
                    "tipo": "$tipo",
                    "senha": "$senha",
                    "entrega": "$entrega",
                    "cep": "$cep",
                    "rua": "$rua",
                    "cidade": "$cidade",
                    "complemento": "$complemento",
                    "bairro": "$bairro",
                    "numero": "$numero",
                    "estado": "$estado",
                    "telefone": "$telefone"
                }
            }
        ]
        barraca = list(collection.aggregate(pipeline))
        if len(barraca) > 0:
            collection = db["itens"]
            pipeItens = [
                {"$match": {"id_barraca": barraca[0]["_id"]}},
                {"$sort": {"_id": -1}},
                {
                    "$project": {
                        "_id": {"$toString": "$_id"},
                        "nome": "$nome",
                        "preco": "$preco",
                        "medida": "$medida",
                        "categoria": "$categoria",
                        "quantidade": "$quantidade",
                        "id_barraca": "$id_barraca"
                    }
                }
            ]
            itens = list(collection.aggregate(pipeItens))
            itens2 = []
            for item in itens:
                itens2.append(item)

            barraca[0]["itens"] = itens2
            retorno = json.dumps(barraca[0])
            return HttpResponse(retorno, content_type='application/json')
        else:
            return HttpResponseNotFound("usuario não encontrado")
