jogador = {}
gol = []
gtotal = 0
jogador['nome'] = str(input('Digite o nome do jogador:  '))
jogador['total de jogos'] = int(input(f'Digite o numero de jogos que o jogador {jogador["nome"]} participou:  '))
for c in range(0, jogador['total de jogos']):
    gol2 = int(input(f'Digite quantos gols o {jogador["nome"].capitalize()} fez no jogo {c+1}:  '))
    gtotal = gtotal + gol2
    gol.append(gol2)
jogador['gol por partida'] = gol.copy()
jogador['total de gols'] = gtotal
jogador['média'] = float((f'{gtotal / jogador["total de jogos"]:.2f}'))
print(jogador)
print('=-'*40)
for c, i in jogador.items():
    print(f'O campo {c} tem valor {i}.')
for c, g in enumerate(jogador['gol por partida']):
    print(f'Na partida {c+1} fez {g}')