import FreeSimpleGUI as sg

class TelaPaciente:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3')

    def mostra_menu_paciente(self):
        font_titulo = ("Segoe UI", 18, "bold")
        font_sub = ("Segoe UI", 12)
        font_botao = ("Segoe UI", 11, "bold")
        
        layout = [
            [sg.VPush()],
            [sg.Text("Gerenciamento de Pacientes", font=font_titulo, pad=(0, 10), text_color="#1a365d")],
            [sg.Text("Escolha uma das opções abaixo:", font=font_sub, pad=(0, 20), text_color="#4a5568")],
            
            [sg.Button("Incluir Paciente", key=1, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Listar Pacientes", key=2, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Excluir Paciente", key=3, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Editar Paciente", key=4, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar ao Menu Principal", key=5, size=(25, 2), font=font_sub, button_color=("#718096", "#F0F0F0"), border_width=0, pad=(0, 20))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("ControlClin - Pacientes", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        
        botao_clicado, _ = self.__janela.read()
        self.__janela.close()

        if botao_clicado is None:
            return 5  # Retorna a opção de voltar caso feche a janela
        return botao_clicado

    def pega_dados_paciente(self):
        font_sub = ("Segoe UI", 11)
        layout = [
            [sg.Text("Nome:", size=(8, 1), font=font_sub), sg.InputText(key="nome")],
            [sg.Text("Celular:", size=(8, 1), font=font_sub), sg.InputText(key="celular")],
            [sg.Text("CPF:", size=(8, 1), font=font_sub), sg.InputText(key="cpf")],
            [sg.Text("Idade:", size=(8, 1), font=font_sub), sg.InputText(key="idade")],
            [sg.Button("Confirmar", key=1), sg.Button("Cancelar", key=0)]
        ]
        
        janela = sg.Window("Dados do Paciente", layout, font=("Segoe UI", 10), modal=True)
        botao, valores = janela.read()
        janela.close()
        
        if botao == 1:
            try:
                celular = int(valores["celular"])
            except ValueError:
                celular = 0
            try:
                idade = int(valores["idade"])
            except ValueError:
                idade = 0
                
            return {"nome": valores["nome"], "celular": celular, "cpf": valores["cpf"], "idade": idade}
        return None

    def mostra_pacientes(self, pacientes):
        if not pacientes:
            sg.popup_ok("Nenhum paciente cadastrado.", title="Pacientes", font=("Segoe UI", 10))
            return
            
        dados_tabela = []
        for p in pacientes:
            dados_tabela.append([p.nome, p.celular, p.cpf, p.idade])
            
        layout = [
            [sg.Text("Lista de Pacientes", font=("Segoe UI", 14, "bold"), text_color="#1a365d")],
            [sg.Table(values=dados_tabela, headings=["Nome", "Celular", "CPF", "Idade"], 
                      auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', num_rows=10)],
            [sg.Button("Fechar", size=(10, 1))]
        ]
        janela = sg.Window("Pacientes Cadastrados", layout, element_justification="center", modal=True)
        janela.read()
        janela.close()
    
    def pega_cpf(self, acao):
        cpf = sg.popup_get_text(f"Digite o CPF do paciente a ser {acao}:", title="Buscar CPF", font=("Segoe UI", 10))
        return cpf if cpf else ""

    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem, title="Aviso", font=("Segoe UI", 10))

    def mostra_opcao_invalida(self):
        sg.popup_error("Opção inválida. Tente novamente.", title="Erro", font=("Segoe UI", 10))