from django.db import models

class Itens(djongo_models.Model):
    nome = models.CharField(verbose_name="nome", max_length=100)
    preco = models.DecimalField(verbose_name="preco", max_digits=8, decimal_places=2)
    categoria = models.CharField(verbose_name="categoria", max_length=100)
    quantidade = models.IntegerField(verbose_name="quantidade")
    id_item = models.IntegerField(verbose_name="id_item")
    id_usuario = models.CharField(verbose_name='id_usuario', unique=True, max_length=30)
    class Meta:
        db_table = 'itens'
        
        
class Usuario(djongo_models.Model):
    email = models.CharField(verbose_name="email", max_length=100)
    nome = models.CharField(verbose_name="nome", max_length=100)
    tipo = models.CharField(verbose_name="tipo", max_length=100)
    senha = models.IntegerField(verbose_name="senha")
    telefone = models.CharField(verbose_name="telefone", max_length=100)
    entrega = models.BooleanField(verbose_name="entrega", default=False)
    #endereco
    rua = models.CharField(verbose_name="rua", max_length=100)
    cidade = models.CharField(verbose_name="cidade", max_length=100)
    cep = models.CharField(verbose_name="cep", max_length=100)
    estado = models.CharField(verbose_name="estado", max_length=100)
    complemento = models.CharField(verbose_name="complemento", max_length=100)
    bairro = models.CharField(verbose_name="bairro", max_length=100)
    numero = models.CharField(verbose_name="numero", max_length=100)
    
    class Meta:
        db_table = 'barraca'
