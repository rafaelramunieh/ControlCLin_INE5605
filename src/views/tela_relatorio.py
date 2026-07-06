class TelaRelatorio:
    def __init__(self):
        pass

    def mostra_menu_relatorio(self):
        print("\n---------- MENU RELATÓRIOS ----------")
        print("1. Clínicas com maior número de atendimentos")
        print("2. Atendimentos mais caros e mais baratos")
        print("3. Procedimentos mais realizados")
        print("4. Procedimentos mais caros e mais baratos")
        print("5. Voltar ao menu principal")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostra_ranking_clinicas(self, ranking):
        print("\n---------- CLÍNICAS POR Nº DE ATENDIMENTOS ----------")
        if not ranking:
            print("Nenhum dado encontrado para gerar o ranking.")
            return
        for i, (nome, total) in enumerate(ranking):
            print(f"{i+1}º {nome}: {total} atendimento(s)")

    def mostra_atendimentos_extremos(self, mais_caro, mais_barato):
        print("\n---------- ATENDIMENTOS ----------")
        # Correção: Acessa a descrição de dentro do dicionário do Enum (.value)
        desc_caro = mais_caro.tipoAtendimento.value['descricao']
        desc_barato = mais_barato.tipoAtendimento.value['descricao']
        
        print(f"Mais caro:   {mais_caro.paciente.nome} | {desc_caro} | R$ {mais_caro.valor:.2f}")
        print(f"Mais barato: {mais_barato.paciente.nome} | {desc_barato} | R$ {mais_barato.valor:.2f}")

    def mostra_ranking_procedimentos(self, ranking):
        print("\n---------- PROCEDIMENTOS MAIS REALIZADOS ----------")
        if not ranking:
            print("Nenhum dado encontrado para gerar o ranking.")
            return
        for i, (descricao, total) in enumerate(ranking):
            print(f"{i+1}º {descricao}: {total} vez(es)")

    def mostra_procedimentos_extremos(self, mais_caro, mais_barato):
        print("\n---------- PROCEDIMENTOS ----------")
        print(f"Mais caro:   {mais_caro.descricao} | R$ {mais_caro.custo:.2f}")
        print(f"Mais barato: {mais_barato.descricao} | R$ {mais_barato.custo:.2f}")

    # --- MÉTODO CENTRALIZADO DE MENSAGENS EXIGIDO PELO MVC ---
    def mostra_mensagem(self, mensagem: str):
        """Único ponto do controlador de relatórios autorizado a exibir avisos na tela"""
        print(f"\n[Aviso] {mensagem}")