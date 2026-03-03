# Sua Primeira aplicacao web com Django por pythonando

### Criando o projeto a partir do terminal VSCode

````
django-admin startproject primeiroProjetoDjando .
````
- esse espaço . depois do nome do projeto indica que vamos criar o projeto já nessa pasta que estamos

### pasta manage.py

O seu painel de controle via linha de comando para o projeto Django. Ele é criado automaticamente quando você inicia um projeto e serve como um "atalho" para as ferramentas administrativas do framework. Nele pode ser feito: 

1. Gerenciamento do Banco de Dados: Ele é o responsável por aplicar mudanças que você faz nos seus modelos (tabelas) ao banco de dados real.

``makemigrations``: Cria as instruções de mudança.

``migrate`` : Aplica essas mudanças no banco.

2. Execução do Servidor de Desenvolvimento: Como você tentou fazer no seu print, o comando ``runserver`` inicia um servidor web leve na sua máquina para que você possa testar o site em tempo real (geralmente em http://127.0.0.1:8000).

3. Criação de Componentes e Usuários: 

``startapp``: Cria a estrutura de pastas para uma nova funcionalidade do site.

``createsuperuser``: Cria o login de administrador para você acessar o painel /admin.

- no terminal rodamos o comando `` python manage.py runserver`` para iniciar o servidor web geralmente na porta 8080
- enquando estiver aberto esse comando no terminal ele roda no navegador

### Criando um app (dividindo a aplicaçaõ em pequenas partes)

``python manage.py startapp home`` no terminal e criamos uma pasta com nome home

- para o Django reconhcer home como app precisamos add no aquivo ``settings.py`` da pasta principal (nesse caso: primeiroProjetoDjango)
- essa mudança é feita em: ´
    INSTALLED_APPS = [
        ...
        'home'   <-- o app criado
    ]

### Aplicações WEB são baseadas em Rotas

- Dependendo da URL temos um processamento diferente
- No Django precisamos criar essas URLs, vamos fazer em ``urls.py`` (arquivo responsável por gerenciar as URLs)

- as rotas ficam em: 
urlpatterns = [
    path('admin/', admin.site.urls)  ->> usamos dois parametros: 1º string, 2º função (em views.py)
]

- para cadastrar uma nova escrevemos a função em *views.py da pasta home* e importamos o arquivo em urls.py
- escreva a função em views.py da pasta home !!

### arquivos.py

- models.py    -->>  gerenciar o BD
- views.py     -->>  funções python responsáveis pelo gerenciamento de URLs
- templates.py -->> o que o u´suario vê na tela (HTML)

### Response com HTML (está definido em views. py em home)

Criar nosso HTML que vai ser exibido:

- na pasta home criar nova pasta templetes
- dentro da pasta criar arquivo home.html (mesmo caminho descrito em render)

#### Aqrquivo em HTML:

````HTML
<form action="/home/" method="POST">{% csrf_token %}    
    #atributo action define para onde os dados serão enviados

    #method='POST' envia as informações 'escondidas' no corpo da requisiçaõ HTTP, e não pela URL (como o método GET)

    # {% csrf_token %} -- Esta é uma tag de template do Django para segurança
        - O que significa: CSRF significa Cross-Site Request Forgery (Falsificação de Solicitação Entre Sites).

        - Como funciona: O Django gera um código único e secreto para cada sessão de usuário. Ao incluir essa tag, ele insere um campo oculto (<input type="hidden">) no formulário com esse código.

        - O objetivo: Garante que o formulário enviado veio realmente do seu site e não de um hacker tentando enviar comandos maliciosos em nome do usuário logado. Sem isso, o Django bloqueará o envio por segurança


    <input type="text" name="nome">     
            #type="text" cria uma caixa de entrada de texto simples.

            #name="nome" é o identificador. Sem isso, o servidor não sabe como chamar o dado que foi digitado
    
    <input type="submit" value="Salvar">
        #type="submit" transforma o botão em um gatilho de envio. Ao clicar nele, o navegador empacota os dados dos campos acima e os envia para o destino definido no action.

        #value="Salvar" é apenas o texto que aparece escrito dentro do botão.    
</form>
````

### Guardar respostas do POST no BD

- no arquivo models.py ficam as configurações do BD
- depois de configurar a parte da tabela (comentários no proprio arquivo)

- no terminal ````python manage.py makemigrations````

- no terminal ````python manage.py migrate````

#### O Fluxo do Django:

| Passo | Comando                         | O que acontece?                                                                 |
|-------|---------------------------------|----------------------------------------------------------------------------------|
| 1     | Alterar o `models.py`           | Você define a estrutura da tabela (campos e tipos de dados).                   |
| 2     | `python manage.py makemigrations` | O Django cria o "manual de instruções" da mudança (arquivo de migração .py). |
| 3     | `python manage.py migrate`      | O Django lê o manual e executa no banco, criando/alterando a tabela no SQL.   |

### Visualizar as informações do BD Pelo Admin do Django
- 1. criar superusuario: no terminal ````python manage.py createsuperuser````
    - ele vai pedir (exemplo de preenchimento):

        Username: (leave blank to use 'carol')

        Email address: carol@email.com

        Password:01234

        Password (again):01234

        Bypass password validation and create user anyway? [y/N]: y


- 2. Precisamos conf o arquivo admin.py pra mostrar a tabela no painel administrativo:


````` python
from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Usuario, UsuarioAdmin)
`````


1️⃣ from django.contrib import admin: Aqui você está importando o sistema de administração que já vem pronto no Django. É ele que cria a tela: ````/admin````


2️⃣ from .models import Usuario: Aqui você está dizendo:  "Quero usar o model Usuario que está no meu models.py"

O ponto (.) significa: 👉 "da pasta atual" (no seu caso, o app home)

3️⃣ admin.site.register(Usuario): *Você está registrando o model no painel admin.*, ou seja, você diz "Django, mostra a tabela Usuario no admin." Sem isso, o admin ignora o model.


- 3. Tabela vai estar em : http://127.0.0.1:8000/admin 