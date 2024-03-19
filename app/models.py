from django.db import models

# Create your models here.
class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=500)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    datapublicacao = models.DateField()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    dataemprestimo = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    datadevolucao = models.DateField()
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
