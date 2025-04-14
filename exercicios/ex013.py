"""
    FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM
    FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM
    15% DE AUMENTO.
"""

v = float(input('Digite o salário:' ))
print(f'O aumento ficou em: R${v*(15/100)}O novo salário com aumento fica: R${v+(v*(15/100)):.2f}')
