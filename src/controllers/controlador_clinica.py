from models.clinica import Clinica
from views.tela_clinica import TelaClinica

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()

    @property
    def clinicas(self):
        return self.__clinicas

    def abrir_menu(self): 
        while True:
            opcao = self.__tela_clinica.mostra_menu_clinica()
            if opcao == 1:
                self.incluir_clinica()
            elif opcao == 2:
                self.listar_clinicas()
            elif opcao == 3:
                nome = input("Digite o nome da clínica a ser excluída: ")
                self.excluir_clinica(nome)
            elif opcao == 4:
                nome = input("Digite o nome da clínica a ser editada: ")
                self.editar_clinica(nome)
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def incluir_clinica(self):
        dados_clinica = self.__tela_clinica.pega_dados_clinica()

        if not dados_clinica['nome'] or not dados_clinica['nome'].strip():
            print("Nome não pode ser vazio.")
            return
        if not dados_clinica['localizacao'] or not dados_clinica['localizacao'].strip():
            print("Localização não pode ser vazia.")
            return
        if self.buscar_clinica(dados_clinica['nome']):
            print("Já existe uma clínica com esse nome.")
            return

        clinica = Clinica(dados_clinica['nome'], dados_clinica['localizacao'], 
                          dados_clinica['descricao'], dados_clinica['horario_abertura'], 
                          dados_clinica['horario_fechamento'])

        if not clinica.horario_abertura or not clinica.horario_fechamento:
            print("Clínica não cadastrada devido a horário inválido.")
            return

        self.__clinicas.append(clinica)
        print("Clínica cadastrada com sucesso!")
    
    def buscar_clinica(self, nome):
        for clinica in self.__clinicas:
            if clinica.nome.lower() == nome.lower():
                return clinica
        return None
    
    def excluir_clinica(self, nome):
        clinica = self.buscar_clinica(nome)
        if clinica:
            self.__clinicas.remove(clinica)
            print(f"Clínica '{nome}' excluída.")
            return
        print(f"Clínica '{nome}' não encontrada.")
    
    def editar_clinica(self, nome):
        clinica = self.buscar_clinica(nome)
        if not clinica:
            print(f"Clínica '{nome}' não encontrada.")
            return

        dados_clinica = self.__tela_clinica.pega_dados_clinica()

        if not dados_clinica['localizacao'] or not dados_clinica['localizacao'].strip():
            print("Localização não pode ser vazia.")
            return

        clinica.localizacao = dados_clinica['localizacao']
        clinica.descricao = dados_clinica['descricao']
        clinica.horario_abertura = dados_clinica['horario_abertura']                
        clinica.horario_fechamento = dados_clinica['horario_fechamento']
        print(f"Clínica '{nome}' editada com sucesso.")
    
    def listar_clinicas(self):
        self.__tela_clinica.mostra_clinicas(self.__clinicas)