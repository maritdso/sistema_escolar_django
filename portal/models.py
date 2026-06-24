from django.db import models

# ERRO 1: A importação do timezone está faltando.
from django.utils import timezone

# Criar um modelo do Professor, com nome, email, telefone, registro, disciplina
class Professor(models.Model):
    # Atributos = características = variáveis
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)  # ERRO 1 aqui: timezone não foi importado
    telefone = models.CharField(max_length=15)
    registro = models.CharField(max_length=10)
    disciplina = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    # Métodos = ações = funções
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Criar um modelo do Aluno, com nome, email, telefone, matricula
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    matricula = models.CharField(max_length=10) # ERRO 7 ENCONTRADO: matrícula estava definida como IntegerField, o que não preserva zeros à esquerda (ex.: "0042" seria armazenado como 42).
                                                # CORREÇÃO: alterado para CharField(max_length=10) para preservar o formato completo da matrícula.
    criacao_data = models.DateTimeField(default=timezone.now)  # ERRO 1 ENCONTRADO: campo de data de criação não possuía valor padrão automático para registrar o momento da criação.
                                                               # CORREÇÃO: adicionado default=timezone.now para preencher automaticamente a data e hora de criação do registro.
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aula(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    horario = models.DateTimeField(default=timezone.now)  # ERRO 1 também aqui
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Aula {self.status} com sucesso.'
