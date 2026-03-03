from django.db import models

# parte do BD

class Usuario(models.Model): 
    #Conceito ORM (Object-Relational Mapping), onde uma classe Python representa uma tabela.
    #class Usuario: Define o nome da sua tabela no banco de dados (geralmente o Django a salvará como app_Usuario)

    #(models.Model): Indica que esta classe é uma subclasse de models.Model. Isso é obrigatório para que o Django
    #entenda que essa classe deve ser transformada em uma tabela e ganhe superpoderes, como métodos para salvar, 
    #excluir e buscar dados.

    nome = models.CharField(max_length=50)
        # nome: É o nome da coluna no banco de dados e o nome do atributo que você usará no Python.

        # models.CharField: Define o tipo de dado como "caractere" (texto). No banco de dados (SQL), isso 
        # geralmente vira um VARCHAR.

        # max_length=50: Obrigatório. Define o limite máximo de caracteres. Isso ajuda o banco de dados a 
        # reservar o espaço correto e valida os dados automaticamente (se você tentar salvar 51 caracteres, o 
        # Django retornará um erro).