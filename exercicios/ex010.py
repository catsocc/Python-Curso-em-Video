"""
    CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA
    TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR

    CONSIDERE: US$1,00 = R$5,89 (11/04/2025)
"""
n = float(input('Digite o valor da carteira em reais: '))
print(f'Você possui: R${n:.2f}.\nO valor convertido em doláres fica: US${n/5.89:.2f}.')
