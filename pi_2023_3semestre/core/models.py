from django.db import models
from djongo import models as djongo_models


class Itens(djongo_models.Model):
<<<<<<< HEAD
    nome = models.CharField(verbose_name="nome", max_length=100)
    preco = models.DecimalField(verbose_name="preco", max_digits=8, decimal_places=2)
    categoria = models.CharField(verbose_name="categoria", max_length=100)
    quantidade = models.IntegerField(verbose_name="quantidade")
=======
    id_barraca = models.CharField(verbose_name='email_', unique=True, max_length=30)

>>>>>>> branch-show(get)
    class Meta:
        db_table = 'itens'
        
        
class Usuario(djongo_models.Model):
    email = models.EmailField(verbose_name="email",unique=True)
    produtor = models.BooleanField(verbose_name="podutor", )
    senha = models.CharField(verbose_name="senha", max_length=100)
    telefone = models.CharField(verbose_name="telefone", max_length=100)
    entrega = models.BooleanField(verbose_name="entrega", default=False)
    #endereco
    rua = models.CharField(verbose_name="rua", max_length=100)
    cidade = models.CharField(verbose_name="cidade", max_length=100)
    cep = models.CharField(verbose_name="cep", max_length=100)
    estado = models.CharField(verbose_name="estado", max_length=100)
    complemento = models.CharField(verbose_name="complemento", max_length=100)
    bairro = models.CharField(verbose_name="bairro", max_length=100)
    numero = models.IntegerField(verbose_name="numero")
    
    class Meta:
        db_table = 'usuario'
