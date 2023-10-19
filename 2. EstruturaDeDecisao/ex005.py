# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

calculo = (nota1 + nota2) / 2
print(calculo)

if calculo >= 7:
    print('Parabéns você foi APROVADO!')
elif calculo < 7:
    print('Parabéns você foi REPROVADOR!')
elif calculo == 10:
    print('Parabéns você foi APROVADO COM DISTINÇÃO!')
else:
    print('Por favor, digite um número de 0 a 10.')