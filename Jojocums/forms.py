from django import forms
from .models import Jogo, Avaliacao


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = "__all__"


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = "__all__"
        widgets = {
            "nota_direcao_de_arte": forms.Select,
            "nota_jogabilidade": forms.Select,
            "nota_entretenimento": forms.Select,
            "nota_imersao": forms.Select,
        }
