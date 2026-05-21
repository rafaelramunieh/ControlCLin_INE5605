from pagamento import Pagamento

class pagamentoCartaoCredito(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago:float, numero_cartao: str, bandeira_cartao:str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira_cartao = bandeira_cartao

    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @property
    def bandeira_cartao(self):
        return self.__bandeira_cartao
    
    def calcula_restante(self) -> float:
        restante = self.atendimento.valor - self.valor_pago
        return restante