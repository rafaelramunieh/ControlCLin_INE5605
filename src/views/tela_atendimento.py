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
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def pega_tipo_atendimento(self):
        print("\n--- TIPO DE ATENDIMENTO ---")
        tipos = list(TipoAtendimento)
        for i, tipo in enumerate(tipos, 1):
            print(f"{i}. {tipo.descricao} (R$ {tipo.valor_base:.2f})")
        try:
            opcao = int(input("Escolha o tipo: "))
            if 1 <= opcao <= len(tipos):
                return tipos[opcao - 1]
            print("[Erro] Opção inválida.")
            return None
        except ValueError:
            print("[Erro] Entrada inválida.")
            return None

    def pega_dados_atendimento(self):
        print("\n--- INFORME OS DADOS DO ATENDIMENTO ---")
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
        except ValueError:
            print("[Erro] Data inválida.")
            return None
        horario_inicio = input("Horário de Início (HH:MM): ")
        horario_fim = input("Horário de Fim (HH:MM): ")
        return {
            "dia": dia, "mes": mes, "ano": ano,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim
        }

    def mostra_atendimentos(self, atendimentos):
        print("\n---------- LISTA DE ATENDIMENTOS ----------")
        if not atendimentos:
            print("Nenhum atendimento agendado.")
            return
        for idx, a in enumerate(atendimentos, 1):
            print("-" * 40)
            print(f"Atendimento N° {idx}")
            print(f"Data: {a.data} | Horário: {a.horario_inicio} às {a.horario_fim}")
            print(f"Clínica: {a.clinica.nome if a.clinica else 'Não informada'}")
            print(f"Paciente: {a.paciente.nome if a.paciente else 'Não informado'}")
            print(f"Profissional: {a.profissional.nome if a.profissional else 'Não informado'}")
            print(f"Tipo: {a.tipoAtendimento.descricao} | Valor: R$ {a.valor:.2f} | Restante: R$ {a.calcula_restante():.2f}")