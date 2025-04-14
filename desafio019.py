"""
    UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA
    APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O
    NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
"""
"""import random
print('Entre com o nome dos alunos: ')
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

#sorteando números aleatórios entre 1 e 4
sorteado = random.randint(1,4)

#criando a variável diretamente

escolhido = (sorteado == 1)*aluno1 + (sorteado == 2)*aluno2 + (sorteado == 3)*aluno3 + (sorteado == 4)*aluno4

print(f'O aluno sorteado foi: {escolhido}')"""
from random import choice
print('Entre com o nome dos alunos: ')
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno sorteado foi: {escolhido}')
