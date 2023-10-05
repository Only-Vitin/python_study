from registro import RegistroChegadaLog
from registro import dias_da_semana

def exibir_ajuda() -> None:
    print("Opções disponíveis:")
    print("  'c' - Registrar chegada")
    print("  'h' - Histórico de chegadas")
    print("  'm' - Médias dos horários")
    print("  'g' - Gerar gráfico")
    print("  'r' - Remove registro")

def formata_dia(par):
    if ' ' in par:
        par = par.replace(' ', '-')

    par = par.lower().capitalize()
    for dia in dias_da_semana:
        if par in dia:
            par = dia
            break
    return par

def opera(operacao:str):
    registro_chegada_log = RegistroChegadaLog()
    if operacao == "c":
        usuario = input("Digite o nome do usuário: ")
        registro_chegada_log.adicionar_chegada(usuario)
        print(f"Registro de horário feito com sucesso - {usuario}\n")

    elif operacao == "h":
        dia = input("Qual dia você deseja ver ? ")
        dia_formatado = formata_dia(dia)

        print(registro_chegada_log.historico_dia(dia_formatado))

    elif operacao == "m":
        print(registro_chegada_log.retorna_media())

    elif operacao == "g":
        registro_chegada_log.mostra_grafico()

    elif operacao == "r":
        data = input("Digite a data que deseja remover: ")
        registro_chegada_log.remove_linha(data)
        print("Registro removido com sucesso!")

    elif operacao == "help":
        exibir_ajuda()

    else:
        print("Operação inválida. Digite 'h' para ajuda.")
        