from profissional import Profissional

class Procedimento():
    def __init__(self, descricao:str, custo:float, profissional:Profissional):
        self.__descricao = None
        if isinstance(descricao, str):
            self.__descricao = descricao
        self.__custo = None
        if isinstance(custo, float):
            self.__custo = custo
        self.__profissional = None
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
    @property
    def custo(self):
        return self.__custo
    @custo.setter
    def custo(self, custo):
        if isinstance(custo, float):
            self.__custo = custo
    @property
    def profissional(self):
        return self.__profissional
    @profissional.setter
    def profissional(self, profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        