from datetime import time as Time
from models.atendimento import Atendimento
from views.tela_atendimento import TelaAtendimento

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = []
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abrir_menu(self):
        while True:
            opcao = self.__tela_atendimento.mostra_menu_atendimento()
            
            if opcao == 1:
                self.incluir_atendimento()
            elif opcao == 2:
                self.listar_atendimentos()
            elif opcao == 3:
                self.excluir_atendimento()
            elif opcao == 4:
                break
            else:
                print("\n[Erro] Opção inválida! Tente novamente.")

    def incluir_atendimento(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()
        clinica = self.__controlador_sistema.controlador_clinica.buscar_clinica(dados['clinica_nome'])
        paciente = self.__controlador_sistema.controlador_paciente.buscar_paciente(dados['paciente_cpf'])
        profissional = self.__controlador_sistema.controlador_profissional.buscar_profissional(dados['profissional_cpf'])
        
        if not clinica:
            print("\n[Erro] Clínica não encontrada no sistema!")
            return
        if not paciente:
            print("\n[Erro] Paciente não encontrado no sistema!")
            return
        if not profissional:
            print("\n[Erro] Profissional não encontrado no sistema!")
            return

        try:
            h_ini, m_ini = map(int, dados['horario_inicio'].split(':'))
            h_fim, m_fim = map(int, dados['horario_fim'].split(':'))
            horario_inicio = Time(h_ini, m_ini)
            horario_fim = Time(h_fim, m_fim)
        except ValueError:
            print("\n[Erro] Formato de hora inválido! Use o padrão HH:MM.")
            return

        novo_atendimento = Atendimento(
            clinica=clinica,
            paciente=paciente,
            profissional=profissional,
            data=dados['data'], 
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            tipo=dados['tipo'],
            valor=dados['valor'],
            tipoAtendimento=dados['tipoAtendimento']
        )
        
        self.__atendimentos.append(novo_atendimento)
        print("\n[Sucesso] Atendimento agendado com sucesso!")

    def listar_atendimentos(self):
        self.__tela_atendimento.mostra_atendimentos(self.__atendimentos)

    def excluir_atendimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
            
        try:
            indice = int(input("\nDigite o número do atendimento que deseja excluir: ")) - 1
            if 0 <= indice < len(self.__atendimentos):
                atendimento_removido = self.__atendimentos.pop(indice)
                print(f"\nAtendimento do dia {atendimento_removido.data} foi excluído.")
            else:
                print("\nNúmero de atendimento inválido.")
        except ValueError:
            print("\nEntrada inválida.")