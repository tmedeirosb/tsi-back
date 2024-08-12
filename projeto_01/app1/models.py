from django.db import models

# Create your models here.
class Agenda(models.Model):
    nome = models.CharField(
        max_length=100, 
        null=False,
        blank=False
    )
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome
