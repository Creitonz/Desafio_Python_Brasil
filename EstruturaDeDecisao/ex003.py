# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Qual seu sexo biológico? [F]eminino ou [M]asculino: ')

if sexo == 'F' or sexo == 'f':
    print('Bem Vinda :)')
elif sexo == 'M' or sexo == 'm':
    print('Bem vindo :)')
else:
    print('Sexo Inválido, Por favor digite F para feminino ou M para masculino')