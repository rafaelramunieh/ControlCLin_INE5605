from models.paciente import Paciente
from views.tela_paciente import TelaPaciente
from models.dao.paciente_dao import PacienteDAO

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__paciente_dao = PacienteDAO()

    @property
    def pacientes(self):
        return self.__paciente_dao.get_all()

    def abrir_menu(self):
        while True:
            opcao = self.__tela_paciente.mostra_menu_paciente()
            
            if opcao == 1:
                self.incluir_paciente()
                
            elif opcao == 2:
                self.listar_pacientes()
                
            elif opcao == 3:
                cpf = self.__tela_paciente.pega_cpf("excluído")
                self.excluir_paciente(cpf)

            elif opcao == 4:
                cpf = self.__tela_paciente.pega_cpf("editado")
                self.editar_paciente(cpf)

            elif opcao == 5:
                break

            else:
                self.__tela_paciente.mostra_opcao_invalida()
             
    def incluir_paciente(self):
        dados_paciente = self.__tela_paciente.pega_dados_paciente()
        
        # Correção para o botão Cancelar / Fechar janela
        if dados_paciente is None:
            return

        if not dados_paciente['nome'] or not dados_paciente['nome'].strip():
            self.__tela_paciente.mostra_mensagem("Nome não pode ser vazio.")
            return
        if not dados_paciente['cpf'] or not dados_paciente['cpf'].strip():
            self.__tela_paciente.mostra_mensagem("CPF não pode ser vazio.")
            return
        if self.buscar_paciente(dados_paciente['cpf']):
            self.__tela_paciente.mostra_mensagem("Já existe um paciente com esse CPF.")
            return

        paciente = Paciente(dados_paciente['nome'], dados_paciente['celular'],
                            dados_paciente['cpf'], dados_paciente['idade'])
        self.__paciente_dao.add(dados_paciente['cpf'], paciente)
        self.__tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")

    def buscar_paciente(self, cpf):
        return self.__paciente_dao.get(cpf)

    def excluir_paciente(self, cpf):
        paciente = self.buscar_paciente(cpf)
        if paciente:
            self.__paciente_dao.remove(cpf)
            self.__tela_paciente.mostra_mensagem(f"Paciente com CPF {cpf} excluído.")
            return
        self.__tela_paciente.mostra_mensagem(f"Paciente com CPF {cpf} não encontrado.")

    def editar_paciente(self, cpf):
        paciente = self.buscar_paciente(cpf)
        if paciente:
            dados_paciente = self.__tela_paciente.pega_dados_paciente()
            
            # Correção para o botão Cancelar / Fechar janela na edição
            if dados_paciente is None:
                return

            paciente.nome = dados_paciente['nome']
            paciente.celular = dados_paciente['celular']
            paciente.idade = dados_paciente['idade']
            self.__tela_paciente.mostra_mensagem(f"Paciente com CPF {cpf} editado.")
            self.__paciente_dao.add(cpf, paciente)  # Atualiza o paciente no DAO
            return
        self.__tela_paciente.mostra_mensagem(f"Paciente com CPF {cpf} não encontrado.")

    def listar_pacientes(self):
        pacientes = self.__paciente_dao.get_all()
        self.__tela_paciente.mostra_pacientes(pacientes)