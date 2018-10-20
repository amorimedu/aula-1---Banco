# Classe Física

from CLIENTE import Cliente

class Fisica(Cliente):

    # Método construtor

        def __init__(self, nome, idade, cpf):

            super().__init__(nome, idade)
            self.cpf = cpf

    # Método get

        def get_cpf(self):
            return self.cpf