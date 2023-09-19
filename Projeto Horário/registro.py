import re
from datetime import datetime

dias_da_semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

class RegistroChegada:

    def __init__(self):
        self.registro_tempo = self.obter_tempo_atual()
        self.dia_da_semana = self.obter_dia_da_semana()
        self.data = self.obter_data()
        self.hora = self.obter_hora()

    def obter_tempo_atual(self):
        return datetime.today()

    def obter_dia_da_semana(self):
        return dias_da_semana[self.registro_tempo.weekday()]

    def obter_data(self):
        return self.registro_tempo.strftime("%d/%m/%Y")

    def obter_hora(self):
        return self.registro_tempo.strftime("%H:%M:%S")

class RegistroChegadaLog:

    def __init__(self):
        self.registro_semanal = {dia: [] for dia in dias_da_semana}

    def __str__(self):
        resultado = ""
        for dia in dias_da_semana:
            resultado += "{}: {}\n".format(dia, self.formatar_tempo(self.calcular_tempo_medio()[dia]))
        return resultado

    @staticmethod
    def extrair_segundos(tempo_str):
        horas, minutos, segundos = map(int, tempo_str.split(':'))
        return horas * 3600 + minutos * 60 + segundos

    @staticmethod
    def formatar_tempo(segundos):
        horas = int(segundos / 3600)
        segundos %= 3600
        minutos = int(segundos / 60)
        segundos %= 60
        segundos = int(segundos)
        return "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)

    def adicionar_chegada(self, usuario):
        registro_tempo = RegistroChegada()
        registro_chegada_info = f">>> Registrado por: {usuario} -> Dia: {registro_tempo.dia_da_semana} - {registro_tempo.data} às {registro_tempo.hora}"
        self.registro_semanal[registro_tempo.dia_da_semana].insert(0, registro_chegada_info)

    def calcular_tempo_medio(self):
        tempos_medios = {dia: 0 for dia in dias_da_semana}
        contagem = {dia: 0 for dia in dias_da_semana}

        for dia in dias_da_semana:
            for chegada in self.registro_semanal[dia]:
                tempo_str = re.search(r"\d{2}:\d{2}:\d{2}", chegada).group()
                segundos = self.extrair_segundos(tempo_str)
                tempos_medios[dia] += segundos
                contagem[dia] += 1

            if contagem[dia] > 0:
                tempos_medios[dia] /= contagem[dia]

        return tempos_medios