# Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite um número inteiro: '))

if numero1 > numero2:
    print(f'Número {numero1} é maior que {numero2}')
elif numero2 > numero1:
    print(f'Número {numero2} é maior que {numero1}')