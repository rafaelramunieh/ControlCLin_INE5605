from enum import Enum

class TipoAtendimento(Enum):
    # Membros do Enum configurados com dicionário
    CONSULTA = {
        "descricao": "Consulta de Rotina", 
        "valor_base": 150.0
    }
    RETORNO = {
        "descricao": "Retorno de Atendimento", 
        "valor_base": 0.0
    }
    URGENCIA = {
        "descricao": "Atendimento de Urgência", 
        "valor_base": 250.0
    }
    SESSAO = {
        "descricao": "Sessão de Tratamento/Acompanhamento", 
        "valor_base": 100.0
    }

    def __init__(self, dados: dict):

        self._descricao = dados["descricao"]
        self._valor_base = dados["valor_base"]

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def valor_base(self) -> float:
        return self._valor_base