from models.dao.abstract_dao import AbstractDAO

class AtendimentoDAO(AbstractDAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, codigo: int, atendimento):
        from models.atendimento import Atendimento
        if not isinstance(atendimento, Atendimento):
            raise TypeError("O objeto deve ser uma instância da classe Atendimento.")
        super().add(codigo, atendimento)