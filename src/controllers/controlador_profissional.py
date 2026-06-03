from models.profissional import Profissional
from views.tela_profissional import TelaProfissional

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()

    @property
    def profissionais(self):
        return self.__profissionais

    def incluir_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        profissional = Profissional(dados_profissional['nome'], dados_profissional['celular'], 
                                    dados_profissional['cpf'], dados_profissional['especialidade'], 
                                    dados_profissional['registro_profissional'])
        self.__profissionais.append(profissional)
    
    def buscar_profissional(self, cpf):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None
    
    def excluir_profissional(self, cpf):
        profissional = self.buscar_profissional(cpf)
        if profissional:
            self.__profissionais.remove(profissional)
            print(f"Profissional com CPF {cpf} excluído.")
            return
        print(f"Profissional com CPF {cpf} não encontrado.")
    
    def editar_profissional(self, cpf):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                dados_profissional = self.__tela_profissional.pega_dados_profissional()
                profissional.nome = dados_profissional['nome']
                profissional.celular = dados_profissional['celular']
                profissional.especialidade = dados_profissional['especialidade']
                profissional.registro_profissional = dados_profissional['registro_profissional']
                print(f"Profissional com CPF {cpf} editado.")
                return
        print(f"Profissional com CPF {cpf} não encontrado.")
        