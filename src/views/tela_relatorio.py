import FreeSimpleGUI as sg

class TelaRelatorio:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3') 

    def shows_menu_relatorio(self):
        pass

    def mostra_menu_relatorio(self):
        font_titulo = ("Segoe UI", 18, "bold")
        font_botao = ("Segoe UI", 11, "bold")
        font_sub = ("Segoe UI", 12)
        
        layout = [
            [sg.VPush()],
            
            [sg.Text("Relatórios e Dashboards", font=font_titulo, pad=(0, 10), text_color="#1a365d")],
            [sg.Text("Selecione um relatório para visualizar as estatísticas", font=font_sub, pad=(0, 20), text_color="#4a5568")],
            
            [sg.Button("Clínicas com maior número de atendimentos", key=1, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Atendimentos mais caros e mais baratos", key=2, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Procedimentos mais realizados", key=3, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Procedimentos mais caros e mais baratos", key=4, size=(45, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            
            [sg.Text("", pad=(0, 10))],
            
            [sg.Button("Voltar ao menu principal", key=5, size=(20, 1), font=font_sub, button_color=("#718096", "#F0F0F0"), border_width=0, pad=(0, 20))],
            
            [sg.VPush()]
        ]

        self.__janela = sg.Window(
            "ControlClin - Menu Relatórios", 
            layout, 
            element_justification="center",
            finalize=True
        )
        
        self.__janela.maximize()
        
        botao_clicado, _ = self.__janela.read()
        self.__janela.close()

        if botao_clicado is None:
            return 5
            
        return botao_clicado

    def mostra_ranking_clinicas(self, ranking):
        font_titulo = ("Segoe UI", 16, "bold")
        font_botao = ("Segoe UI", 11, "bold")

        cabecalhos = ["Posição", "Nome da Clínica", "Quantidade de Atendimentos"]
        dados_tabela = []
        for i, (nome, total) in enumerate(ranking):
            dados_tabela.append([f"{i+1}º", str(nome), f"{total} atendimento(s)"])

        layout = [
            [sg.VPush()],
            [sg.Text("Clínicas por Nº de Atendimentos", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
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
                font=("Segoe UI", 11)
            )],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("Ranking de Clínicas", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_atendimentos_extremos(self, mais_caro, mais_barato):
        font_titulo = ("Segoe UI", 16, "bold")
        font_label = ("Segoe UI", 11, "bold")
        font_valor = ("Segoe UI", 11)
        font_botao = ("Segoe UI", 11, "bold")

        desc_caro = mais_caro.tipoAtendimento.value['descricao']
        desc_barato = mais_barato.tipoAtendimento.value['descricao']

        layout_caro = [
            [sg.Text("Paciente:", font=font_label, text_color="#2c5282"), sg.Text(mais_caro.paciente.nome, font=font_valor)],
            [sg.Text("Tipo:", font=font_label, text_color="#2c5282"), sg.Text(desc_caro, font=font_valor)],
            [sg.Text("Valor do Atendimento:", font=font_label, text_color="#2c5282"), sg.Text(f"R$ {mais_caro.valor:.2f}", font=("Segoe UI", 12, "bold"), text_color="#2f855a")]
        ]

        layout_barato = [
            [sg.Text("Paciente:", font=font_label, text_color="#2c5282"), sg.Text(mais_barato.paciente.nome, font=font_valor)],
            [sg.Text("Tipo:", font=font_label, text_color="#2c5282"), sg.Text(desc_barato, font=font_valor)],
            [sg.Text("Valor do Atendimento:", font=font_label, text_color="#2c5282"), sg.Text(f"R$ {mais_barato.valor:.2f}", font=("Segoe UI", 12, "bold"), text_color="#2b6cb0")]
        ]

        layout = [
            [sg.VPush()],
            [sg.Text("Extremos de Atendimentos Registrados", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
            [sg.Frame(" ATENDIMENTO MAIS CARO ", layout_caro, font=("Segoe UI", 11, "bold"), title_color="#2f855a", pad=(0, 15), element_justification="left")],
            [sg.Frame(" ATENDIMENTO MAIS BARATO ", layout_barato, font=("Segoe UI", 11, "bold"), title_color="#2b6cb0", pad=(0, 15), element_justification="left")],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("Análise de Atendimentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_ranking_procedimentos(self, ranking):
        font_titulo = ("Segoe UI", 16, "bold")
        font_conteudo = ("Segoe UI", 12)
        font_botao = ("Segoe UI", 11, "bold")

        texto_ranking = ""
        for i, (descricao, total) in enumerate(ranking):
            texto_ranking += f"  {i+1}º  {descricao}: realizou {total} vez(es)\n\n"

        layout = [
            [sg.VPush()],
            [sg.Text("Procedimentos Mais Realizados no Sistema", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
            [sg.Multiline(texto_ranking, size=(60, 12), disabled=True, font=font_conteudo, background_color="#ffffff", text_color="#2d3748", border_width=1)],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("Ranking de Procedimentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_procedimentos_extremos(self, mais_caro, mais_barato):
        font_titulo = ("Segoe UI", 16, "bold")
        font_label = ("Segoe UI", 11, "bold")
        font_valor = ("Segoe UI", 11)
        font_botao = ("Segoe UI", 11, "bold")

        layout_caro = [
            [sg.Text("Descrição:", font=font_label, text_color="#2c5282"), sg.Text(mais_caro.descricao, font=font_valor)],
            [sg.Text("Custo de Operação:", font=font_label, text_color="#2c5282"), sg.Text(f"R$ {mais_caro.custo:.2f}", font=("Segoe UI", 12, "bold"), text_color="#2f855a")]
        ]

        layout_barato = [
            [sg.Text("Descrição:", font=font_label, text_color="#2c5282"), sg.Text(mais_barato.descricao, font=font_valor)],
            [sg.Text("Custo de Operação:", font=font_label, text_color="#2c5282"), sg.Text(f"R$ {mais_barato.custo:.2f}", font=("Segoe UI", 12, "bold"), text_color="#2b6cb0")]
        ]

        layout = [
            [sg.VPush()],
            [sg.Text("Extremos de Custo de Procedimentos", font=font_titulo, pad=(0, 20), text_color="#1a365d")],
            
            [sg.Frame(" PROCEDIMENTO MAIS CARO ", layout_caro, font=("Segoe UI", 11, "bold"), title_color="#2f855a", pad=(0, 15), element_justification="left")],
            [sg.Frame(" PROCEDIMENTO MAIS BARATO ", layout_barato, font=("Segoe UI", 11, "bold"), title_color="#2b6cb0", pad=(0, 15), element_justification="left")],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("Análise de Procedimentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup_ok(mensagem, title="Aviso", font=("Segoe UI", 11), button_color=("#ffffff", "#2c5282"))