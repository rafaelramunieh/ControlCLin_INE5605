from models.dao.abstract_dao import AbstractDAO

class PacienteDAO(AbstractDAO):

    def __init__(self):
        super().__init__("pacientes.pkl")

    def add(self, cpf, paciente):
        from models.paciente import Paciente
        if not isinstance(paciente, Paciente):
            raise TypeError("O objeto deve ser uma instância da classe Paciente.")
        super().add(cpf, paciente)
    
    def get(self, cpf):
        from models.paciente import Paciente
        paciente = super().get(cpf)
        if paciente is not None and not isinstance(paciente, Paciente):
            raise TypeError("O objeto recuperado não é uma instância da classe Paciente.")
        return paciente
    
    def remove(self, cpf):
        from models.paciente import Paciente
        paciente = super().get(cpf)
        if paciente is not None and not isinstance(paciente, Paciente):
            raise TypeError("O objeto a ser removido não é uma instância da classe Paciente.")
        super().remove(cpf)