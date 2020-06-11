class colors:
    blue = '\033[34m'
    yellow = '\033[33m'
    red = '\033[31m'
    std = '\033[m'

from random import randint
from time import sleep
#valor das apostas da MegaSena
Ljogo = [15, 22522.5, 14 , 13515.5 , 13 , 7722, 12 , 4178 , 11 , 2079 , 10 , 945, 9 , 378, 8 , 126, 7 , 31.5 , 6 , 4.5] 
contjogo = 0 #contador qtd de Jogos
contpos = 1 #contador da posição na lista
### Coleta das informações para execução do programa
valbolao = float(input('Digite o valor arrecadado no bolão: R$'))
qtdcotas = int(input('Informe a qtd de cotas: '))
valpremio = float(input('Informe o valor do prêmio: R$'))
#Frescura para fingir que o programa está demorando para calcular
print(f'{colors.red}PROCESSANDO{colors.std}')
sleep(2)

while True:
    #verificar quantos jogos podem ser feitos com o valor disponível
    while valbolao > Ljogo[contpos]:
        valbolao = valbolao - Ljogo[contpos]
        contjogo += 1
    #imprimir a quantidade de jogos que podem ser feitos
    if contjogo > 0:
        print(f'{colors.blue}Será possível fazer {contjogo} jogo(s) de {Ljogo[contpos-1]} números{colors.std}')

    qtdnum = Ljogo[contpos-1]
    #Sortear e imprimir os números
    for count in range (0,contjogo):
            result =[] #cria uma lista chamada Result
            while len(result) < qtdnum: #verifica se a qtd de intens na lista é menor que a qtd de números escolhidas
                    pensanum = randint(1,60) #escolhe um número aleatório de 1 ate 60
                    if pensanum not in result: #Verifica se o número escolhido não está na lista
                            print(f'{colors.yellow}{pensanum}', end = ' ') #imprime o número
                            result.append(pensanum) #adiciona o número na lista
            print(f'\n{colors.std}')

    contjogo = 0
    # Se o saldo do valor do bolão for menor que o jogo de 6 números ele interrompe  o looping
    if valbolao < Ljogo[-1]:
        print(f'Ainda sobrou R${valbolao:.2f}')
        break
    # caso contrarário segue o programa
    else:
        contpos += 2

print(f'{colors.yellow}O valor do prêmio por cota será de R${valpremio/qtdcotas:.2f}{colors.std}')