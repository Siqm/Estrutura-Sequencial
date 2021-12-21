#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
x = 0.0
for i in range(0,4):
    x += float(input(f'Insira a nota {i+1}: '))
print(f'A média é de {x/4}')