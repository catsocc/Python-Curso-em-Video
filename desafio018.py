"""
    FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE
    NA TELA O VALOR DO SENO, COSSENO E TANGENTE DE ÂNGULO.
"""
import math

angulo = float(input('Digite um ângulo qualquer: '))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f'O ângulo {angulo}°, possui seno de {seno}, cosseno de {cosseno} e tangente de: {tangente}')
