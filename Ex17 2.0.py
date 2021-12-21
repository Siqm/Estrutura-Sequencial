# Faça um Programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math


def pede_area():  # Função pede a area e cria folga de 10%
    area = float(input('Insira a area que quer pintar: '))
    area += area * 0.1
    return area


def calcula_qtd_latas18(area):  # retorna qtd de latas grandes necessárias
    qtd_latas18 = (1 / 6 * area) / 18
    return math.ceil(qtd_latas18)


def calcula_qtd_latas3(area):  # retorna qtd de latas pequenas necessárias
    qtd_latas3 = (1 / 6 * area) / 3.6
    return math.ceil(qtd_latas3)


def calcula_qtd_economia(area):  # retorna qtd de latas grandes e pequenas necessárias
    mtquad = area
    acumulador = 0

    while mtquad >= 108:
        acumulador += 108
        mtquad -= 108

    qtd18 = (1 / 6 * acumulador) / 18
    qtd3 = (1 / 6 * mtquad) / 3.6

    return math.ceil(qtd3), math.ceil(qtd18)


def main():
    area = pede_area()
    qtd18 = calcula_qtd_latas18(area)
    qtd3 = calcula_qtd_latas3(area)

    valor_latas_g = qtd18 * 80
    valor_latas_p = qtd3 * 25

    print(f'\nA quantidade necessária para pintar {area}m² (area+10%) é de {qtd18} Latas de 18L')
    print(f'O preço de custo destas latas é de {valor_latas_g}')
    print('*************************************************************************\n')
    print(f'A quantidade necessária para pintar {area}m² (area+10%) é de {qtd3} Latas de 3,6L')
    print(f'O preço de custo destas latas é de {valor_latas_p}')
    print('*************************************************************************\n')

    qtd3, qtd18 = calcula_qtd_economia(area)
    valor = qtd3*25 + qtd18*80
    
    print(f'A quantidade necessária para pintar {area}m² (area+10%) usando latas')
    print(f'pequenas e latas grandes é respectivamente:')
    print(f'{float(qtd3)} latas pequenas e {qtd18} latas grandes, com total de R${valor}')


if __name__ == '__main__':
    main()
