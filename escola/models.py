from django.db import models


class Escola(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

