idade = int(input())

ano = idade // 365
mes = (idade % 365) // 30
dia = (idade % 365) % 30

print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")
