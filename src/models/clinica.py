class Clinica():
    def __init__(self, nome:str, localizacao:str, descricao:str):
        self.__nome = None
        self.__localizacao = None
        self.__descricao = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(localizacao, str):
            self.__localizacao = localizacao
        if isinstance(descricao, str):
            self.__descricao = descricao
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    @property
    def localizacao(self): 
        return self.__localizacao
    @localizacao.setter
    def localizacao(self, localizacao):
        if isinstance(localizacao, str):
            self.__localizacao = localizacao
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
    