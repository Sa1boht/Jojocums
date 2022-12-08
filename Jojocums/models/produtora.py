import models
from . import Base


class Produtora(Base):
    nome = models.CharField(max_length=50)
