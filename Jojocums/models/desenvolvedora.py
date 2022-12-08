import models
from . import Base


class Desenvolvedora(Base):
    nome = models.CharField(max_length=50)
