class TelaProfissional:
    def __init__(self):
        pass

    def mostra_menu_profissional(self):
        print("\n---------- MENU PROFISSIONAL ----------")
        print("1. Incluir profissional")
        print("2. Listar profissionais")
        print("3. Excluir profissional")
        print("4. Editar profissional")
        print("5. Voltar ao menu principal")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            return 0

    def pega_dados_profissional(self):
        nome = input("Digite o nome do profissional: ")
        try:
            celular = int(input("Digite o celular do profissional (somente números): "))
        except ValueError:
            print("Celular inválido. Usando 0.")
            celular = 0
        cpf = input("Digite o CPF do profissional: ")
        especialidade = input("Digite a especialidade do profissional: ")
        registro_profissional = input("Digite o registro profissional: ")
        return {"nome": nome, "celular": celular, "cpf": cpf,
                "especialidade": especialidade, "registro_profissional": registro_profissional}

    def mostra_profissionais(self, profissionais):
        print("\n---------- LISTA DE PROFISSIONAIS ----------")
        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return
        for i, profissional in enumerate(profissionais, 1):
            print("-" * 30)
            print(f"{i}. Nome: {profissional.nome} | Celular: {profissional.celular} | "
                f"CPF: {profissional.cpf} | Especialidade: {profissional.especialidade} | "
                f"Registro: {profissional.registro_profissional}")