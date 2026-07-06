from datetime import time as Time
from models.atendimento import Atendimento
from models.data import Data
from models.tipo_atendimento import TipoAtendimento
from views.tela_atendimento import TelaAtendimento
from models.dao.atendimento_dao import AtendimentoDAO 


class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimento_dao = AtendimentoDAO()  
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimento_dao.get_all() 

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
                self.__tela_atendimento.mostra_mensagem("Opção inválida! Tente novamente.")

    def incluir_atendimento(self):
        nome_clinica = self.__tela_atendimento.pega_nome_clinica()
        clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(nome_clinica)
        if not clinica:
            self.__tela_atendimento.mostra_mensagem("Clínica não encontrada no sistema!")
            return

        cpf_paciente = self.__tela_atendimento.pega_cpf_paciente()
        paciente = self.__controlador_sistema.controlador_paciente.buscar_paciente(cpf_paciente)
        if not paciente:
            self.__tela_atendimento.mostra_mensagem("Paciente não encontrado no sistema!")
            return

        if paciente.idade < 18:
            self.__tela_atendimento.mostra_mensagem("Paciente menor de 18 anos não pode realizar atendimento de forma independente.")
            return

        cpf_profissional = self.__tela_atendimento.pega_cpf_profissional()
        profissional = self.__controlador_sistema.controlador_profissional.buscar_profissional(cpf_profissional)
        if not profissional:
            self.__tela_atendimento.mostra_mensagem("Profissional não encontrado no sistema!")
            return

        tipo_atendimento = self.__tela_atendimento.pega_tipo_atendimento()
        if tipo_atendimento is None:
            return

        dados = self.__tela_atendimento.pega_dados_atendimento()
        if dados is None:
            return

        try:
            data = Data(dados['dia'], dados['mes'], dados['ano'])
            h_ini, m_ini = map(int, dados['horario_inicio'].split(':'))
            h_fim, m_fim = map(int, dados['horario_fim'].split(':'))
            horario_inicio = Time(h_ini, m_ini)
            horario_fim = Time(h_fim, m_fim)
        except (ValueError, TypeError):
            self.__tela_atendimento.mostra_mensagem("Dados de data ou horário inválidos.")
            return

        # Lógica para gerar código auto-incremental seguro para o DAO
        todos = self.__atendimento_dao.get_all()
        proximo_codigo = max([a.codigo for a in todos]) + 1 if todos else 1

        atendimento = Atendimento(
            codigo=proximo_codigo,
            clinica=clinica,
            paciente=paciente,
            profissional=profissional,
            data=data,
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            tipoAtendimento=tipo_atendimento
        )

        # Salva no arquivo de forma persistente
        self.__atendimento_dao.add(atendimento.codigo, atendimento)
        self.__tela_atendimento.mostra_mensagem("Atendimento agendado com sucesso!")

    def listar_atendimentos(self):
        self.__tela_atendimento.mostra_atendimentos(self.__atendimento_dao.get_all())

    def excluir_atendimento(self):
        todos_atendimentos = self.__atendimento_dao.get_all()
        if not todos_atendimentos:
            self.__tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
            
        self.__tela_atendimento.mostra_atendimentos(todos_atendimentos)
        
        # Pede o código único do atendimento via view para exclusão limpa no DAO
        codigo_excluir = self.__tela_atendimento.pega_codigo_atendimento_excluir()
        
        atendimento_encontrado = self.__atendimento_dao.get(codigo_excluir)
        if atendimento_encontrado:
            self.__atendimento_dao.remove(codigo_excluir)
            self.__tela_atendimento.mostra_mensagem(f"Atendimento do dia {atendimento_encontrado.data} excluído.")
        else:
            self.__tela_atendimento.mostra_mensagem("Código de atendimento inválido.")