from models.pagamento import Pagamento
from models.pagamentoCartaoCredito import pagamentoCartaoCredito
from models.pagamentoDinheiro import PagamentoDinheiro
from models.pagamentoPix import PagamentoPix
from views.tela_pagamento import TelaPagamento


class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pagamentos = []
        self.__tela_pagamento = TelaPagamento()

    @property
    def pagamentos(self):
        return self.__pagamentos

    def abrir_menu(self):
        while True:
            opcao = self.__tela_pagamento.mostra_menu_pagamento()
            if opcao == 1:
                self.incluir_pagamento()
            elif opcao == 2:
                self.listar_pagamentos()
            elif opcao == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")

    def incluir_pagamento(self):
        # Busca o atendimento pelo sistema
        controlador_atendimento = self.__controlador_sistema.controlador_atendimento
        atendimentos = controlador_atendimento.atendimentos
        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        self.__tela_pagamento.mostra_atendimentos(atendimentos)
        indice = self.__tela_pagamento.get_indice_atendimento(len(atendimentos))
        if indice is None:
            return
        atendimento = atendimentos[indice]

        # Paciente já está no atendimento
        paciente = atendimento.paciente

        valor_restante = atendimento.calcula_restante()
        if valor_restante <= 0:
            print("Este atendimento já está totalmente pago.")
            return

        print(f"Valor total do atendimento: R$ {atendimento.valor:.2f}")
        print(f"Valor restante a pagar: R$ {valor_restante:.2f}")

        tipo_pagamento = self.__tela_pagamento.get_tipo_pagamento()
        dados = self.__tela_pagamento.get_dados_pagamento(tipo_pagamento)

        pagamento = None

        if tipo_pagamento == 1:  # Dinheiro
            pagamento = PagamentoDinheiro(
                dados['data'],
                atendimento,
                paciente,
                dados['valor_pago']
            )

        elif tipo_pagamento == 2:  # Pix
            pagamento = PagamentoPix(
                dados['data'],
                atendimento,
                paciente,
                dados['valor_pago'],
                dados['cpf_pagador']
            )

        elif tipo_pagamento == 3:  # Cartão de Crédito
            pagamento = pagamentoCartaoCredito(
                dados['data'],
                atendimento,
                paciente,
                dados['valor_pago'],
                dados['numero_cartao'],
                dados['bandeira_cartao']
            )

        if pagamento:
            self.__pagamentos.append(pagamento)
            atendimento.adicionar_pagamento(pagamento)
            print("Pagamento registrado com sucesso!")
            restante = atendimento.calcula_restante()
            if restante > 0:
                print(f"Ainda resta R$ {restante:.2f} a pagar neste atendimento.")
            else:
                print("Atendimento totalmente quitado.")

    def buscar_pagamentos_por_atendimento(self, atendimento):
        return [p for p in self.__pagamentos if p.atendimento == atendimento]

    def listar_pagamentos(self):
        self.__tela_pagamento.mostra_pagamentos(self.__pagamentos)