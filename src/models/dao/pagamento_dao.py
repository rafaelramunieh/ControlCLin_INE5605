from models.dao.abstract_dao import AbstractDAO

class PagamentoDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pagamentos.pkl")
    
    def add(self, codigo_pagamento, pagamento):
        from models.pagamento import Pagamento
        if not isinstance(pagamento, Pagamento):
            raise TypeError("O objeto deve ser uma instância da classe Pagamento.")
        super().add(codigo_pagamento, pagamento)