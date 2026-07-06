import FreeSimpleGUI as sg
from models.tipo_atendimento import TipoAtendimento

class TelaAtendimento:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3')
        self.__fonte_titulo = ("Segoe UI", 18, "bold")
        self.__fonte_label = ("Segoe UI", 12)
        self.__fonte_botao = ("Segoe UI", 11, "bold")

    def mostra_menu_atendimento(self):
        layout = [
            [sg.VPush()],
            [sg.Text("Gestão de Atendimentos", font=self.__fonte_titulo, text_color="#1a365d", pad=(0, 20))],
            [sg.Button("Agendar Atendimento", key=1, size=(25, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Listar Atendimentos", key=2, size=(25, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Excluir Atendimento", key=3, size=(25, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar ao Menu Principal", key=4, size=(20, 1), font=self.__fonte_label, button_color=("#718096", "#DAE9F5"), border_width=0)],
            [sg.VPush()]
        ]
        
        self.__janela = sg.Window("ControlClin - Atendimentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        
        evento, _ = self.__janela.read()
        self.__janela.close()
        
        return evento if evento is not None else 4

    def pega_nome_clinica(self) -> str:
        layout = [
            [sg.Text("Informe o Nome da Clínica:", font=self.__fonte_label)],
            [sg.Input(key="clinica", size=(30, 1))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="Cancel")]
        ]
        janela = sg.Window("Clínica", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()
        return valores["clinica"] if evento == "OK" else ""

    def pega_cpf_paciente(self) -> str:
        layout = [
            [sg.Text("Informe o CPF do Paciente:", font=self.__fonte_label)],
            [sg.Input(key="cpf", size=(25, 1))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="Cancel")]
        ]
        janela = sg.Window("Paciente", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()
        return valores["cpf"] if evento == "OK" else ""

    def pega_cpf_profissional(self) -> str:
        layout = [
            [sg.Text("Informe o CPF do Profissional:", font=self.__fonte_label)],
            [sg.Input(key="cpf", size=(25, 1))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="Cancel")]
        ]
        janela = sg.Window("Profissional", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()
        return valores["cpf"] if evento == "OK" else ""

    def pega_codigo_atendimento_excluir(self) -> int:
        layout = [
            [sg.Text("Digite o CÓDIGO do atendimento que deseja excluir:", font=self.__fonte_label)],
            [sg.Input(key="codigo", size=(15, 1))],
            [sg.Button("Excluir", key="OK", button_color=("white", "darkred")), sg.Button("Cancelar", key="Cancel")]
        ]
        janela = sg.Window("Excluir Atendimento", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()
        if evento == "OK":
            try:
                return int(valores["codigo"])
            except ValueError:
                pass
        return None

    def pega_tipo_atendimento(self):
        tipos = list(TipoAtendimento)
        layout = [[sg.Text("Selecione o Tipo de Atendimento", font=self.__fonte_titulo, pad=(0, 15))]]
        
        for i, tipo in enumerate(tipos, 1):
            descricao = tipo.value['descricao']
            valor = tipo.value['valor_base']
            layout.append([sg.Button(f"{descricao} (R$ {valor:.2f})", key=i, size=(35, 2), font=self.__fonte_label)])
            
        layout.append([sg.Button("Cancelar", key="Cancel", pad=(0, 15), button_color=("#718096", "#DAE9F5"), border_width=0)])
        
        janela = sg.Window("Tipo de Atendimento", layout, element_justification="center")
        evento, _ = janela.read()
        janela.close()
        
        if isinstance(evento, int) and 1 <= evento <= len(tipos):
            return tipos[evento - 1]
        return None

    def pega_dados_atendimento(self):
        layout = [
            [sg.Text("Informe a Data e Horário", font=self.__fonte_titulo, pad=(0, 15))],
            [sg.Text("Dia:", size=(18, 1)), sg.Input(key="dia", size=(10, 1))],
            [sg.Text("Mês:", size=(18, 1)), sg.Input(key="mes", size=(10, 1))],
            [sg.Text("Ano:", size=(18, 1)), sg.Input(key="ano", size=(10, 1))],
            [sg.Text("Início (HH:MM):", size=(18, 1)), sg.Input(key="h_ini", size=(10, 1))],
            [sg.Text("Fim (HH:MM):", size=(18, 1)), sg.Input(key="h_fim", size=(10, 1))],
            [sg.Text("", pad=(0, 5))],
            [sg.Button("Confirmar", key="OK", size=(12, 1)), sg.Button("Cancelar", key="Cancel")]
        ]
        
        janela = sg.Window("Dados do Agendamento", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()
        
        if evento != "OK":
            return None
            
        return {
            "dia": valores["dia"], "mes": valores["mes"], "ano": valores["ano"],
            "horario_inicio": valores["h_ini"],
            "horario_fim": valores["h_fim"]
        }

    def mostra_atendimentos(self, atendimentos_com_saldo):
        if not atendimentos_com_saldo:
            self.mostra_mensagem("Nenhum atendimento agendado.")
            return

        cabecalhos = ["Código", "Data", "Horário", "Clínica", "Paciente", "Profissional", "Tipo", "Valor Total", "A Pagar"]
        dados_tabela = []

        for a, restante in atendimentos_com_saldo:
            dados_tabela.append([
                str(a.codigo),
                str(a.data),
                f"{a.horario_inicio} - {a.horario_fim}",
                a.clinica.nome if a.clinica else "N/I",
                a.paciente.nome if a.paciente else "N/I",
                a.profissional.nome if a.profissional else "N/I",
                str(a.tipoAtendimento.value['descricao']),
                f"R$ {a.valor:.2f}",
                f"R$ {restante:.2f}"
            ])

        layout = [
            [sg.VPush()],
            [sg.Text("Lista de Atendimentos Agendados", font=self.__fonte_titulo, text_color="#1a365d", pad=(0, 20))],
            [sg.Table(
                values=dados_tabela,
                headings=cabecalhos,
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
                num_rows=15,
                alternating_row_color="#e2e8f0",
                key="-TABELA-",
                row_height=30,
                font=("Segoe UI", 11)
            )],
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar", key="voltar", size=(15, 1), font=self.__fonte_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.VPush()]
        ]

        self.__janela = sg.Window("ControlClin - Lista de Atendimentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        self.__janela.read()
        self.__janela.close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup("Aviso", mensagem, font=self.__fonte_label, title="ControlClin")