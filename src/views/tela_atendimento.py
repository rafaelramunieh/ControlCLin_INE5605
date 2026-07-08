from models.tipo_atendimento import TipoAtendimento

class TelaAtendimento:
    def __init__(self):
        pass
    
    def mostra_menu_atendimento(self):
        print("\n---------- MENU ATENDIMENTOS ----------")
        print("1. Agendar atendimento")
        print("2. Listar atendimentos")
        print("3. Excluir atendimento")
        print("4. Voltar ao menu principal")
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1
    
    def pega_dados_atendimento(self):
        print("\n--- INFORME OS DADOS DO ATENDIMENTO ---")

        clinica_nome = input("Nome da Clínica: ")
        paciente_cpf = input("CPF do Paciente: ")
        profissional_cpf = input("CPF do Profissional: ")

        data = input("Data (DD/MM/AAAA): ")
        horario_inicio = input("Horário de Início (HH:MM): ")
        horario_fim = input("Horário de Fim (HH:MM): ")

        return {
            "clinica_nome": clinica_nome,
            "paciente_cpf": paciente_cpf,
            "profissional_cpf": profissional_cpf,
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim
        }
        
    def mostra_atendimentos(self, atendimentos):
        print("---------- LISTA DE ATENDIMENTOS ----------")
        if not atendimentos:
            print("Nenhum atendimento agendado.")
            return
            
        for idx, atendimento in enumerate(atendimentos, 1):
            print("-" * 40)
            print(f"Atendimento N° {idx}")
            print(f"Data: {atendimento.data} | Horário: {atendimento.horario_inicio} às {atendimento.horario_fim}")
            print(f"Clínica: {atendimento.clinica.nome if atendimento.clinica else 'Não informada'}")
            print(f"Paciente: {atendimento.paciente.nome if atendimento.paciente else 'Não informado'}")
            print(f"Profissional: {atendimento.profissional.nome if atendimento.profissional else 'Não informado'}")
            print(f"Categoria: {atendimento.tipoAtendimento.name} | Tipo: {atendimento.tipoAtendimento.value['descricao']}")
            print(f"Valor: R$ {atendimento.valor:.2f}")
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
    
    def pega_tipo_atendimento(self):
        
        print("\nSelecione o Tipo de Atendimento:")

        tipos = list(TipoAtendimento)

        for i, tipo in enumerate(tipos, start=1):
            print(f"{i}. {tipo.name}")

        try:
            opcao = int(input("Escolha o número correspondente: "))

            if 1 <= opcao <= len(tipos):
                return tipos[opcao - 1]

            self.mostra_mensagem("Opção inválida.")
            return None

        except ValueError:
            self.mostra_mensagem("Opção inválida.")
            return None