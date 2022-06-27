def ficha(n=0,g=0):
    '''
    n = Nome do jogador
    g = Número de gols
    se algum parâmetro não for preenchido, será completo por "desconhecido"
    '''
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n == '':
        n = '<desconhecido>'
    print('-='*30)
    print(f'O jogador {n} fez {g} gols!!')


print('-='*10,'CADASTRO DE JOGADORES','=-'*10)
a = str(input('Digite o nome: ')).capitalize().strip()
b = str(input('Digite o número de gols: ')).strip()
ficha(a,b)
