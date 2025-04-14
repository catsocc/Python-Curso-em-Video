"""
    FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO
    E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE
    E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
"""
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa é: {math.hypot(co,ca)}')
