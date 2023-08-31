from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'Nome: {self.nome}' 
        
class todolist(models.Model):
    tarefa = models.CharField(max_length= 20)
    choice_status = [
        ('F', 'menina'),
        ('M', 'menino'),
    ]
    status = models.CharField(choices = choice_status,max_length=12)
    pessoa = models.ForeignKey(
        Pessoa,on_delete=models.CASCADE)