from django.db import models
from . import Base, Produtora, Distribuidora, Genero
from django.core.validators import MinValueValidator, MaxValueValidator


class Jogo(Base):
    titulo = models.CharField(max_length=150)
    produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    ano_lancamento = models.PositiveIntegerField()
