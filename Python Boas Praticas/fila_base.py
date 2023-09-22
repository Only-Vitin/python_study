from typing import List, Dict, Union
from abc import abstractmethod, ABCMeta

from constantes import TAMANHO_CODIGO_MAXIMO, TAMANHO_CODIGO_MINIMO


class FilaBase(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        self.codigo: int = 0
        self.senha_atual: str = ""
        self.fila: List[str] = []
        self.clientes_atendidos: List[str] = []

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_CODIGO_MAXIMO:
            self.codigo = TAMANHO_CODIGO_MINIMO
        else:
            self.codigo += 1

    @abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def chama_cliente(self, caixa: int) -> str:
        try:
            cliente_atual: str = self.fila.pop(0)
            self.clientes_atendidos.append(cliente_atual)
        except IndexError as exc:
            raise ValueError("Não há mais clientes na fila") from exc

        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {str(caixa)}"

    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        estatistica: Dict[str, Union[str, int, List[str]]] = {}
        if flag != "detail":
            estatistica[f"{agencia} - {dia}"] = len(self.clientes_atendidos)
        else:
            estatistica["Dia"] = dia
            estatistica["Agencia"] = agencia
            estatistica["Clientes atendidos"] = self.clientes_atendidos
            estatistica["Quantidade de clientes atendidos"] = len(
                self.clientes_atendidos
            )

        return estatistica