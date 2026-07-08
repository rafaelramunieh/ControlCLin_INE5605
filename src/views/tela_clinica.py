import FreeSimpleGUI as sg

class TelaClinica:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3')
    
    def mostra_menu_clinica(self):
        font_titulo = ("Segoe UI", 18, "bold")
        font_sub = ("Segoe UI", 12)
        font_botao = ("Segoe UI", 11, "bold")
        
        layout = [
            [sg.VPush()],
            [sg.Text("Gerenciamento de Clínicas", font=font_titulo, pad=(0, 10), text_color="#1a365d")],
            [sg.Text("Escolha uma das opções abaixo:", font=font_sub, pad=(0, 20), text_color="#4a5568")],
            
            [sg.Button("Incluir Clínica", key=1, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Listar Clínicas", key=2, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Excluir Clínica", key=3, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Editar Clínica", key=4, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))],
            
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar ao Menu Principal", key=5, size=(25, 2), font=font_sub, button_color=("#718096", "#F0F0F0"), border_width=0, pad=(0, 20))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("ControlClin - Clínicas", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        
        botao_clicado, _ = self.__janela.read()
        self.__janela.close()

        if botao_clicado is None:
            return 5
        return botao_clicado
        
    def pega_dados_clinica(self):
        font_sub = ("Segoe UI", 11)
        layout = [
            [sg.Text("Nome:", size=(22, 1), font=font_sub), sg.InputText(key="nome")],
            [sg.Text("Localização:", size=(22, 1), font=font_sub), sg.InputText(key="localizacao")],
            [sg.Text("Descrição:", size=(22, 1), font=font_sub), sg.InputText(key="descricao")],
            [sg.Text("Horário de Abertura:", size=(22, 1), font=font_sub), sg.InputText(key="horario_abertura")],
            [sg.Text("Horário de Fechamento:", size=(22, 1), font=font_sub), sg.InputText(key="horario_fechamento")],
            [sg.Button("Confirmar", key=1), sg.Button("Cancelar", key=0)]
        ]
        
        janela = sg.Window("Dados da Clínica", layout, font=("Segoe UI", 10), modal=True)
        botao, valores = janela.read()
        janela.close()
        
        if botao == 1:
            return {
                "nome": valores["nome"], 
                "localizacao": valores["localizacao"], 
                "descricao": valores["descricao"], 
                "horario_abertura": valores["horario_abertura"], 
                "horario_fechamento": valores["horario_fechamento"]
            }
        return None
    
    def mostra_clinicas(self, clinicas):
        if not clinicas:
            sg.popup_ok("Nenhuma clínica cadastrada.", title="Clínicas", font=("Segoe UI", 10))
            return
            
        dados_tabela = []
        for c in clinicas:
            dados_tabela.append([c.nome, c.localizacao, c.descricao, c.horario_abertura, c.horario_fechamento])
            
        layout = [
            [sg.Text("Lista de Clínicas", font=("Segoe UI", 14, "bold"), text_color="#1a365d")],
            [sg.Table(values=dados_tabela, headings=["Nome", "Localização", "Descrição", "Abertura", "Fechamento"], 
                      auto_size_columns=True, display_row_numbers=False, justification='center', key='-TABLE-', num_rows=10)],
            [sg.Button("Fechar", size=(10, 1))]
        ]
        janela = sg.Window("Clínicas Cadastradas", layout, element_justification="center", modal=True)
        janela.read()
        janela.close()
    
    def pega_nome_clinica(self, acao): 
        nome = sg.popup_get_text(f"Digite o nome da clínica a ser {acao}:", title="Buscar Clínica", font=("Segoe UI", 10))
        return nome if nome else ""
    
    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem, title="Aviso", font=("Segoe UI", 10))
    
    def mostra_opcao_invalida(self):
        sg.popup_error("Opção inválida. Tente novamente.", title="Erro", font=("Segoe UI", 10))