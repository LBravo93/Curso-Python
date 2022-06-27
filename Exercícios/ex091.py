from operator import itemgetter
from time import sleep
from random import randint
jogo = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1,6),}
for j, n in jogo.items():
    print(f'O {j} tirou: {n}')
    sleep(0.5)
sleep(2)
print('*'*30)
print(f'{"== Resultado == ":^25}')
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print(f'{i+1}° lugar: {j[0]} com {j[1]}.')
    sleep(0.5)