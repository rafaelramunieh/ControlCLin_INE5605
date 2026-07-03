from models.pagamento import Pagamento
from models.pagamentoCartaoCredito import PagamentoCartaoCredito
from models.pagamentoDinheiro import PagamentoDinheiro
from models.pagamentoPix import PagamentoPix
from views.tela_pagamento import TelaPagamento
from models.dao.pagamento_dao import PagamentoDAO


class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pagamento_dao = PagamentoDAO()
        self.__tela_pagamento = TelaPagamento()

    @property
    def pagamentos(self):
        return self.__pagamento_dao.get_all()

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
                self.__tela_pagamento.mostra_mensagem("Opção inválida. Tente novamente.")

    def incluir_pagamento(self):
        controlador_atendimento = self.__controlador_sistema.controlador_atendimento
        atendimentos = controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        self.__tela_pagamento.mostra_atendimentos(atendimentos)
        indice = self.__tela_pagamento.get_indice_atendimento(len(atendimentos))
        if indice is None:
            return
        atendimento = atendimentos[indice]

        paciente = atendimento.paciente

        valor_restante = atendimento.calcula_restante()
        if valor_restante <= 0:
            self.__tela_pagamento.mostra_mensagem("Este atendimento já está totalmente pago.")
            return

        self.__tela_pagamento.mostra_mensagem(f"Valor total do atendimento: R$ {atendimento.valor:.2f}")
        self.__tela_pagamento.mostra_mensagem(f"Valor restante a pagar: R$ {valor_restante:.2f}")

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
            pagamento = PagamentoCartaoCredito(
                dados['data'],
                atendimento,
                paciente,
                dados['valor_pago'],
                dados['numero_cartao'],
                dados['bandeira_cartao']
            )

        if pagamento:
            chave = id(pagamento) # Gera uma chave única temporária para o exemplo
            self.__pagamento_dao.add(chave, pagamento)
            
            atendimento.adicionar_pagamento(pagamento)
            self.__tela_pagamento.mostra_mensagem("Pagamento registrado com sucesso!")
            
            restante = atendimento.calcula_restante()
            if restante > 0:
                self.__tela_pagamento.mostra_mensagem(f"Ainda resta R$ {restante:.2f} a pagar neste atendimento.")
            else:
                self.__tela_pagamento.mostra_mensagem("Atendimento totalmente quitado.")

    def buscar_pagamentos_por_atendimento(self, atendimento):
        return [p for p in self.__pagamento_dao.get_all() if p.atendimento == atendimento]

    def listar_pagamentos(self):
        self.__tela_pagamento.mostra_pagamentos(self.__pagamento_dao.get_all())