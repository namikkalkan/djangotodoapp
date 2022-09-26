#tablolari claslar halinde olusturuyoruz ve sonra migrate ile tablomuz olusur
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length =50, verbose_name = 'baslik', null=True, blank=False)
    completed = models.BooleanField(verbose_name = 'Durum')
    def __str__(self):
        return self.title