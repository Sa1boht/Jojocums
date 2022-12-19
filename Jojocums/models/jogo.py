from django.db import models
from . import Base, Produtora, Distribuidora, Genero
from django.core.validators import MinValueValidator, MaxValueValidator


class Jogo(Base):
    titulo = models.CharField(max_length=150)
    produtora = models.CharField(max_length=150)
    distribuidora = models.CharField(max_length=150)
    genero = models.CharField(max_length=30)
    ano_lancamento = models.PositiveIntegerField()
