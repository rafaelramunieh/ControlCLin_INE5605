class TelaSistema:
    def __init__(self):
        pass

    def mostra_menu_principal(self):
        print("\n======== SISTEMA DE GESTÃO DE CLÍNICAS ========")
        print("1. Clínicas")
        print("2. Profissionais")
        print("3. Pacientes")
        print("4. Atendimentos")
        print("5. Pagamentos")
        print("6. Relatórios")
        print("0. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            return -1

    def mostra_mensagem_saida(self):
        print("Encerrando o sistema. Até logo!")

    def mostra_opcao_invalida(self):
        print("Opção inválida. Tente novamente.")