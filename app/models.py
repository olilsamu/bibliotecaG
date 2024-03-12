from django.db import models

# Create your models here.
class Cidades(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cidades"


    def __str__(self):
        return self.nome

class Generos(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Generos"


    def __str__(self):
        return self.nome   

class Editoras(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Editoras"


    def __str__(self):
        return self.nome

class Autores(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Autores"


    def __str__(self):
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Livros"


    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Emprestimo"


    def __str__(self):
        return self.nome  


class Leitor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Leitor"


    def __str__(self):
        return self.nome             

