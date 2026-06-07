class Clinica():
    def __init__(self, nome: str, localizacao: str, descricao: str, horario_abertura: str, horario_fechamento: str):
        self.__nome = nome if isinstance(nome, str) else None
        self.__localizacao = localizacao if isinstance(localizacao, str) else None
        self.__descricao = descricao if isinstance(descricao, str) else None
        self.__horario_abertura = horario_abertura if isinstance(horario_abertura, str) else None
        self.__horario_fechamento = horario_fechamento if isinstance(horario_fechamento, str) else None

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

    @property
    def horario_abertura(self):
        return self.__horario_abertura
    @horario_abertura.setter
    def horario_abertura(self, horario_abertura):
        if isinstance(horario_abertura, str):
            self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento
    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento):
        if isinstance(horario_fechamento, str):
            self.__horario_fechamento = horario_fechamento