from django.db import models
from . import Base, Jogo
from django.core.validators import MinValueValidator, MaxValueValidator


class Avaliacao(Base):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    nota_direcao_de_arte = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    nota_jogabilidade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    nota_entretenimento = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    nota_imersao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def media(self):
        return (
            self.nota_direcao_de_arte
            + self.nota_jogabilidade
            + self.nota_entretenimento
            + self.nota_imersao
        ) / 4
