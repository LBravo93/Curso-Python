from random import randint
from time import sleep

from modulo_cores import *

num = []
prov = []
print('-'*30)
print('         MEGA SENA       ')
print('-'*30)
resposta = input(amarelo('Olá!!!! Digite seu nome: \n')).upper()
quant = int(input(amarelo('Digite o número de jogos que deseja fazer: ')))
for c in range(0, quant):
    for j in range(0, 6):
        val = randint(1, 60)
        while val in prov:
            val = randint(1, 60)
        prov.append(val)

    num.append(prov[:])
    prov.clear()
if quant <= 0:
    print(vermelho(
        f'O usuário {resposta.lower().capitalize()} não quis fazer jogo nenhum!!'))
if quant == 1:
    print('-='*15)
    print(amarelo('Seu jogo é: '))
    for c in range(0, quant):
        print(verde(f'Jogo {c+1}: {sorted(num[c])}'))
        sleep(.5)
    print('-='*15)
else:
    print('-='*15)
    print(amarelo('Seus jogos são: '))
    for c in range(0, quant):
        print(verde(f'Jogo {c+1}: {sorted(num[c])}'))
        sleep(.5)
    print('-='*15)
if quant >= 1:
    if resposta == 'LIDIO':
        print('BOA SORTE LIDIÃO, VAMOS FICAR RICO PORRAAA!!!!')
    if resposta == 'ALINE':
        print('BOA SORTE ALINE, DEIXA O LIDIO RICO. UHUUUL!!!!')
    elif resposta not in 'LIDIOALINE':
        print(
            f'{resposta}, melhor o LIDIO ou a ALINE saber que você está aqui, porquê eu vou contar!!!')
