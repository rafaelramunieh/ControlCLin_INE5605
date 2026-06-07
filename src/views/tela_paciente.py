class TelaPaciente:
    def __init__(self):
        pass

    def mostra_menu_paciente(self):
        print("\n---------- MENU PACIENTE ----------")
        print("1. Incluir paciente")
        print("2. Listar pacientes")
        print("3. Excluir paciente")
        print("4. Editar paciente")
        print("5. Voltar ao menu principal")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            return -1

    def pega_dados_paciente(self):
        nome = input("Digite o nome do paciente: ")
        try:
            celular = int(input("Digite o celular do paciente: "))
        except ValueError:
            print("Celular inválido. Usando 0.")
            celular = 0
        cpf = input("Digite o CPF do paciente: ")
        try:
            idade = int(input("Digite a idade do paciente: "))
        except ValueError:
            print("Idade inválida. Usando 0.")
            idade = 0
        return {"nome": nome, "celular": celular, "cpf": cpf, "idade": idade}

    def mostra_pacientes(self, pacientes):
        print("\n---------- LISTA DE PACIENTES ----------")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return
        for paciente in pacientes:
            print("-" * 30)
            print(f"Nome: {paciente.nome} | Celular: {paciente.celular} | CPF: {paciente.cpf} | Idade: {paciente.idade}")