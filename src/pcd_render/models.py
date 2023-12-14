from django.db import models

# Create your models here.

class FormModel(models.Model):
    choices = [("F","Forte"), ("M","Moderada"), ("L","Leve"), ("N","Nenhuma")]
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    nausea = models.CharField(max_length=1, choices=choices, name="Nausea")
    stomach = models.CharField(max_length=1, choices=choices, name="Desconforto Estomacal")
    discomfort = models.CharField(max_length=1, choices=choices, name="Desconforto")
    describe = models.TextField(max_length=1000, blank=True, null=True, name="Descrição")

    def __str__(self):
        return self.name
