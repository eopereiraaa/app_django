from django.db import models


# Create your models here.
# ORM => Object Relationship Manager


# Ele automaticamente define o nome da tabela com o seguinte formato: <app>_<nome_da_classe_minúsculo>
# 1. Criar/modificar ou eliminar uma classe modelo
# 2. Criar a migração
# 3. Executar a migração
class Category(models.Model):
    # Definir uma tabela no banco de dados
    # É utilizada pelo sistema de migracoes para aplicar mudanças no banco de dados.
    # Criar registros em forma de instâncias da classe
    # A possibilidade de fazer CONSULTAS no banco de dados usando um MANAGER (.objects)

    category_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=200)
    nota = models.TextField()
    rating = models.PositiveIntegerField(null=True)
    last_update = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name


class Filme(models.Model):
    pass


""" 
CREATE TABLE category 
 category_id INT PRIMARY KEY
 name varchar(200)
"""
