# Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

def pede_area():
    area = input(('Insira a area que quer pintar: '))
    area = float(area)
    return area

def calcula_qtd_latas(area):
    qtd_latas = (1/3 * area)/18
    qtd_latas = math.ceil(qtd_latas)
    # calcula preço:
    preco = qtd_latas * 80
    return qtd_latas, preco

def main():
    area = pede_area()
    qtd_latas, preco = calcula_qtd_latas(area)
    print(f'A quantidade de latas necessárias é de: {qtd_latas}')
    print(f'O preço total é de R${preco}')

if __name__ == '__main__':
    main()