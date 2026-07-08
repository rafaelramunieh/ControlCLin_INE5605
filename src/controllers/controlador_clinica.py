from models.clinica import Clinica
from views.tela_clinica import TelaClinica
from models.dao.clinica_dao import ClinicaDAO

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()
        self.__clinica_dao = ClinicaDAO()

    @property
    def clinicas(self):
        return self.__clinica_dao.get_all()

    def abrir_menu(self): 
        while True:
            opcao = self.__tela_clinica.mostra_menu_clinica()
            if opcao == 1:
                self.incluir_clinica()
            elif opcao == 2:
                self.listar_clinicas()
            elif opcao == 3:
                nome = self.__tela_clinica.pega_nome_clinica("excluída")
                self.excluir_clinica(nome)
            elif opcao == 4:
                nome = self.__tela_clinica.pega_nome_clinica("editada")
                self.editar_clinica(nome)
            elif opcao == 5:
                break
            else:
                self.__tela_clinica.mostra_opcao_invalida()
    
    def incluir_clinica(self):
        dados_clinica = self.__tela_clinica.pega_dados_clinica()

        if not dados_clinica['nome'] or not dados_clinica['nome'].strip():
            self.__tela_clinica.mostra_mensagem("Nome não pode ser vazio.")
            return
        if not dados_clinica['localizacao'] or not dados_clinica['localizacao'].strip():
            self.__tela_clinica.mostra_mensagem("Localização não pode ser vazia.")
            return
        if self.buscar_clinica(dados_clinica['nome']):
            self.__tela_clinica.mostra_mensagem("Já existe uma clínica com esse nome.")
            return

        clinica = Clinica(dados_clinica['nome'], dados_clinica['localizacao'], 
                          dados_clinica['descricao'], dados_clinica['horario_abertura'], 
                          dados_clinica['horario_fechamento'])

        if not clinica.horario_abertura or not clinica.horario_fechamento:
            self.__tela_clinica.mostra_mensagem("Clínica não cadastrada devido a horário inválido.")
            return
        
        self.__clinica_dao.add(dados_clinica['nome'], clinica)
        self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")

    def buscar_clinica(self, nome):
        return self.__clinica_dao.get(nome)
    
    def excluir_clinica(self, nome):
        clinica = self.buscar_clinica(nome)
        if clinica:
            self.__clinica_dao.remove(nome)
            self.__tela_clinica.mostra_mensagem(f"Clínica '{nome}' excluída.")
            return
        self.__tela_clinica.mostra_mensagem(f"Clínica '{nome}' não encontrada.")
    
    def editar_clinica(self, nome):
        clinica = self.buscar_clinica(nome)
        if not clinica:
            self.__tela_clinica.mostra_mensagem(f"Clínica '{nome}' não encontrada.")
            return

        dados_clinica = self.__tela_clinica.pega_dados_clinica()
        if not dados_clinica:
            return  # Caso o usuário clique em Cancelar na janela

        if not dados_clinica['nome'] or not dados_clinica['nome'].strip():
            self.__tela_clinica.mostra_mensagem("Nome não pode ser vazio.")
            return

        if not dados_clinica['localizacao'] or not dados_clinica['localizacao'].strip():
            self.__tela_clinica.mostra_mensagem("Localização não pode ser vazia.")
            return

        novo_nome = dados_clinica['nome']
        if novo_nome != nome and self.buscar_clinica(novo_nome):
            self.__tela_clinica.mostra_mensagem("Já existe uma clínica com esse novo nome.")
            return

        if novo_nome != nome:
            self.__clinica_dao.remove(nome)

        clinica.nome = novo_nome
        clinica.localizacao = dados_clinica['localizacao']
        clinica.descricao = dados_clinica['descricao']
        clinica.horario_abertura = dados_clinica['horario_abertura']                
        clinica.horario_fechamento = dados_clinica['horario_fechamento']
        
        self.__clinica_dao.add(clinica.nome, clinica)
        
        self.__tela_clinica.mostra_mensagem(f"Clínica '{novo_nome}' editada com sucesso.")
    
    def listar_clinicas(self):
        clinicas = self.__clinica_dao.get_all()
        self.__tela_clinica.mostra_clinicas(clinicas)