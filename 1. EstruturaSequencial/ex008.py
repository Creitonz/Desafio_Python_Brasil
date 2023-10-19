# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hrs_trabalhada = int(input('Quanto você ganha por horas trabalhada? '))
hrs_mes = int(input('Quanto de horas você trabalhou no mês? '))

total = hrs_trabalhada * hrs_mes 

print(f'Você ira receber pelo trabalho: {total}')