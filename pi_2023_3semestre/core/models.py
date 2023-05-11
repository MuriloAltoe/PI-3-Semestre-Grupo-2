from django.db import models
from djongo import models as djongo_models

class Usuario(djongo_models.Model):
    # id_usuario = models.IntegerField(verbose_name='usuario_', unique=True)
    email = models.EmailField(verbose_name='email_', unique=True)

    class Meta:
        db_table = 'usuarios'


class Barraca(djongo_models.Model):
    id_usuario = models.IntegerField(verbose_name='usuario_', unique=True)
    id_itens = models.IntegerField(verbose_name='items_', unique=True)


    class Meta:
        db_table = 'barraca'


class Itens(djongo_models.Model):
    id_barraca = models.EmailField(verbose_name='email_', unique=True)

    class Meta:
        db_table = 'itens'
