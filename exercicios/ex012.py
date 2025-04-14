"""
    FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO
    E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO
"""
p = 0
try:
    p = float(input('Digite o preço do produto: '))
except ValueError:
    print('Por favor, insira um valor númerico válido')
desconto = p*(5/100)
print(f'O desconto de 5% fica no valor de R${desconto:.2f}.\nNovo preço do produto R${p-desconto:.2f}')

