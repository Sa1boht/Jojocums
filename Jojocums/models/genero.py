from django.db import models
from . import Base


class Genero(Base):
    nome = models.CharField(max_length=50)
