from datetime import time as Time
from models.atendimento import Atendimento
from models.data import Data
from models.tipo_atendimento import TipoAtendimento
from views.tela_atendimento import TelaAtendimento


class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = []
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abrir_menu(self):
        while True:
            opcao = self.__tela_atendimento.mostra_menu_atendimento()
            if opcao == 1:
                self.incluir_atendimento()
            elif opcao == 2:
                self.listar_atendimentos()
            elif opcao == 3:
                self.excluir_atendimento()
            elif opcao == 4:
                break
            else:
                self.__tela_atendimento.mostra_mensagem(f"\n[Erro] Opção inválida! Tente novamente.")

    def incluir_atendimento(self):

        dados = self.__tela_atendimento.pega_dados_atendimento()

        clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(
            dados["clinica_nome"]
        )

        if not clinica:
            self.__tela_atendimento.mostra_mensagem(
                "\n[Erro] Clínica não encontrada no sistema!"
            )
            return

        paciente = self.__controlador_sistema.controlador_paciente.buscar_paciente(
            dados["paciente_cpf"]
        )

        if not paciente:
            self.__tela_atendimento.mostra_mensagem(
                "\n[Erro] Paciente não encontrado no sistema!"
            )
            return

        if paciente.idade < 18:
            self.__tela_atendimento.mostra_mensagem(
                "\n[Erro] Paciente menor de 18 anos não pode realizar atendimento."
            )
            return

        profissional = self.__controlador_sistema.controlador_profissional.buscar_profissional(
            dados["profissional_cpf"]
        )

        if not profissional:
            self.__tela_atendimento.mostra_mensagem(
                "\n[Erro] Profissional não encontrado no sistema!"
            )
            return

        tipo_atendimento = self.__tela_atendimento.pega_tipo_atendimento()

        if tipo_atendimento is None:
            return

        try:
            dia, mes, ano = map(int, dados["data"].split("/"))

            data = Data(dia, mes, ano)

            h_ini, m_ini = map(int, dados["horario_inicio"].split(":"))
            h_fim, m_fim = map(int, dados["horario_fim"].split(":"))

            horario_inicio = Time(h_ini, m_ini)
            horario_fim = Time(h_fim, m_fim)

        except (ValueError, TypeError):
            self.__tela_atendimento.mostra_mensagem(
                "\n[Erro] Data ou horário inválidos."
            )
            return

        atendimento = Atendimento(
            clinica=clinica,
            paciente=paciente,
            profissional=profissional,
            data=data,
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            tipoAtendimento=tipo_atendimento
        )

        self.__atendimentos.append(atendimento)

        self.__tela_atendimento.mostra_mensagem(
            "\n[Sucesso] Atendimento agendado com sucesso!"
        )
        
    def listar_atendimentos(self):
        self.__tela_atendimento.mostra_atendimentos(self.__atendimentos)

    def excluir_atendimento(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem(f"Nenhum atendimento cadastrado.")
            return
        self.__tela_atendimento.mostra_atendimentos(self.__atendimentos)
        try:
            indice = int(input("\nDigite o número do atendimento que deseja excluir: ")) - 1
            if 0 <= indice < len(self.__atendimentos):
                removido = self.__atendimentos.pop(indice)
                self.__tela_atendimento.mostra_mensagem(f"\nAtendimento do dia {removido.data} excluído.")
            else:
                self.__tela_atendimento.mostra_mensagem(f"\nNúmero inválido.")
        except ValueError:
            self.__tela_atendimento.mostra_mensagem(f"\nEntrada inválida.")