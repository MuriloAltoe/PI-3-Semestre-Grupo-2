from django.shortcuts import render
import json
import jwt
import pymongo
from bson import ObjectId
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


localhost="mongodb://localhost:27017/"

@csrf_exempt
def login(request):
    conn = conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'POST':
        collection = db["barraca"]
        data = json.loads(request.body)
        
        result = list(collection.find({
            "email" : data["email"],
            "senha" : data["senha"],
        }))

        if len(result) > 0:

            payload = {
                'user_id': str(list(result)[0]['_id']),
                'user_id':'',
                'exp': datetime.utcnow() + timedelta(minutes=15)
            }
            # Gera o tolken
            secret_key = 'stardewgreen' # Senha
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            response = HttpResponse()
            response["x-access-token"] = token
            return response
        else:
            return JsonResponse({'message': '>:c'})

@csrf_exempt
def usuario(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db["barraca"]
        objId = ObjectId(id)
        usuario = list(collection.aggregate([{ "$match": { "_id": objId } }]))

        result2 = dict(usuario[0])

        collection = db["itens"]
        itens = list(collection.aggregate([{ "$match": { "id_items": objId } }])) 
        itens2 = []
        for i in itens:
            itens2.append(i)       

        dictRetorno = {   
            "_id"         :str(result2["_id"]),                
            "email"       :result2["email"],      
            "nome"        :result2["nome"],
            "tipo"        :result2["tipo"],
            "senha"       :result2["senha"],
            "entrega"     :result2["entrega"],
            "cep"         :result2["cep"],
            "rua"         :result2["rua"],
            "cidade"      :result2["cidade"],
            "complemento" :result2["complemento"],
            "bairro"      :result2["bairro"],
            "numeros"     :result2["numeros"],
            "estado"      :result2["estado"],
            "telefone"    :result2["telefone"],
            "id_usuario"  :result2["id_usuario"],
        }
        return JsonResponse(dictRetorno)
         
    elif request.method == 'POST':
        collection = db["barraca"]
        data = json.loads(request.body)
        
        dictRetorno = {   
            "email"       :data["email"],      
            "nome"        :data["nome"],
            "tipo"        :data["tipo"],
            "senha"       :data["senha"],
            "entrega"     :data["entrega"],
            "cep"         :data["cep"],
            "rua"         :data["rua"],
            "cidade"      :data["cidade"],
            "complemento" :data["complemento"],
            "bairro"      :data["bairro"],
            "numeros"     :data["numeros"],
            "estado"      :data["estado"],
            "telefone"    :data["telefone"],     
        }

        collection.insert_one(dictRetorno)

        return HttpResponse("Requisição POST processada com sucesso!")
    
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
        if 'numeros' in data:
            dictRetorno['numeros'] = data['numeros']
        if 'estado' in data:
            dictRetorno['estado'] = data['estado']
        if 'telefone' in data:
            dictRetorno['telefone'] = data['telefone']

        result = collection.update_one({'_id': id}, {'$set': dictRetorno})
        
        if result.modified_count > 0:
            return JsonResponse({'message': '>:D'})
        else:
            return JsonResponse({'message': '>:c'})

    elif request.method == 'DELETE':
        collection = db["barraca"]
        data = json.loads(request.body)
        collection.delete_one({"_id":ObjectId(data['id'])})
        return HttpResponse()

    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")

@csrf_exempt
def itens(request, id):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':

        collection = db["itens"]
        objId = ObjectId(id)

        pipeline = [
            { '$match': { "_id" : objId } },
            { '$project': {
                    '_id': {'$toString': '$_id'},  # Converter ObjectId para string
                    # "id_item": "$id_item",
                    "nome": "$nome",
                    "preco": "$preco",
                    "medida": "$medida",
                    "categoria": "$categoria",
                    "quantidade": "$quantidade",
                    # "id_usuario": "$id_usuario"
                }
            }
        ]

        itens = list(collection.aggregate( pipeline ))

        itens2 = []
        for i in itens:
            itens2.append(i)

        return HttpResponse(json.dumps(itens2), content_type='application/json')

    elif request.method == 'POST':
        collection = db["itens"]
        data = json.loads(request.body)

        dictRetorno = {
            "nome": data['nome'],
            "preco": data['preco'],
            "medida": data['medida'],
            "categoria": data['categoria'],
            "quantidade": data['quantidade'],
            "id_usuario": ObjectId(data['id_usuario'])
        }

        collection.insert_one(dictRetorno)
        # return JsonResponse(data)
        return HttpResponse()

    elif request.method == 'DELETE':
        collection = db["itens"]
        data = json.loads(request.body)
        collection.delete_one({"_id":ObjectId(data['id'])})
        return HttpResponse()

    elif request.method == 'PUT':
        collection = db["itens"]
        data = json.loads(request.body)
        objId = ObjectId(data['id'])

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

        result = collection.update_one({'_id': objId}, {'$set': update_data})
        if result.modified_count > 0:
            return JsonResponse({'message': '>:D'})
        else:
            return JsonResponse({'message': '>:c'})
         
    else:
        return HttpResponse("Método não permitido. Use POST para enviar dados.")


@csrf_exempt
def allUsers(request):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db['barraca']
        pipeline=[{
            '$project': {
                '_id': {'$toString': '$_id'}, 
                "email":"$email",          
                "nome":"$nome",         
                "tipo":"$tipo",       
                "senha":"$senha",   
                "entrega":"$entrega",   
                "cep":"$cep", 
                "rua":"$rua",
                "cidade":"$cidade",
                "complemento" :"$complemento",
                "bairro":"$bairro",   
                "numeros":"$numeros", 
                "estado":"$estado",
                "telefone":"$telefone",
                "id_usuario":"$id_usuario",
            }
        }]
        barraca = list(collection.aggregate(pipeline))
        
        barraca2 = []
        for i in barraca:
            barraca2.append(i)

        retorno = json.dumps(barraca2)

        return HttpResponse(retorno, content_type='application/json')

@csrf_exempt
def allItens(request):
    conn = pymongo.MongoClient(localhost)
    db = conn["banco"]

    if request.method == 'GET':
        collection = db["itens"]
        pipeline = [{
            '$project': {
                '_id': {'$toString': '$_id'},  # Converter ObjectId para string
                # "id_item": "$id_item",
                "nome": "$nome",
                "preco": "$preco",
                "medida": "$medida",
                "categoria": "$categoria",
                "quantidade": "$quantidade",
                # "id_usuario": "$id_usuario"
            }
        }]

        itens = list(collection.aggregate(pipeline)) 

        itens2 = []

        for i in itens:
            itens2.append(i)

        retorno = json.dumps(itens2)


        return HttpResponse(retorno, content_type='application/json')

    else:
        return HttpResponse("Método não permitido. Use GET para enviar dados.")
