from models.profissional import Profissional
from views.tela_profissional import TelaProfissional

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()

    @property
    def profissionais(self):
        return self.__profissionais

    def incluir_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        profissional = Profissional(dados_profissional['nome'], dados_profissional['celular'], 
                                    dados_profissional['cpf'], dados_profissional['especialidade'], 
                                    dados_profissional['registro_profissional'])
        self.__profissionais.append(profissional)