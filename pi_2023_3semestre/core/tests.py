from django.test import TestCase, Client
from django.urls import reverse
import json

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user_url = reverse('usuario', args=['1'])  # tira o 1 e coloca o id do user
        self.all_users_url = reverse('allUsers')
        self.itens_url = reverse('itens', args=['1'])  # aqui também
        self.all_itens_url = reverse('allItens')

    def test_login(self):
        # criar user test banco

        #envia uma solictação post para o endpoint de login com as credenciais do user

        response = self.client.post(self.login_url, json.dumps({'email': 'test@example.com', 'senha': 'password'}), content_type='application/json')

        
        self.assertEqual(response.status_code, 200)
        self.assertIn('x-access-token', response.headers)
        token = response.headers['x-access-token']

        #

    def test_usuario_get(self):
        # fazer login com user 

        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, 200)
        user_data = json.loads(response.content)
        self.assertEqual(user_data['nome'], 'Murilo Leme')  # tira murilo e coloca o nome do usuario test
    def test_usuario_post(self):
        # fazer login com usuario autenticado
        

        # enviar uma solicitação POST para o endpoint de login com as credenciais do user
        response = self.client.post(self.user_url, json.dumps({'email': 'new@example.com', 'nome': 'Novo Usuário'}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Requisição POST processada com sucesso!'.encode('utf-8'))


    def test_usuario_put(self):


        # enviar uma solicitação PUT para o endpoint de login com as att do user
        response = self.client.put(self.user_url, json.dumps({'nome': 'Usuário Atualizado'}), content_type='application/json')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"message": ">:D"}')

    def test_usuario_delete(self):


        response = self.client.delete(self.user_url)

        self.assertEqual(response.status_code, 200)

    def test_all_users_get(self):

        response = self.client.get(self.all_users_url)

        self.assertEqual(response.status_code, 200)
        user_data = json.loads(response.content)
        self.assertTrue(isinstance(user_data, list))

    def test_itens_get(self):

        # enviar uma solicitação GET para o endpoint de login com o id do user
        response = self.client.get(self.itens_url)

        
        self.assertEqual(response.status_code, 200)
        item_data = json.loads(response.content)
        self.assertTrue(isinstance(item_data, list))

    def test_itens_post(self):


  
        response = self.client.post(self.itens_url, json.dumps({'nome': 'Item 1', 'descricao': 'Descrição do Item 1'}), content_type='application/json')

      
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Requisição POST processada com sucesso!'.encode('utf-8'))

    def test_itens_put(self):


        # Enviar um PUT para o endpoint de itens com os dados do item atualizados
        response = self.client.put(self.itens_url, json.dumps({'nome': 'Item Atualizado', 'descricao': 'Descrição atualizada'}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"message": ">:D"}')

    def test_itens_delete(self):
 

        # envia um  DELETE para o endpoint de itens
        response = self.client.delete(self.itens_url)

        self.assertEqual(response.status_code, 200)

    def test_all_itens_get(self):

        # enviar um  GET para o endpoint de allItens
        response = self.client.get(self.all_itens_url)


        self.assertEqual(response.status_code, 200)
        item_data = json.loads(response.content)
        self.assertTrue(isinstance(item_data, list))



