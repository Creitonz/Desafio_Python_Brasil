# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_horas = float(input('Quanto você ganha por hora? '))
horas_trabalhada = float(input('Quanto você trabalhalhou no mês? '))
valor_bruto = valor_horas * horas_trabalhada
inss = 8
ir = 11
sindicato = 5

desconto_inss = valor_bruto - (valor_bruto * inss / 100)
desconto_ir = valor_bruto - (valor_bruto * ir / 100)
desconto_sindicato = valor_bruto - (valor_bruto * sindicato / 100)

print(f'Valor bruto do mês foi: {valor_bruto:.2f}')

pg_inss = valor_bruto - desconto_inss
print(f'Valor pago ao INSS foi: {pg_inss:.2f}')
pg_ir = valor_bruto - desconto_ir
print(f'Valor pago ao Imposto de Renda foi: {pg_ir:.2f}')
pg_sindicato = valor_bruto - desconto_sindicato
print(f'O Valor pago ao Sindicato foi: {pg_sindicato:.2f}')

descontos = pg_inss + pg_ir + pg_sindicato
valor_liquido = valor_bruto - descontos
print(f'O valor liquido foi de: {valor_liquido:.2f}')