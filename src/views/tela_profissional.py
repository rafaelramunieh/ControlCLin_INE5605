from models.profissional import Profissional
from controllers.controlador_profissional import ControladorProfissional

class TelaProfissional:
    def __init__(self):
        pass
    
    def mostra_menu_profissional(self):
        print("1. Incluir profissional")
        print("2. Listar profissionais")
        print("3. Excluir profissional")
        print("4. Editar profissional")
        print("5. Voltar ao menu principal")
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_dados_profissional(self):
        nome = input("Digite o nome do profissional: ")
        celular = int(input("Digite o celular do profissional: "))
        cpf = input("Digite o CPF do profissional: ")
        especialidade = input("Digite a especialidade do profissional: ")
        registro_profissional = input("Digite o registro profissional do profissional: ")
        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade, "registro_profissional": registro_profissional}
    
    def mostra_profissionais(self, profissionais):
        print("---------- LISTA DE PROFISSIONAIS ----------")
        for profissional in profissionais:
            print("-" * 30)
            print(f"Nome: {profissional.nome}, Celular: {profissional.celular}, CPF: {profissional.cpf}, Especialidade: {profissional.especialidade}, Registro Profissional: {profissional.registro_profissional}")
        
    