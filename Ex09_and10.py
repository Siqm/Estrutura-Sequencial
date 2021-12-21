# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

# 10 - Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

def cTof(temp):
    temp = (temp*9/5) + 32
    print(f'O resultado é: {temp}')

def fToc(temp):
    temp = (temp-32) * 5/9
    print(f'O resultado é: {temp}')

def programa():
    resp = input('Deseja transformar Celsius para Fahrenheit (1) ou Fahrenheit para Celsius (2): ')
    temperatura = float(input('Insira a temperatura: '))
    if resp == '1':
        cTof(temperatura)
    else:
         fToc(temperatura)

if __name__ == '__main__':
    programa()