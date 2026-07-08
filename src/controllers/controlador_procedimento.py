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
        
        # Agora a tela abre de forma gráfica para escolher o índice
        indice_usuario = self.__tela_procedimento.mostra_atendimentos(atendimentos)
        if indice_usuario == -1:
            return
            
        indice = indice_usuario - 1
        if not (0 <= indice < len(atendimentos)):
            self.__tela_procedimento.mostra_mensagem(f"[Erro] Número inválido")
            return
        atendimento = atendimentos[indice]

        profissionais = self.__controlador_sistema.controlador_profissional.profissionais
        if not profissionais:
            self.__tela_procedimento.mostra_mensagem(f"Nenhum profissional encontrado.")
            return
        
        # Criamos uma janela rápida para selecionar o profissional graficamente pelo índice
        import FreeSimpleGUI as sg
        cabecalhos = ["Índice", "Nome", "Especialidade"]
        dados_prof = [[str(i), p.nome, p.especialidade] for i, p in enumerate(profissionais, 1)]
        
        layout_prof = [
            [sg.Text("Selecione o Profissional Responsável", font=("Segoe UI", 14, "bold"), text_color="#1a365d")],
            [sg.Table(values=dados_prof, headings=cabecalhos, auto_size_columns=True, justification="center", num_rows=6, font=("Segoe UI", 11))],
            [sg.Text("Digite o número do índice do profissional escolhido:"), sg.Input(key="idx", size=(10, 1))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="Cancel")]
        ]
        
        janela_prof = sg.Window("Selecionar Profissional", layout_prof, element_justification="center")
        evento, valores = janela_prof.read()
        janela_prof.close()
        
        if evento != "OK":
            return
            
        try:
            indice_prof = int(valores["idx"]) - 1
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