class Pessoa:

    def __init__(self,nome,cpf,idade):
        self.__nome=nome
        self.__cpf=cpf
        self.__idade=idade

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self,nome):
         self.__nome=nome

    @cpf.setter
    def cpf(self,cpf):
         self.__cpf=cpf

    @idade.setter
    def idade(self,idade):
         self.__idade=idade

teste=Pessoa('Pedro Paulo','052.987.651-05',26)
print(f'NOME: {teste.nome} CPF: {teste.cpf} IDADE {teste.idade}')
teste.nome='Igor'
teste.idade='20'
print(f'NOME: {teste.nome} CPF: {teste.cpf} IDADE {teste.idade}')
