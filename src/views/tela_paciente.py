class TelaPaciente:
    def __init__(self):
        pass
    
    def mostra_menu_paciente(self):
        print("Menu Paciente:")
        print("1. Incluir paciente")
        print("2. Listar pacientes")
        print("3. Excluir paciente")
        print("4. Editar paciente")
        print("5. Voltar ao menu principal")
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return 0
    
    def pega_dados_paciente(self):
        nome = input("Digite o nome do paciente: ")
        celular = int(input("Digite o celular do paciente: "))
        cpf = input("Digite o CPF do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        return {"nome": nome, "celular": celular, "cpf": cpf, "idade": idade}
    
    def mostra_pacientes(self, pacientes):
        print("---------- LISTA DE PACIENTES ----------")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return
        for paciente in pacientes:
            print("-" * 30)
            print(f"Nome: {paciente.nome}, Celular: {paciente.celular}, CPF: {paciente.cpf}, Idade: {paciente.idade}")
        
        