from models.pagamentoCartaoCredito import PagamentoCartaoCredito
from models.pagamentoDinheiro import PagamentoDinheiro
from models.pagamentoPix import PagamentoPix

class TelaPagamento():
    def __init__(self):
        pass

    def mostra_menu_pagamento(self):
        print("---- MENU PAGAMENTO ----")
        print("1. Registrar Pagamento")
        print("2. Listar Pagamentos")
        print("3. Retornar ao menu principal")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def get_tipo_pagamento(self):
        print("---- FORMA DE PAGAMENTO ----")
        print("1. Dinheiro")
        print("2. Pix")
        print("3. Cartão de crédito")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def get_dados_pagamento(self, tipo_pagamento):
        data = input("Digite a data do pagamento (ex: 03/06/2026):")
        valor_pago = float(input("Digite o valor pago: R$ "))

        dados = {"data": data, "valor_pago": valor_pago}

        if tipo_pagamento == 2: # Pix
            cpf_pagador = input("Digite o CPF do pagador: ")
            dados['cpf_pagador'] = cpf_pagador

        elif tipo_pagamento == 3: # Cartão de crédito
            numero_cartao = input("Digite o número do cartão: ")
            bandeira_cartao = input("Digite a bandeira do cartão (Ex: Visa, Mastercard, etc.): ")
            dados["numero_cartao"] =  numero_cartao
            dados["bandeira_cartao"] = bandeira_cartao

        return dados

    def mostra_atendimentos(self, atendimentos):
        print("---- ATENDIMENTOS DISPONÍVEIS ----")
        for i, atendimento in enumerate(atendimentos):
            print(f"[{i}] Paciente: {atendimento.paciente.nome} | "
                f"Profissional: {atendimento.profissional.nome} | "
                f"Data: {atendimento.data} | "
                f"Valor total: R$ {atendimento.valor:.2f} | "
                f"Restante: R$ {atendimento.calcula_restante():.2f}")
    
    def get_indice_atendimento(self, total):
        indice = int(input("Digite o número do atendimento: "))
        if 0 <= indice < total:
            return indice
        else:
            print("Índice inválido")
        
    
    def mostra_pagamentos(self, pagamentos):
        print("---- LISTA DE PAGAMENTOS ----")
        if not pagamentos:
            print("Não há nenhum pagamento para esse atendimento")
            return
        
        for pagamento in pagamentos:
            print("-" * 40)
            print(f"Data: {pagamento.data}")
            print(f"Paciente: {pagamento.paciente.nome}")
            print(f"Valor Pago: {pagamento.valor_pago}")

            if isinstance(pagamento, PagamentoCartaoCredito):
                print(f"Pago com 'Cartão de Crédito'.")
                print(f"Número do cartão: {pagamento.numero_cartao}")
                print(f"Bandeira do car~tão: {pagamento.bandeira_cartao}")

            elif isinstance(pagamento, PagamentoPix):
                print(f"Pago com Pix")
                print(f"CPF do pagador: {pagamento.cpf_pagador}")
            
            else:
                print("Pago com Dinheiro")
