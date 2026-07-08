from .abstract_dao import AbstractDAO

class ProfissionalDAO(AbstractDAO):
    def __init__(self):
        super().__init__("profissional.pkl")
    
    def add(self, nome, profissional):
        from models.profissional import Profissional
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto deve ser uma instância da classe Profissional.")
        super().add(nome, profissional)
    
    def get(self, nome):
        from models.profissional import Profissional
        profissional = super().get(nome)
        return profissional
    
    def remove(self, nome):
        from models.profissional import Profissional
        profissional = super().get(nome)
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto deve ser uma instância da classe Profissional.")
        super().remove(nome)