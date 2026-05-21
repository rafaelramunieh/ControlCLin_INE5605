from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, data:int, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago
    
    @property
    def data(self):
        return self.__data
    
    @property
    def atendimento(self):
        return self.__atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @abstractmethod
    def calcula_restante(self) -> float:
        pass
    
    