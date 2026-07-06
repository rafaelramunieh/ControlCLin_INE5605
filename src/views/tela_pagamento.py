import FreeSimpleGUI as sg
from models.pagamentoCartaoCredito import PagamentoCartaoCredito
from models.pagamentoDinheiro import PagamentoDinheiro
from models.pagamentoPix import PagamentoPix

class TelaPagamento:
    def __init__(self):
        self.__janela = None
        sg.theme('LightBlue3')
        self.__fonte_titulo = ("Segoe UI", 18, "bold")
        self.__fonte_label = ("Segoe UI", 12)
        self.__fonte_botao = ("Segoe UI", 11, "bold")

    def mostra_menu_pagamento(self):
        layout = [
            [sg.VPush()],
            [sg.Text("Gestão de Pagamentos", font=self.__fonte_titulo, text_color="#1a365d", pad=(0, 20))],
            [sg.Button("Registrar Novo Pagamento", key=1, size=(30, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Button("Listar Todos os Pagamentos", key=2, size=(30, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2b6cb0"))],
            [sg.Text("", pad=(0, 10))],
            [sg.Button("Voltar ao Menu Principal", key=3, size=(20, 1), font=self.__fonte_label, button_color=("#718096", "#DAE9F5"), border_width=0)],
            [sg.VPush()]
        ]
        
        self.__janela = sg.Window("ControlClin - Pagamentos", layout, element_justification="center", finalize=True)
        self.__janela.maximize()
        
        evento, _ = self.__janela.read()
        self.__janela.close()
        
        return evento if evento is not None else 3

    def get_tipo_pagamento(self):
        layout = [
            [sg.VPush()],
            [sg.Text("Selecione a Forma de Pagamento", font=self.__fonte_titulo, text_color="#1a365d", pad=(0, 20))],
            [sg.Button("Dinheiro", key=1, size=(20, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2f855a"))],
            [sg.Button("Pix", key=2, size=(20, 2), font=self.__fonte_botao, button_color=("#ffffff", "#2c5282"))],
            [sg.Button("Cartão de Crédito", key=3, size=(20, 2), font=self.__fonte_botao, button_color=("#ffffff", "#744210"))],
            [sg.Button("Cancelar", key=0, size=(10, 1), pad=(0, 20), button_color=("#718096", "#DAE9F5"), border_width=0)],
            [sg.VPush()]
        ]
        
        janela = sg.Window("Forma de Pagamento", layout, element_justification="center", finalize=True)
        janela.maximize()
        evento, _ = janela.read()
        janela.close()
        return evento

    def get_dados_pagamento(self, tipo_pagamento):
        # Campos comuns
        layout = [
            [sg.Text("Dados do Pagamento", font=self.__fonte_titulo, pad=(0, 20))],
            [sg.Text("Data (DD/MM/AAAA):", size=(18, 1)), sg.Input(key="data", size=(20, 1))],
            [sg.Text("Valor Pago: R$", size=(18, 1)), sg.Input(key="valor", size=(20, 1))],
        ]

        # Campos específicos
        if tipo_pagamento == 2: # Pix
            layout.append([sg.Text("CPF do Pagador:", size=(18, 1)), sg.Input(key="cpf", size=(20, 1))])
        elif tipo_pagamento == 3: # Cartão
            layout.append([sg.Text("Número do Cartão:", size=(18, 1)), sg.Input(key="numero", size=(20, 1))])
            layout.append([sg.Text("Bandeira:", size=(18, 1)), sg.Input(key="bandeira", size=(20, 1))])

        layout.append([sg.Button("Confirmar", key="OK", pad=(0, 20), size=(15, 1)), sg.Button("Cancelar", key="Cancel")])

        janela = sg.Window("Registrar Dados", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()

        if evento != "OK":
            return None

        # Monta o dicionário de retorno
        dados = {"data": valores["data"], "valor_pago": float(valores["valor"])}
        if tipo_pagamento == 2:
            dados['cpf_pagador'] = valores["cpf"]
        elif tipo_pagamento == 3:
            dados["numero_cartao"] = valores["numero"]
            dados["bandeira_cartao"] = valores["bandeira"]
        
        return dados

    def mostra_atendimentos(self, atendimentos_com_saldo):
        if not atendimentos_com_saldo:
            self.mostra_mensagem("Não há nenhum atendimento cadastrado.")
            return

        listagem = "---------- ATENDIMENTOS DISPONÍVEIS ----------\n\n"
        
        for i, (a, restante) in enumerate(atendimentos_com_saldo):
            listagem += f"[{i}] Paciente: {a.paciente.nome} | Restante: R$ {restante:.2f}\n"
            listagem += f"    Serviço: {a.tipoAtendimento.value['descricao']} | Data: {a.data}\n"
            listagem += "-" * 60 + "\n"
        
        sg.popup_scrolled(listagem, title="Atendimentos Disponíveis", size=(80, 20), font=("Courier New", 10))

    def get_indice_atendimento(self, total):
        layout = [
            [sg.Text("Informe o número [índice] do atendimento selecionado:", font=self.__fonte_label)],
            [sg.Input(key="indice", size=(10, 1))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="Cancel")]
        ]
        janela = sg.Window("Selecionar Atendimento", layout, element_justification="center")
        evento, valores = janela.read()
        janela.close()

        if evento == "OK":
            try:
                indice = int(valores["indice"])
                if 0 <= indice < total:
                    return indice
            except ValueError:
                pass
        
        self.mostra_mensagem("Índice inválido ou operação cancelada.")
        return None

    def mostra_pagamentos(self, pagamentos):
        if not pagamentos:
            self.mostra_mensagem("Não há nenhum pagamento registrado.")
            return

        listagem = "---------- LISTA DE PAGAMENTOS ----------\n\n"
        for p in pagamentos:
            listagem += f"Data: {p.data} | Paciente: {p.paciente.nome}\n"
            listagem += f"VALOR: R$ {p.valor_pago:.2f} | "
            
            if isinstance(p, PagamentoCartaoCredito):
                listagem += f"CARTÃO ({p.bandeira_cartao})\n"
            elif isinstance(p, PagamentoPix):
                listagem += f"PIX (Pagador: {p.cpf_pagador})\n"
            else:
                listagem += "DINHEIRO\n"
            listagem += "-" * 50 + "\n"

        sg.popup_scrolled(listagem, title="Pagamentos Registrados", size=(80, 20), font=("Courier New", 10))

    def mostra_mensagem(self, mensagem: str):
        sg.popup("Aviso", mensagem, font=self.__fonte_label, title="ControlClin")