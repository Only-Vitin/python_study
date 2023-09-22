from typing import Union
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def get_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        if tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()

        raise NotImplementedError("Esse tipo de fila não existe!")

    @staticmethod
    def second_method():
        ...
