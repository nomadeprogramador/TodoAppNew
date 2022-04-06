from django.db import models

# Create your models here.
class Tarefa(models.Model):
    conteudo = models.TextField()
    completado = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.conteudo}'