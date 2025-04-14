"""
    O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM
    DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA
    O NOME DOS QUATRO E MOSTRE A ORDEM SORTEADO.
"""
import random

print('Entre com o nome dos alunos: ')
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)