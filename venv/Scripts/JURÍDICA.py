# CLASSE JURÍDICA

from CLIENTE import Cliente

class Juridica(Cliente):

    # Método construtor

        def __init__(self, cnpj):

            super().__init__(nome, idade)
            self.cnpj = cnpj

    # Método get

        def get_cnpj(self):
            return self.cnpj