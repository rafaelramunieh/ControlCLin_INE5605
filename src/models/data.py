class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        if not self.validar_data(dia, mes, ano):
            raise ValueError("Data inválida")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    @property
    def dia(self):
        return self.__dia
    
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano

    @staticmethod
    def validar_data(dia: int, mes: int, ano: int) -> bool:
        if ano < 1 or mes < 1 or mes > 12 or dia < 1:
            return False
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return dia <=31
        elif mes in [4, 6, 9, 11]:
            return dia <=30
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return dia <=29
            else:
                return dia <=28
        return False
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

    def __lt__(self, other_data: 'Data') -> bool:
        if self.ano != other_data.ano:
            return self.ano < other_data.ano
        if self.mes != other_data.mes:
            return self.mes < other_data.mes
        return self.dia < other_data.dia

    def __eq__(self, other_data: 'Data') -> bool:
        return (self.ano == other_data.ano and 
        self.mes == other_data.mes and 
        self.dia == other_data.dia)
    
    def __le__(self, other_data: 'Data'):
        return self.__lt__(other_data) or self.__eq__(other_data)