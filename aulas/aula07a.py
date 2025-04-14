"""OPERADORES ARITMÉTICOS
    + ADIÇÃO        **POTÊNCIA pow(,)
    - SUBTRAÇÃO     //DIVISÃO INTEIRA
    * MULTIPLICAÇÃO     %RESTO DA DIVISÃO
    / DIVISÃO       RAIZ QUADRADA: 25**(1/2)
    RAIZ CÚBICA: 8**(1/3)
"""
""" ORDEM DE PRECEDÊNCIA
        1- ()
        2- **
        3- *,/,//,%
        4- +,-
"""
"""
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')
"""

"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma de {n1}+{n2} vale = {n1+n2}')
"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
menos = n1 - n2
mult = n1 * n2
div = n1/n2
pot = n1 ** n2
print(f'A soma de {n1}+{n2} vale = {n1+n2}', end=' /// ')
print(f'A subtração de {n1}-{n2} vale = {n1-n2}')
print(f'A multiplicação de {n1}*{n2} vale = {n1*n2}')
print(f'A divisão de {n1}/{n2} vale = {n1/n2:.3f}')
print(f'A potência de {n1}^{n2} vale = {n1**n2}')
