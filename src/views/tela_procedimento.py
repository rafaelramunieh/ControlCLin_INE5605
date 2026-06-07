class TelaProcedimento:
    def __init__(self):
        pass

    def mostra_menu_procedimento(self):
        print("---- MENU PROCEDIMENTOS ----")
        print("1. Adicionar um procedimento a um atendimento")
        print("2. Listar todos os procedimentos")
        print("3. Voltar ao menu principal")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def pega_dados_procedimento(self):
        descricao = input("Descrição do procedimento: ")
        try:
            custo = float(input("Custo do procedimento: R$ "))
        except ValueError:
            print("[Erro] Custo Inválido.")
            return None
        return {"descricao": descricao, "custo": custo}
    
    def mostra_atendimentos(self, atendimentos):
        print("---- ATENDIMENTOS DISPONÍVEIS ----")
        for i, a in enumerate(atendimentos, 1):
            print((f"{i}. {a.paciente.nome} | {a.tipoAtendimento.descricao} | {a.data}"))

    def mostra_procedimentos(self, procedimentos):
        print("\n---------- LISTA DE PROCEDIMENTOS ----------")
        if not procedimentos:
            print("Nenhum procedimento registrado.")
            return
        for atendimento, proc in procedimentos:
            print("-" * 40)
            print(f"Atendimento: {atendimento.paciente.nome} | {atendimento.data}")
            print(f"Procedimento: {proc.descricao}")
            print(f"Custo: R$ {proc.custo:.2f}")
            print(f"Profissional: {proc.profissional.nome}")
        