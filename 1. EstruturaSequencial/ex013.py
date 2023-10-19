# 1. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#     a) Para homens: (72.7*h) - 58
#     b) Para mulheres: (62.1*h) - 44.7

h = float(input('Digite a sua altura em metros: '))

peso_homem = (72.7 * h) - 58
peso_mulher = (62.1 * h) - 44.7

print(f'Resposta(a): Seu peso ideal é: {peso_homem} se for biologicamente Homem')
print(f'Resposta(b): Seu peso ideal é: {peso_mulher} se for biologicamente Mulher')