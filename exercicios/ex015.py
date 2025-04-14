"""
    ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO
    POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
    CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA
    E R$0,15 POR KM RODADOS.
"""
t = int(input('Quantos dias alugados? '))
d = float(input('Quantos km foram rodados? '))
v = (60 * t) + (d * 0.15)
print(f'O total a pagar é de R${v}')
