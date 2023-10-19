# 1. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

r1 = int(input('Digite um valor de número inteiro: '))
r2 = int(input('Digite um valor de número inteiro: '))
real = float(input('Digite um valor de número real: '))

valor1 = 2 * r1
valor2 = r2 / 2
print(f'Resposta(a): Os valores são {valor1} e {valor2}')

valor3 = 3 * r1 + real
print(f'Resposta(b): O valor é {valor3}')

valor4 = real ** 3
print(f'Resposta(c): O valor é {valor4}')
