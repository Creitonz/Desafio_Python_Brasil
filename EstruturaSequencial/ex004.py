# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Descubra a média das suas notas bimestrais')

nb1 = float(input('Fale a nota do seu 1 Bimestre: '))
nb2 = float(input('Fale a nota do seu 2 Bimestre: '))
nb3 = float(input('Fale a nota do seu 3 Bimestre: '))
nb4 = float(input('Fale a nota do seu 4 Bimestre: '))

media = (nb1 + nb2 + nb3 + nb4) / 4

print(f'Sua média é: {media}')