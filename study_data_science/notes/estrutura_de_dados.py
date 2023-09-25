'''
Anotações sobre estrutura de dados
'''

from typing import List

#Grafico
from matplotlib import pyplot as plt

nomes: List[str] = ["João", "Lucas", "Matheus", "José"]
notas: List[int | float] = [4.5, 8.9, 10, 1.5]

plt.bar(x= nomes, height=notas)
#plt.show()

######################################################

#Lambda
nota = float(input("Digite a nota: "))

soma1 = lambda nota: nota+1
arredonda = lambda nota: round(nota)
print(soma1(nota), arredonda(nota))

#Com varios valores
n1, n2, n3 = map(float, input("Digite as notas: ").split())

media = lambda n1, n2, n3: (n1+n2+n3)/3
print(media(n1, n2, n3))

#Utilizando o map
notas: List[int | float] = [2, 4.6, 9.99, 7.23, 10]

novas_notas: List[int | float] = list(map(lambda nota: nota+1, notas))
print(notas, novas_notas)

#Lambda com If e Else
novas_notas = list(map(lambda nota: nota+1 if nota < 10 else nota, notas))
print(notas, novas_notas)

######################################################

#List Comprehension
notas: List[List[int | float]] = [
    [3.4, 5, 9], [4.21, 7.98, 10], [0.4, 5.12, 8.94]
]

def media(lista) -> float:
    return sum(lista) / len(lista)

medias = [round(media(nota),1) for nota in notas]
print(medias)

#Zip
nomes: List[str] = ["João", "Lucas", "Matheus", "José"]
notas: List[int | float] = [10, 7.53, 4, 9.93]

alunos = list(zip(nomes, notas))
print(alunos)

#If
candidatos = [aluno[0] for aluno in alunos if aluno[1] > 8.0]
print(candidatos)

######################################################

#Dict Comprehension

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media Final", "Situação"]

cadastro  = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]

for i in range(len(cadastro['Estudante'])):
    print(f"Aluno: {cadastro['Estudante'][i]} - "
          f"Notas: {cadastro['Notas'][i]} - "
          f"Media: {cadastro['Media Final'][i]} - "
          f"Situação: {cadastro['Situação'][i]}"
    )
