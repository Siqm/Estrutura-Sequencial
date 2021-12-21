# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B -  a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

def programa():
    num1 = int(input('Insira um número inteiro: '))
    num2 = int(input('Insira um número inteiro: '))
    num3 = float(input('Insira um número real: '))
    A(num1, num2)
    B(num1, num3)
    C(num3)

def A(n1, n2):
    resultado = (n1 * 2) * (n2 / 2)
    print(resultado)


def B(n1, n3):
    resultado = (3 * n1) + n3
    print(resultado)


def C(n3):
    print(n3 ** 2)

if __name__ == '__main__':
    programa()