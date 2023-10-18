# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero < 0:
    print('Seu número é NEGATIVO')
elif numero > 0:
    print('Seu número é POSITIVO')
else:
    print('Por favor, digite um número diferente de 0')