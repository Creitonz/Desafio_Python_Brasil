# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# (A = π r²)

raio = int(input('Informe o valor do raio: '))
pi = float(3.14)
a = pi * raio**2

print(f'A área do circulo com raio de {raio} é igual a: {a}')