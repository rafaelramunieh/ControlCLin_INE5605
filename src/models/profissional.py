from pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome:str, celular:int, cpf:str, especialidade:str, registro_profissional:str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = None
        if isinstance(especialidade, str):
            self.__especialidade = especialidade
        self.__registro_profissional = None
        if isinstance(registro_profissional, str):
            self.__registro_profissional = registro_profissional

    @property
    def especialidade(self):
        return self.__especialidade
    @especialidade.setter
    def especialidade(self, especialidade):
        if isinstance(especialidade, str):
            self.__especialidade = especialidade

    @property
    def registro_profissional(self):
        return self.__registro_profissional
    @registro_profissional.setter
    def registro_profissional(self, registro_profissional):
        if isinstance(registro_profissional, str):
            self.__registro_profissional = registro_profissional