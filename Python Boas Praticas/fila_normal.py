from fila_base import FilaBase

from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    
    def gera_senha_atual(self):
        self.senha_atual = f"{CODIGO_NORMAL}{self.codigo}"
        