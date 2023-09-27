'''
Anotações sobre os comandos try/except
'''

try:
    ...
    #Código a ser executado, caso tenha uma exceção para imediatamente
except:
    ...
    #Se uma exceção for lançada no try, rode este script, senão pule
else:
    ...
    #Se não houver exceção no try, rode este scripts
finally:
    ...
    #Rode esse script (com ou sem exceção)

##################################################################

notas = {
    'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],
    'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 
    'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]
}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")

#####################################

notas = {
    'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],
    'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 
    'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]
}

def media(notas):
    if len(notas) > 3:
        raise ValueError("Por favor, não digite mais que 3 notas")
    return sum(notas)/len(notas)

try:
    nome = input("Digite o nome do(a) estudante: ")
    nota_aluno = notas[nome]
    med = media(nota_aluno)
except KeyError:
    print("Estudante não matriculado(a) na turma")
except TypeError:
    print("São permitidos apenas valores numéricos")
except ValueError as e:
    print(e)
else:
    print("Media: ", med)
finally:
    print("A consulta foi encerrada!")