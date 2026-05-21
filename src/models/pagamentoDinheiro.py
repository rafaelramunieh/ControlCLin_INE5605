from pagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago:float)
        super().__init__(data, atendimento, paciente, valor_pago)
    
    def calcular_restante(self) -> float:
        restante = self.atendimento.valor - self.valor_pago
        return restante
    