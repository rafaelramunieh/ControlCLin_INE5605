from clinica import Clinica
from paciente import Paciente
from profissional import Profissional
from data import Data
import time as Time

class Atendimento():
    def __init__(self, clinica:Clinica, paciente:Paciente, profissional:Profissional, data:Data, horario_inicio:Time, horario_fim:Time, tipo:str, valor:float):
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
        if isinstance(data, str):
            self.__data = data
        self.__horario_inicio = None
        if isinstance(horario_inicio, str):
            self.__horario_inicio = horario_inicio
        self.__horario_fim = None
        if isinstance(horario_fim, str):
            self.__horario_fim = horario_fim
        self.__tipo = None
        if isinstance(tipo, str):
            self.__tipo = tipo
        self.__valor = None
        if isinstance(valor, float):
            self.__valor = valor
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
        if isinstance(data, str):
            self.__data = data
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        if isinstance(horario_inicio, str):
            self.__horario_inicio = horario_inicio
    @property
    def horario_fim(self):  
        return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, horario_fim):
        if isinstance(horario_fim, str):
            self.__horario_fim = horario_fim
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            self.__tipo = tipo
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor
    