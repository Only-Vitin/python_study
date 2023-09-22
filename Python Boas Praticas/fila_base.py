from colorama import Fore, Style
from typing import List
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
        except IndexError:
            raise Exception(Fore.RED + "Não há mais clientes na fila" + Style.RESET_ALL)

        return f"Cliente atual: {Fore.GREEN + cliente_atual + Style.RESET_ALL}, dirija-se ao caixa: {Fore.GREEN + str(caixa) + Style.RESET_ALL}"
