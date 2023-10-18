# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#--------------------       Precisei da ajuda de I.A nessa atividade         ------------------------------------------------------------------------

metros_quadrado = float(input('Informe a área em metros quadrados: '))
lata = 18
litros_por_metros = 3

litros_necessario = metros_quadrado / litros_por_metros

latas_necessaria = int(litros_necessario / lata)
if litros_necessario % lata != 0:
    latas_necessaria += 1

valor = latas_necessaria * 80


print(f'Você precisará de {latas_necessaria} latas de tinta, custando {valor}')