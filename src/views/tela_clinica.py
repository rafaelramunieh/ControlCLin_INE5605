class TelaClinica:
    def __init__(self):
        pass
    
    def mostra_menu_clinica(self):
        print("1. Incluir clínica")
        print("2. Listar clínicas")
        print("3. Excluir clínica")
        print("4. Editar clínica")
        print("5. Voltar ao menu principal")
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return 0
        
    
    def pega_dados_clinica(self):
        nome = input("Digite o nome da clínica: ")
        localizacao = input("Digite a localização da clínica: ")
        descricao = input("Digite a descrição da clínica: ")
        horario_abertura = input("Digite o horário de abertura da clínica: ")
        horario_fechamento = input("Digite o horário de fechamento da clínica: ")
        return {"nome": nome, "localizacao": localizacao, "descricao": descricao, "horario_abertura": horario_abertura, "horario_fechamento": horario_fechamento}
    
    def mostra_clinicas(self, clinicas):
        print("---------- LISTA DE CLÍNICAS ----------")
        if not clinicas:
            print("Nenhuma clínica cadastrada.")
            return
        for clinica in clinicas:
            print("-" * 30)
            print(f"Nome: {clinica.nome}, Localização: {clinica.localizacao}, Descrição: {clinica.descricao}, Horário de Abertura: {clinica.horario_abertura}, Horário de Fechamento: {clinica.horario_fechamento}")