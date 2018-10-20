# Classe Cliente

class Cliente:

    # Métod construtor

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    # Métodos get

        def get_nome(self):
            return self.nome

        def get_idade(self):
            return self.idade