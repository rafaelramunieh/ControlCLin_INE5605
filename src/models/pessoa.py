class Pessoa():
    def __init__(self, nome:str, celular:int, cpf:str):
        self.__nome = None
        self.__celular = None
        self.__cpf = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(celular, int):
            self.__celular = celular
        if isinstance(cpf, str):
            self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def celular(self):
        return self.__celular
    @celular.setter
    def celular(self, celular):
        if isinstance(celular, int):
            self.__celular = celular
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf
