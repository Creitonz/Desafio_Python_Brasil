# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da Internet em Mbps: '))

velocidade_mbps = velocidade / 8
tempo = arquivo_tamanho / velocidade_mbps
converter = tempo / 60
tempo_segundos = tempo
print(f'Irá demorar: {converter:.2f} minutos')
print(f'Irá demorar: {tempo_segundos:.2f} segundos')