import FreeSimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__janela = None
        # Define o tema antes de qualquer coisa para aplicar globalmente
        sg.theme('LightBlue3') 

    def mostra_menu_principal(self):
        font_titulo = ("Segoe UI", 18, "bold") # Aumentei um pouco as fontes para a tela cheia
        font_sub = ("Segoe UI", 12)
        font_botao = ("Segoe UI", 11, "bold")
        
        layout = [
            [sg.VPush()], # Mola invisível que empurra o conteúdo para baixo (centraliza verticalmente)
            
            [sg.Text("ControlClin", font=font_titulo, pad=(0, 10), text_color="#1a365d")],
            [sg.Text("Gerenciamento de Clínicas e Atendimentos", font=font_sub, pad=(0, 20), text_color="#4a5568")],
            
            [
                sg.Button("Clínicas", key=1, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0")), 
                sg.Button("Profissionais", key=2, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))
            ],
            [
                sg.Button("Pacientes", key=3, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0")), 
                sg.Button("Atendimentos", key=4, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))
            ],
            [
                sg.Button("Procedimentos", key=5, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0")), 
                sg.Button("Pagamentos", key=6, size=(25, 2), font=font_botao, button_color=("#ffffff", "#2b6cb0"))
            ],
            
            [sg.Text("", pad=(0, 10))],
            
            [sg.Button("Relatórios e Dashboards", key=7, size=(53, 2), font=font_botao, button_color=("#ffffff", "#2c5282"))],
            
            [sg.Button("Sair do Sistema", key=0, size=(15, 1), font=font_sub, button_color=("#718096", "#F0F0F0"), border_width=0, pad=(0, 20))],
            
            [sg.VPush()] # Mola invisível que empurra o conteúdo para cima
        ]

        # Criamos a janela adicionando o finalize=True para permitir comandos logo em seguida
        self.__janela = sg.Window(
            "ControlClin - Menu", 
            layout, 
            element_justification="center",
            finalize=True
        )
        
        # ESSA É A MÁGICA: Maximiza a janela assim que ela abre
        self.__janela.maximize()
        
        botao_clicado, _ = self.__janela.read()
        self.__janela.close()

        if botao_clicado is None:
            return 0
            
        return botao_clicado

    def mostra_mensagem_saida(self):
        sg.popup_ok("Até logo!", title="Saída", font=("Segoe UI", 10))

    def mostra_opcao_invalida(self):
        sg.popup_error("Opção inválida. Tente novamente.", title="Erro", font=("Segoe UI", 10))