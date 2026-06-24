# Sistema Django — Correção de Erros

Este documento descreve os erros encontrados no projeto Django, explicando como estavam, qual foi a correção e o impacto de cada problema no funcionamento do sistema.

---

## Erro 01 — Import ausente (timezone)

**Como estava:**
criacao_data = models.DateTimeField(default=timezone.now)

**Problema:**
O módulo timezone não foi importado.

**Correção:**
from django.utils import timezone

**Impacto:**
O sistema gerava NameError e impedia a criação de registros com data automática.

---

## Erro 02 — Tipo de campo incorreto (matrícula)

**Como estava:**
matricula = models.IntegerField()

**Problema:**
Matrículas podem ter zeros à esquerda.

**Correção:**
matricula = models.CharField(max_length=10)

**Impacto:**
Perda de informação ao salvar valores como "0042", que virariam "42".

---

## Erro 03 — Caminho de template incorreto

**Como estava:**
'templates/portal/index.html'

**Problema:**
Django já busca automaticamente dentro da pasta templates.

**Correção:**
'portal/index.html'

**Impacto:**
Template não era encontrado (TemplateDoesNotExist).

---

## Erro 04 — Import inválido em forms

**Como estava:**
from models import Professor

**Problema:**
Import fora do padrão Django.

**Correção:**
from portal.models import Professor

**Impacto:**
Erro ModuleNotFoundError impedindo o carregamento do formulário.

---

## Erro 05 — Campo inexistente no admin

**Como estava:**
'especialidade'

**Problema:**
Campo não existe no modelo.

**Correção:**
'disciplina'

**Impacto:**
Erro no Django Admin impedindo abertura da listagem.

---

## Erro 06 — View inexistente no urls.py do app

**Como estava:**
path('cadastro/', views.cadastro)

**Problema:**
A view cadastro não existia.

**Correção:**
Criar a view ou remover a rota.

**Impacto:**
Erro AttributeError ao carregar as URLs.

---

## Erro 07 — SyntaxError no urls principal

**Como estava:**
path('cadastro/', preciso mostrar a página cadastro.html)

**Problema:**
Texto inválido dentro de código Python.

**Correção:**
path('cadastro/', views.cadastro)
OU
include('portal.urls')

**Impacto:**
O servidor não iniciava (SyntaxError).

---

## Erro 08 — App não registrado no settings

**Como estava:**
'portal' não estava no INSTALLED_APPS

**Problema:**
Django não reconhecia o app.

**Correção:**
'portal' adicionado ao INSTALLED_APPS

**Impacto:**
Models, admin e templates não funcionavam corretamente.

---

## Conclusão

Os erros estavam relacionados a:

- Configuração do Django
- Imports incorretos
- Views e URLs
- Models e Admin

Após as correções, o sistema funciona corretamente. Se a estrutura estivesse certa.



## Observação sobre a estrutura de templates

Analisando a estrutura apresentada na imagem, temos apenas os seguintes arquivos dentro de `templates/portal`:

- base.html
- index.html

Isso indica um problema direto de correspondência com as rotas e views do projeto.

---

## Problema esperado

A aplicação está configurada para renderizar páginas como:

- portal/cadastro.html

No entanto, esse arquivo não existe na estrutura atual.

---

## Consequência

Ao tentar acessar a rota `/cadastro/`, o Django irá gerar erro `TemplateDoesNotExist`, pois não há o template correspondente.

---

## Resultado atual do projeto

Com a configuração atual, apenas a rota:

- /admin/

irá funcionar corretamente, pois ela é nativa do Django e não depende desses templates.

---

## Conclusão

Sem a criação do arquivo `cadastro.html` (ou ajuste na view para apontar para `index.html` ou `base.html`), a aplicação não conseguirá renderizar a página de cadastro e falhará ao acessá-la.



###Trabalho Feito pelo Marino Teixeira Dos Santos Oliveira, O melhor aluno e Dev que você ja conheceu
