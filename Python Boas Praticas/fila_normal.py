from fila_base import FilaBase

from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):

    def __init__(self) -> None:
        super().__init__()

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'
        
    #Para não dar erro
    def estatistica(self, dia: str, agencia: str, flag: str):
        ...
    