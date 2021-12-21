# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,

# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

def programa():
    hora = float(input('Insira quanto você ganha por hora: '))
    qtd_horas = int(input('Insira a quantidade de horas trabalhadas: '))
    total = bruto(hora, qtd_horas)
    ir = IR(total)
    inss = INSS(total)
    sind = sindicato(total)

    print(f'+ Salário Bruto: R$: {total}')
    print(f'- IR(11 %): R$ {ir}')
    print(f'- INSS(8 %): R$ {inss}')
    print(f'- Sindicato(5 %): R$ {sind}')
    print(f'= Salário Liquido: R$ {total-ir-inss-sind}')


def bruto(hr, qh):
    total = hr * qh
    return total

def IR(sal_bruto):
    ir = sal_bruto * 0.11
    return ir

def sindicato(total):
    sind = total * 0.05
    return sind

def INSS(total):
    inss = total * 0.08
    return inss

if __name__ == '__main__':
    programa()