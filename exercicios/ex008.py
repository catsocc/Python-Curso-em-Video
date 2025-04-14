"""
    ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS
    E O EXIBA CONVERTIDO EM CENTÍMETRO E MILÍMETROS
    1 m = 100cm     1m = 1000mm
"""
n = float(input('Digite um valor em metros para conversão em centímetros e milímetros:\n'))
print(f'O valor digitado foi de: {n}m.\nO valor equivale a: {n*100}cm, e {n*1000}mm.\n')
