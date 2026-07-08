from .abstract_dao import AbstractDAO

class ProfissionalDAO(AbstractDAO):
    def __init__(self):
        super().__init__("profissional.pkl")
    
    def add(self, cpf, profissional):
        from models.profissional import Profissional
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto deve ser uma instância da classe Profissional.")
        super().add(cpf, profissional)
    
    def get(self, cpf):
        from models.profissional import Profissional
        profissional = super().get(cpf)
        return profissional
    
    def remove(self, cpf):
        from models.profissional import Profissional
        profissional = super().get(cpf)
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto deve ser uma instância da classe Profissional.")
        super().remove(cpf)