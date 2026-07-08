from models.procedimento import Procedimento
from views.tela_procedimento import TelaProcedimento 

class ControladorProcedimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_procedimento = TelaProcedimento()
    
    def abrir_menu(self):
        while True:
            opcao = self.__tela_procedimento.mostra_menu_procedimento()
            if opcao == 1:
                self.incluir_procedimento()
            elif opcao == 2:
                self.listar_procedimentos()
            elif opcao == 3:
                break
            else:
                self.__tela_procedimento.mostra_mensagem(f"[Erro] Opção Inválida. Tente novamente.")
    
    def incluir_procedimento(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela_procedimento.mostra_mensagem(f"Nenhum atendimento cadastrado")
            return
        
        self.__tela_procedimento.mostra_atendimentos(atendimentos)
        try:
            indice = int(input("Selecione o número de atendimento")) - 1
        except ValueError:
            self.__tela_procedimento.mostra_mensagem(f"[Erro] Entrada inválida.")
            return
        
        if not (0 <= indice < len(atendimentos)):
            self.__tela_procedimento.mostra_mensagem(f"[Erro] Número inválido")
            return
        atendimento = atendimentos[indice]

        profissionais = self.__controlador_sistema.controlador_profissional.profissionais
        if not profissionais:
            self.__tela_procedimento.mostra_mensagem(f"Nenhumm profissional encontrado.")
            return
        
        self.__controlador_sistema.controlador_profissional.listar_profissionais()
        try:
            indice_prof = int(input("Selecione o número do profissional responsável pelo procedimento: ")) - 1
        except ValueError:
            self.__tela_procedimento.mostra_mensagem(f"[Erro] Entrada inválida")
            return
        
        if not (0 <= indice_prof < len(profissionais)):
            self.__tela_procedimento.mostra_mensagem(f"[Erro] Número inválido")
            return
        profissional = profissionais[indice_prof]

        dados = self.__tela_procedimento.pega_dados_procedimento()

        if dados is None:
            return
        
        procedimento = Procedimento(dados["descricao"], dados["custo"], profissional)
        atendimento.adicionar_procedimento(procedimento)
        self.__tela_procedimento.mostra_mensagem(f"Procedimento cadastrado com sucesso!")
        self.__tela_procedimento.mostra_mensagem(f"Novo valor do atendimento: R$ {atendimento.valor:.2f}")


    def listar_procedimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        todos = []
        for a in atendimentos:
            for p in a.procedimentos:
                todos.append((a, p))
        self.__tela_procedimento.mostra_procedimentos(todos)



