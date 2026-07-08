from views.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    def abrir_menu(self):
        while True:
            opcao = self.__tela_relatorio.mostra_menu_relatorio()
            if opcao == 1:
                self.clinicas_mais_atendimentos()
            elif opcao == 2:
                self.atendimentos_mais_caros_baratos()
            elif opcao == 3:
                self.procedimentos_mais_populares()
            elif opcao == 4:
                self.procedimentos_mais_caros_baratos()
            elif opcao == 5:
                break
            else:
                self.__tela_relatorio.mostra_mensagem(f"Opção inválida. Tente novamente.")

    def __get_procedimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        procedimentos = []
        for a in atendimentos:
            procedimentos.extend(a.procedimentos)
        return procedimentos

    def clinicas_mais_atendimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(f"Nenhum atendimento registrado.")
            return
        contagem = {}
        for a in atendimentos:
            nome = a.clinica.nome
            contagem[nome] = contagem.get(nome, 0) + 1
        ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        self.__tela_relatorio.mostra_ranking_clinicas(ranking)

    def atendimentos_mais_caros_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(f"Nenhum atendimento registrado.")
            return
        mais_caro = max(atendimentos, key=lambda a: a.valor)
        mais_barato = min(atendimentos, key=lambda a: a.valor)
        self.__tela_relatorio.mostra_atendimentos_extremos(mais_caro, mais_barato)

    def procedimentos_mais_populares(self):
        procedimentos = self.__get_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem(f"Nenhum procedimento registrado.")
            return
        contagem = {}
        for p in procedimentos:
            contagem[p.descricao] = contagem.get(p.descricao, 0) + 1
        ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        self.__tela_relatorio.mostra_ranking_procedimentos(ranking)

    def procedimentos_mais_caros_baratos(self):
        procedimentos = self.__get_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem(f"Nenhum procedimento registrado.")
            return
        mais_caro = max(procedimentos, key=lambda p: p.custo)
        mais_barato = min(procedimentos, key=lambda p: p.custo)
        self.__tela_relatorio.mostra_procedimentos_extremos(mais_caro, mais_barato)