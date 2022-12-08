from django.db import models
from . import Base

class Distribuidora(Base):
    nome = models.CharField(max_length=50)