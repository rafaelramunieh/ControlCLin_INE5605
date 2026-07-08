import FreeSimpleGUI as sg

class TelaProcedimento:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3')

    def mostra_menu_procedimento(self):
        font_titulo = ("Segoe UI", 18, "bold")
        font_botao = ("Segoe UI", 11, "bold")
        font_sub = ("Segoe UI", 12)
        
        layout = [
            [sg.VPush()],
            
            [sg.Text("Gestão de Procedimentos", font=font_titulo, pad=(0, 10), text_color="#1a365d")],
            [sg.Text("Selecione a ação desejada para gerenciar os procedimentos", font=font_sub, pad=(0, 20), text_color="#4a5568")],
            
            [sg.Button("Adicionar um procedimento a um atendimento", key=1, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Listar todos os procedimentos", key=2, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            
            [sg.Text("", pad=(0, 10))],
            
            [sg.Button("Voltar ao menu principal", key=3, size=(20, 1), font=font_sub, button_color=("#718096", "#F0F0F0"), border_width=0, pad=(0, 20))],
            
            [sg.VPush()]
        ]

        self.__janela = sg.Window(
            "ControlClin - Menu Procedimentos", 
            layout, 
            element_justification="center",
            finalize=True
        )
        
        self.__janela.maximize()
        
        botao_clicado, _ = self.__janela.read()
        self.__janela.close()

        if botao_clicado is None:
            return 3
            
        return botao_clicado

    def pega_dados_procedimento(self):
        font_titulo = ("Segoe UI", 16, "bold")
        font_label = ("Segoe UI", 12)
        font_botao = ("Segoe UI", 11, "bold")

        layout = [
            [sg.VPush()],
            [sg.Text("Novo Procedimento", font=font_titulo, pad=(0, 15), text_color="#1a365d")],
            
            [sg.Text("Descrição do procedimento:", font=font_label, size=(22, 1)), sg.Input(key="descricao", size=(30, 1))],
            [sg.Text("Custo do procedimento (R$):", font=font_label, size=(22, 1)), sg.Input(key="custo", size=(15, 1))],
            
            [sg.Text("", pad=(0, 10))],
            [
                sg.Button("Confirmar", key="OK", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282")),
                sg.Button("Cancelar", key="Cancel", size=(15, 1), font=font_botao, button_color=("#718096", "#F0F0F0"), border_width=0)
            ],
            [sg.VPush()]
        ]

        janela = sg.Window("Dados do Procedimento", layout, element_justification="center", finalize=True)
        janela.maximize()
        
        evento, valores = janela.read()
        janela.close()
        
        if evento != "OK":
            return None
            
        try:
            custo_float = float(valores["custo"])
            return {"descricao": valores["descricao"], "custo": custo_float}
        except ValueError:
            self.mostra_mensagem("[Erro] Custo Inválido.")
            return None

    def mostra_atendimentos(self, atendimentos):
        font_titulo = ("Segoe UI", 16, "bold")
        font_botao = ("Segoe UI", 11, "bold")

        cabecalhos = ["Índice", "Paciente", "Tipo de Atendimento", "Data"]
        dados_tabela = []
        for i, a in enumerate(atendimentos, 1):
            dados_tabela.append([
                str(i),
                str(a.paciente.nome),
                str(a.tipoAtendimento.value['descricao'] if hasattr(a.tipoAtendimento, 'value') else a.tipoAtendimento.descricao),
                str(a.data)
            ])

        layout = [
            [sg.VPush()],
            [sg.Text("Selecione o Atendimento Desejado", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
            [sg.Table(
                values=dados_tabela,
                headings=cabecalhos,
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
                num_rows=10,
                alternating_row_color="#e2e8f0",
                key="-TABELA-",
                row_height=30,
                font=("Segoe UI", 11),
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],
            
            [sg.Text("Digite o número do índice do atendimento escolhido:", font=("Segoe UI", 11), pad=(0, 10))],
            [sg.Input(key="indice_escolhido", size=(10, 1))],
            
            [sg.Text("", pad=(0, 10))],
            [
                sg.Button("Selecionar", key="OK", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282")),
                sg.Button("Cancelar", key="Cancel", size=(15, 1), font=font_botao, button_color=("#718096", "#F0F0F0"), border_width=0)
            ],
            [sg.VPush()]
        ]

        janela = sg.Window("Atendimentos Disponíveis", layout, element_justification="center", finalize=True)
        janela.maximize()
        
        evento, valores = janela.read()
        janela.close()
        
        if evento == "OK":
            try:
                return int(valores["indice_escolhido"])
            except ValueError:
                return -1
        return -1

    def mostra_procedimentos(self, procedimentos):
        font_titulo = ("Segoe UI", 16, "bold")
        font_botao = ("Segoe UI", 11, "bold")

        cabecalhos = ["Paciente", "Data Atendimento", "Procedimento realizado", "Custo", "Profissional"]
        dados_tabela = []
        
        if procedimentos:
            for atendimento, proc in procedimentos:
                dados_tabela.append([
                    str(atendimento.paciente.nome),
                    str(atendimento.data),
                    str(proc.descricao),
                    f"R$ {proc.custo:.2f}",
                    str(proc.profissional.nome)
                ])

        layout = [
            [sg.VPush()],
            [sg.Text("Lista de Procedimentos Registrados", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
            [sg.Table(
                values=dados_tabela,
                headings=cabecalhos,
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
                num_rows=12,
                alternating_row_color="#e2e8f0",
                key="-TABELA-",
                row_height=30,
                font=("Segoe UI", 11)
            )],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("Procedimentos do Sistema", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem, title="Aviso", font=("Segoe UI", 11), button_color=("#ffffff", "#2c5282"))