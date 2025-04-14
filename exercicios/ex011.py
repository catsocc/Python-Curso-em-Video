"""
    FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA
    DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A
    QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA,
    SABENDO QUE CADA LITRO DE TINTA PINTA 2m²
"""
l = float(input('Digite a largura da parede: (em metros)'))
a = float(input('Digite a altura: (em metros)'))
area = l*a
print(f'A área da parede é de : {area}m.\nSeria necessário para pintar a parede considerando que cada litro cobre 2m² um total de: {area/2} litros.')

