"""FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO
E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS
INFORMAÇÕES POSSÍVEIS SOBRE ELA"""

x = input('Digite algo: ')
print('Você digitou algum número?')
print(x.isalnum())
print('Você digitou alguma letra?')
print(x.isalpha())