from dao.abstract_dao import AbstractDAO as DAO

class PacienteDAO(DAO):

    def __init__(self):
        super().__init__("pacientes.pkl")

    def add(self, cpf, paciente):
        from models.paciente import Paciente
        if not isinstance(paciente, Paciente):
            raise TypeError("O objeto deve ser uma instância da classe Paciente.")
        super().add(cpf, paciente)

    def get(self, cpf):
        return super().get(cpf)

    def remove(self, cpf):
        super().remove(cpf)