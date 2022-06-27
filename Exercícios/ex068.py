from random import randint
v = 0
while True:
    jogador = int(input('Digite um número:\n'))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper() [0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print ('VOCÊ VENCEU!!!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!!')
            V = V + 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER... Você venceu {v} vezes')