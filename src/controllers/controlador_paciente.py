from models.paciente import Paciente
from views.tela_paciente import TelaPaciente

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()

    @property
    def pacientes(self):
        return self.__pacientes

    def abrir_menu(self): 
        while True:
            opcao = self.__tela_paciente.mostra_menu_paciente()
            if opcao == 1:
                self.incluir_paciente()
            elif opcao == 2:
                self.listar_pacientes()
            elif opcao == 3:
                cpf = input("Digite o CPF do paciente a ser excluído: ")
                self.excluir_paciente(cpf)
            elif opcao == 4:
                cpf = input("Digite o CPF do paciente a ser editado: ")
                self.editar_paciente(cpf)
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def incluir_paciente(self):
        dados_paciente = self.__tela_paciente.pega_dados_paciente()
        paciente = Paciente(dados_paciente['nome'], dados_paciente['celular'], 
                            dados_paciente['cpf'], dados_paciente['idade'])
        self.__pacientes.append(paciente)
    
    def buscar_paciente(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None
    
    def excluir_paciente(self, cpf):
        paciente = self.buscar_paciente(cpf)
        if paciente:
            self.__pacientes.remove(paciente)
            print(f"Paciente com CPF {cpf} excluído.")
            return
        print(f"Paciente com CPF {cpf} não encontrado.")
    
    def editar_paciente(self, cpf):
        paciente = self.buscar_paciente(cpf)
        if paciente:
            dados_paciente = self.__tela_paciente.pega_dados_paciente()
            paciente.nome = dados_paciente['nome']
            paciente.celular = dados_paciente['celular']
            paciente.idade = dados_paciente['idade']
            print(f"Paciente com CPF {cpf} editado.")
            return
        print(f"Paciente com CPF {cpf} não encontrado.")
    
    def listar_pacientes(self):
        self.__tela_paciente.mostra_pacientes(self.__pacientes)
    