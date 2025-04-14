"""
    CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER
    PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
    EX: 6.127 TEM A PARTE INTEIRA 6.
"""
import math
n = float(input('Digite um número real qualquer: '))
print(math.trunc(n))
