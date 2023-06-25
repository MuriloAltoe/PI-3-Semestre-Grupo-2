from django.test import TestCase, Client
from django.urls import reverse
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['banco']

class ViewTests(TestCase):
    def setUp(self):
        
        # Criando Novo item
        self.last_id_barraca = "6496252b028fb895ec7a2d47"
        self.last_id_itens = "6496252b028fb895ec7a2d47"

        self.client = Client()
        self.login_url = reverse('login')
        self.all_users_url = reverse('allUsers')
        self.usercadastro_url = reverse('usercadastro')
        self.user_url = reverse('user', args=[str(self.last_id_barraca)])
        self.all_itens_url = reverse('allItens')
        self.itens_url  = reverse('itens', args=[str(self.last_id_itens)])
        self.itemcadastro_url = reverse('itemcadastro')

    def test_usuario_post(self):
        response = self.client.post(self.usercadastro_url, json.dumps({ "email": "test@example.com", "nome": "$nome", "tipo": "$tipo", "senha": "password", "entrega": "$entrega", "cep": "$cep", "rua": "$rua", "cidade": "$cidade", "complemento": "$complemento", "bairro": "$bairro", "numero": "$numero", "estado": "$estado", "telefone": "$telefone" }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_usuario_get(self):
        # Pega o último registro
        collection = db['barraca']
        self.last_id_barraca = collection.find_one(sort=[('_id', -1)])["_id"]
        self.user_url = reverse('user', args=[str(self.last_id_barraca)])

        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 200)

    def test_usuario_put(self):
        # Pega o último registro
        collection = db['barraca']
        self.last_id_barraca = collection.find_one(sort=[('_id', -1)])["_id"]
        self.user_url = reverse('user', args=[str(self.last_id_barraca)])

        # Exec a ação
        response = self.client.put(self.user_url, json.dumps({ "telefone": 4141515354346 }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_all_users_get(self):
        response = self.client.get(self.all_users_url)
        self.assertEqual(response.status_code, 200)
        user_data = json.loads(response.content)
        self.assertTrue(isinstance(user_data, list))
    
    def test_login(self):
        response = self.client.post(self.login_url, json.dumps({"email": "test@example.com", "senha": "password"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_itens_get(self):
        # Pega o último registro
        collection = db['itens']
        self.last_id_itens = collection.find_one(sort=[('_id', -1)])["_id"]
        self.itens_url = reverse('itens', args=[str(self.last_id_itens)])

        response = self.client.get(self.itens_url)
        self.assertEqual(response.status_code, 200)

    def test_itens_post(self):
        response = self.client.post(self.itemcadastro_url, json.dumps({'nome': 'Item 1', 'descricao': 'Descrição do Item 1'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_itens_put(self):
        # Pega o último registro
        collection = db['itens']
        self.last_id_itens = collection.find_one(sort=[('_id', -1)])["_id"]
        self.itens_url = reverse('itens', args=[str(self.last_id_itens)])

        response = self.client.put(self.itens_url, json.dumps({'nome': 'Descrição atualizada'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_all_itens_get(self):
        response = self.client.get(self.all_itens_url)
        self.assertEqual(response.status_code, 200)

    def test_itens_delete(self):
        # Pega o último registro
        collection = db['itens']
        self.last_id_itens = collection.find_one(sort=[('_id', -1)])["_id"]
        self.itens_url = reverse('itens', args=[str(self.last_id_itens)])

        response = self.client.delete(self.itens_url, json.dumps({ "id": str(self.last_id_itens) }), content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_usuario_delete(self):
        # Pega o último registro
        collection = db['barraca']
        self.last_id_barraca = collection.find_one(sort=[('_id', -1)])["_id"]
        self.user_url = reverse('user', args=[str(self.last_id_barraca)])

        response = self.client.delete(self.user_url, json.dumps({ "id": str(self.last_id_barraca) }), content_type='application/json')
        self.assertEqual(response.status_code, 204)