from pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago:float, cpf_pagador:str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    def calcular_restante(self) -> float:
        restante = self.atendimento.valor - self.valor_pago
        return restante

    