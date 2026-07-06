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
    def pagamento_dao(self):
        # Propriedade necessária para que o ControladorAtendimento acesse o DAO
        return self.__pagamento_dao

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
            elif opcao == 3 or opcao == 0:  # Trata o botão de fechar/voltar
                break
            else:
                self.__tela_pagamento.mostra_mensagem("Opção inválida. Tente novamente.")

    def incluir_pagamento(self):
        controlador_atendimento = self.__controlador_sistema.controlador_atendimento
        atendimentos = controlador_atendimento.atendimento_dao.get_all() # Busca direto do DAO de atendimentos
        
        if not atendimentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        # Monta a lista cruzando os dados com o cálculo em tempo real lá do ControladorAtendimento
        atendimentos_com_saldo = []
        for a in atendimentos:
            saldo_restante = controlador_atendimento.calcula_restante(a)
            atendimentos_com_saldo.append((a, saldo_restante))

        # Envia para a nova tela gráfica tratar a exibição elegante
        self.__tela_pagamento.mostra_atendimentos(atendimentos_com_saldo)
        
        indice = self.__tela_pagamento.get_indice_atendimento(len(atendimentos))
        if indice is None:
            return
            
        atendimento = atendimentos[indice]
        paciente = atendimento.paciente

        # Calcula o valor restante usando a fonte dinâmica
        valor_restante = controlador_atendimento.calcula_restante(atendimento)
        if valor_restante <= 0:
            self.__tela_pagamento.mostra_mensagem("Este atendimento já está totalmente pago.")
            return

        self.__tela_pagamento.mostra_mensagem(
            f"Valor total: R$ {atendimento.valor:.2f}\nValor restante a pagar: R$ {valor_restante:.2f}"
        )

        tipo_pagamento = self.__tela_pagamento.get_tipo_pagamento()
        if tipo_pagamento == 0 or tipo_pagamento is None:
            return

        dados = self.__tela_pagamento.get_dados_pagamento(tipo_pagamento)
        if not dados:
            return

        # Garante que o usuário não pague mais do que o que está devendo
        if dados['valor_pago'] > valor_restante:
            self.__tela_pagamento.mostra_mensagem(
                f"Erro: O valor pago (R$ {dados['valor_pago']:.2f}) é maior do que o saldo restante (R$ {valor_restante:.2f})."
            )
            return

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
            # Substituído o id() temporário por uma string única combinando o código e o timestamp/contador interno se aplicável,
            # mas mantendo o add estruturado para o DAO persistir no .pkl
            chave = f"PAG_{atendimento.codigo}_{len(self.__pagamento_dao.get_all()) + 1}"
            self.__pagamento_dao.add(chave, pagamento)
            
            self.__tela_pagamento.mostra_mensagem("Pagamento registrado com sucesso!")
            
            # Recalcula dinamicamente após a inserção no arquivo
            restante_final = controlador_atendimento.calcula_restante(atendimento)
            if restante_final > 0:
                self.__tela_pagamento.mostra_mensagem(f"Ainda resta R$ {restante_final:.2f} a pagar neste atendimento.")
            else:
                self.__tela_pagamento.mostra_mensagem("Atendimento totalmente quitado!")

    def buscar_pagamentos_por_atendimento(self, atendimento):
        return [p for p in self.__pagamento_dao.get_all() if p.atendimento.codigo == atendimento.codigo]

    def listar_pagamentos(self):
        self.__tela_pagamento.mostra_pagamentos(self.__pagamento_dao.get_all())