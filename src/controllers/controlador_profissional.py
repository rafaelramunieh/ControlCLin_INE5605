from models.profissional import Profissional
from views.tela_profissional import TelaProfissional
from models.dao.profissional_dao import ProfissionalDAO

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()
        self.__profissional_dao = ProfissionalDAO()

    @property
    def profissionais(self):
        return self.__profissional_dao.get_all()

    def abrir_menu(self): 
        while True:
            opcao = self.__tela_profissional.mostra_menu_profissional()
            if opcao == 1:
                self.incluir_profissional()
            elif opcao == 2:
                self.listar_profissionais()
            elif opcao == 3:
                cpf = input("Digite o CPF do profissional a ser excluído: ")
                self.excluir_profissional(cpf)
            elif opcao == 4:
                cpf = input("Digite o CPF do profissional a ser editado: ")
                self.editar_profissional(cpf)
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def incluir_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        profissional = Profissional(dados_profissional['nome'], dados_profissional['celular'], 
                                    dados_profissional['cpf'], dados_profissional['especialidade'], 
                                    dados_profissional['registro_profissional'])
        self.__profissional_dao.add(dados_profissional['cpf'], profissional)
    
    def buscar_profissional(self, cpf):
        return self.__profissional_dao.get(cpf)
    
    def excluir_profissional(self, cpf):
        profissional = self.buscar_profissional(cpf)
        if profissional:
            self.__profissional_dao.remove(cpf)
            print(f"Profissional com CPF {cpf} excluído.")
            return
        print(f"Profissional com CPF {cpf} não encontrado.")
    
    def editar_profissional(self, cpf):
        profissional = self.buscar_profissional(cpf)
        if profissional:
            dados_profissional = self.__tela_profissional.pega_dados_profissional()
            profissional.nome = dados_profissional['nome']
            profissional.celular = dados_profissional['celular']
            profissional.especialidade = dados_profissional['especialidade']
            profissional.registro_profissional = dados_profissional['registro_profissional']
            print(f"Profissional com CPF {cpf} editado.")
            self.__profissional_dao.add(cpf, profissional)  # Atualiza o profissional no DAO
            return
        print(f"Profissional com CPF {cpf} não encontrado.")
    
    def listar_profissionais(self):
        self.__tela_profissional.mostra_profissionais(self.profissionais)
        