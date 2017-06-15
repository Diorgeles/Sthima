# TO-DO LIST
Sistema para avaliação da empresa Sthima

# Desafio
Vaga de desenvolvedor
 
# Descrição
Criar um sistema que funcione como uma lista de tarefas
 
Escrita em:
  * Python 3.5.2
  * Django 1.11.1

# Instalação

Clone o projeto


```shell

$ git clone git@github.com:Diorgeles/Sthima.git

```

Instale os pacotes necessários


```shell

$ pip install -r requirements.txt

```

Execute as migrations


```shell

$ python manage.py migrate 

```

Crie um superusuario

```shell

$ python manage.py createsuperuser 

```

# Forma de uso

- Para cadastrar uma tarefa basta clicar no button na parte superior da tela
- Para editar basta clicar no lápis que aparece em cada tarefa acrescentada
- Para excluir basta clicar no "x"
- Para marcar/desmarcar como feito, basta clicar no lápis de edição e no modal que abrirá mostrará o campo para edição

# Funcionalidades

- É possível mover as tarefas e organiza-las, basta clicar e arrastar a tarefa e reordena-la
    - Esta funcionalidade não salva a nova ordem no banco, a solução encontrada que pudesse atender as 24h não ficou muito boa.
- Ao final de cada linha da tarefa mostra o status dela, se está feita ou sem fazer
