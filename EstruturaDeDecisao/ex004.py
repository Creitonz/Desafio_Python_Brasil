# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

resposta = input('Digite UMA letra: ').upper()

vogal = ['A', 'E', 'I', 'O', 'U']
consoante = 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z'

if resposta in vogal:
    print('A letra que você digitou é uma: Vogal')
elif resposta in consoante:
    print('A letra que você digitou é uma: Consoante')
else:
    print('Infelizmente deu um erro, tente digitar apenas UMA letra que exista no alfábeto')
