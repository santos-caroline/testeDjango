from django.shortcuts import render
from django.http import HttpResponse # Importa a classe responsável por gerar respostas HTTP
from .models import Usuario #da pasta de estou importe a pasta models e da pasta models importe a tabela usuário

def home(request): #arquitetura cliente-servidor -->> portanto precisamos de um retorno response
    # return HttpResponse('Olá você está na home!! ') #retorno de string

    if request.method == "GET":
        return render(request, 'home.html') #retorno de pag. html
    
    else:
        nome = request.POST.get('nome')

        user = Usuario( #instanciando no BD
            nome=nome

        )
        user.save() #salvar a instancia do disco

        return HttpResponse(nome)
    
    # request.POST: É um dicionário que contém todos os dados enviados pelo formulário (desde que o formulário 
    # use method="POST").

    # .get('nome'): Busca o valor do campo que tem o atributo name="nome" no HTML. Se o campo estiver vazio ou 
    # não existir, ele evita um erro e retorna None.

    # return HttpResponse(nome): Pega o conteúdo da variável nome e o envia de volta ao navegador como uma 
    # resposta simples, exibindo o texto puro na tela.