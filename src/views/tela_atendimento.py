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
        tipo = input("Tipo de atendimento (Ex: Particular, Retorno): ")
        
        try:
            valor = float(input("Valor do atendimento: "))
        except ValueError:
            valor = 0.0
            
        print("\nSelecione o Tipo de Atendimento:")
        for t in TipoAtendimento:
            print(f"{t.value}. {t.name}")
        
        try:
            opcao_tipo = int(input("Escolha o número correspondente: "))
            tipo_atendimento = TipoAtendimento(opcao_tipo)
        except (ValueError, ValueError):
            print("[Aviso] Opção inválida. Definido como CONSULTA por padrão.")
            tipo_atendimento = TipoAtendimento.CONSULTA
            
        return {
            "clinica_nome": clinica_nome,
            "paciente_cpf": paciente_cpf,
            "profissional_cpf": profissional_cpf,
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "tipo": tipo,
            "valor": valor,
            "tipoAtendimento": tipo_atendimento
        }
    
    def mostra_atendimentos(self, atendimentos):
        print("\n---------- LISTA DE ATENDIMENTOS ----------")
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
            print(f"Categoria: {atendimento.tipoAtendimento.name} | Tipo: {atendimento.tipo}")
            print(f"Valor: R$ {atendimento.valor:.2f}")