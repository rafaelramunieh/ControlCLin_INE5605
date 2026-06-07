from models.tipo_atendimento import TipoAtendimento
from models.clinica import Clinica
from models.paciente import Paciente
from models.profissional import Profissional
from models.data import Data
from datetime import time as Time
from models.pagamento import Pagamento


class Atendimento():
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional,
                 data: Data, horario_inicio: Time, horario_fim: Time, tipoAtendimento: TipoAtendimento):
        self.__clinica = None
        if isinstance(clinica, Clinica):
            self.__clinica = clinica
        self.__paciente = None
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        self.__profissional = None
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        self.__data = None
        if isinstance(data, Data):
            self.__data = data
        self.__horario_inicio = None
        if isinstance(horario_inicio, Time):
            self.__horario_inicio = horario_inicio
        self.__horario_fim = None
        if isinstance(horario_fim, Time):
            self.__horario_fim = horario_fim
        self.__tipoAtendimento = None
        if isinstance(tipoAtendimento, TipoAtendimento):
            self.__tipoAtendimento = tipoAtendimento
        self.__pagamentos = []
        self.__procedimentos = []

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        if isinstance(clinica, Clinica):
            self.__clinica = clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, Data):
            self.__data = data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        if isinstance(horario_inicio, Time):
            self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        if isinstance(horario_fim, Time):
            self.__horario_fim = horario_fim

    @property
    def tipoAtendimento(self):
        return self.__tipoAtendimento

    @tipoAtendimento.setter
    def tipoAtendimento(self, tipoAtendimento):
        if isinstance(tipoAtendimento, TipoAtendimento):
            self.__tipoAtendimento = tipoAtendimento

    @property
    def valor(self) -> float:
        valor_total = self.__tipoAtendimento.valor_base if self.__tipoAtendimento else 0.0
        return valor_total + sum(proc.custo for proc in self.__procedimentos)

    @property
    def procedimentos(self):
        return self.__procedimentos

    def adicionar_pagamento(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            self.__pagamentos.append(pagamento)

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    def calcula_restante(self) -> float:
        total_pago = sum(pag.valor_pago for pag in self.__pagamentos)
        return max(0.0, self.valor - total_pago)