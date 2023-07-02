from django.forms import ModelForm
from .models import Investimento


# Criando model form
class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'  # Para que todos os campos sejam exibidos.
        # Isso é tudo que precisa fazer para criar um formulário usando DJANGO.
