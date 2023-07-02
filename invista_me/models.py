from django.db import models
from datetime import datetime
'''
- Investimento
- Valor
- Pago
- Data
'''
# Create your models here.


class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)  # Default False significa que ainda não foi pago.
    data = models.DateField(default=datetime.now)
