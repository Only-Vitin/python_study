from typing import Dict, Union, List
from fila_base import FilaBase

from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):

    def __init__(self) -> None:
        super().__init__()
    
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        estatistica: Dict[str, Union[str, int, List[str]]] = {}
        if flag != 'detail':
            estatistica[f"{agencia} - {dia}"] = len(self.clientes_atendidos)
        else:
            estatistica['Dia'] = dia
            estatistica['Agencia'] = agencia
            estatistica['Clientes atendidos'] = self.clientes_atendidos
            estatistica['Quantidade de clientes atendidos'] = (
                len(self.clientes_atendidos)
            )

        return estatistica
    