from models.dao.abstract_dao import AbstractDAO

class ClinicaDAO(AbstractDAO):
    def __init__(self):
        super().__init__("clinica.pkl")
    
    def add(self, nome, clinica):
        from models.clinica import Clinica
        if not isinstance(clinica, Clinica):
            raise TypeError("O objeto deve ser uma instância da classe Clinica.")
        super().add(nome, clinica)
    
    def get(self, nome):
        from models.clinica import Clinica
        clinica = super().get(nome)
        return clinica
    
    def remove(self, nome):
        from models.clinica import Clinica
        clinica = super().get(nome)
        if clinica is not None and not isinstance(clinica, Clinica):
            raise TypeError("O objeto deve ser uma instância da classe Clinica.")
        super().remove(nome)