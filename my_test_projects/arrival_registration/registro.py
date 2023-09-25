import re
from datetime import datetime
from typing import Tuple, Dict

dias_da_semana: Tuple[str] = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
)


class RegistroChegada:
    def __init__(self) -> None:
        self.registro_tempo: datetime = self.obter_tempo_atual()
        self.dia_da_semana: str = self.obter_dia_da_semana()
        self.data: str = self.obter_data()
        self.hora: str = self.obter_hora()

    def obter_tempo_atual(self) -> datetime:
        return datetime.today()

    def obter_dia_da_semana(self) -> str:
        return dias_da_semana[self.registro_tempo.weekday()]

    def obter_data(self) -> str:
        return self.registro_tempo.strftime("%d/%m/%Y")

    def obter_hora(self) -> str:
        return self.registro_tempo.strftime("%H:%M:%S")


class RegistroChegadaLog:
    def __init__(self) -> None:
        self.registro_semanal = {dia: [] for dia in dias_da_semana}

    def __str__(self) -> str:
        resultado: str = ""
        for dia in dias_da_semana:
            resultado += (
                f"{dia}:" f"{self.formatar_tempo(self.retorna_tempo_medio()[dia])}"
            )
        return resultado

    def extrair_segundos(self, tempo_str) -> int:
        horas, minutos, segundos = map(int, tempo_str.split(":"))
        return horas * 3600 + minutos * 60 + segundos

    def formatar_tempo(self, segundos) -> str:
        horas = int(segundos / 3600)
        segundos %= 3600
        minutos = int(segundos / 60)
        segundos %= 60
        segundos = int(segundos)
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def adicionar_chegada(self, usuario) -> None:
        registro = RegistroChegada()
        chegada_info: str = (
            "> Registrado por: "
            f"{usuario} -> Dia: {registro.dia_da_semana} -"
            f" {registro.data} às {registro.hora}"
        )
        self.registro_semanal[registro.dia_da_semana].insert(0, chegada_info)

    def calcula_tempo_medio(self, tempos_medios, contagem):
        for dia in dias_da_semana:
            for chegada in self.registro_semanal[dia]:
                tempo: str = re.search(r"\d{2}:\d{2}:\d{2}", chegada).group()
                segundos: int = self.extrair_segundos(tempo)
                tempos_medios[dia] += segundos
                contagem[dia] += 1

            if contagem[dia] > 0:
                tempos_medios[dia] /= contagem[dia]

    def retorna_tempo_medio(self) -> Dict[str, int]:
        tempos_medios: Dict[str, int] = {dia: 0 for dia in dias_da_semana}
        contagem: Dict[str, int] = {dia: 0 for dia in dias_da_semana}

        self.calcula_tempo_medio(tempos_medios, contagem)

        return tempos_medios
