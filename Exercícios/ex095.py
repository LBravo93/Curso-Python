indi = 1
time = []
jogador = {}
gol = []
gtotal = 0
r = ''
timenome = str(input('Digite o nome do time: ')).capitalize().strip()
while True:
    jogador['nome'] = str(input('Digite o nome do jogador:  ')).capitalize().strip()
    jogador['total de jogos'] = int(input(f'    Digite o numero de jogos que o jogador {jogador["nome"]} participou:  ').strip())
    gol.clear()
    gtotal = 0
    for c in range(0, jogador['total de jogos']):
        gol2 = int(input(f'    Digite quantos gols o {jogador["nome"].capitalize()} fez no jogo {c+1}:  ').strip())
        gol.append(gol2)
        gtotal = gtotal + gol2
    jogador['gol por partida'] = gol.copy()
    jogador['total de gols'] = gtotal
    jogador['média'] = float((f'{gtotal / jogador["total de jogos"]:.2f}'))
    time.append(jogador.copy())
    jogador.clear()
    while True:
        r = str(input('Deseja continuar cadastrando [S/N]? ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('Digite apenas S ou N.')
    if r == 'N':
        break
    

print('-='*15,f'TIME: {timenome.upper()}','-='*15)
print('=-'*35)
print(f'{"Cod Nome":<15}{"Partidas":<15}{"G/Partida":<15}{"G/Totais":<15}{"G/Média":<15}')
print('=-'*35)
for pos, j in enumerate(time):
    print(f'{pos+1}-',end='')
    for v in j.values():
        print(f'{str(v):<15}',end='')
    print()
print('=-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador?[0 para finalizar] ').strip())
    if busca <=0:
        print('!!!PROGRAMA FINALIZADO!!!')
        break
    if busca >= len(time)+1:
        print(f'Erro, Jogador com código {busca} não existe.')
    else:
        print(f'Dados do jogador: {time[busca-1]["nome"]}')
        for pos, g in enumerate(time[busca-1]['gol por partida']):
            print(f'    No jogo {pos+1} fez {g} gols.')