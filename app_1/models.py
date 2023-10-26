from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField("Município", max_length=50)
    sigla = models.CharField("Sigla", max_length=2)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField("Curso", max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=50)
    endereco = models.TextField("Endereço")
    email = models.EmailField("Email")
    data_nascimento = models.DateField("Data de Aniversário")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
