from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_profissional import ControladorProfissional
from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_atendimento import ControladorAtendimento
from controllers.controlador_pagamento import ControladorPagamento
from controllers.controlador_relatorio import ControladorRelatorio
from views.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_relatorio = ControladorRelatorio(self)

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def abrir_menu(self):
        while True:
            opcao = self.__tela_sistema.mostra_menu_principal()
            if opcao == 1:
                self.__controlador_clinica.abrir_menu()
            elif opcao == 2:
                self.__controlador_profissional.abrir_menu()
            elif opcao == 3:
                self.__controlador_paciente.abrir_menu()
            elif opcao == 4:
                self.__controlador_atendimento.abrir_menu()
            elif opcao == 5:
                self.__controlador_pagamento.abrir_menu()
            elif opcao == 6:
                self.__controlador_relatorio.abrir_menu()
            elif opcao == 0:
                self.__tela_sistema.mostra_mensagem_saida()
                break
            else:
                self.__tela_sistema.mostra_opcao_invalida()