from time import sleep


def contagem(a, b, c):
    if c <0:
        c = c*-1
    if c == 0:
        c = 1

    print(f'Contagem de {a} até {b} pulando de {c} em {c}')
    
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ',end='',flush=True)
            sleep(0.2)
            cont = cont + c
        print('FIM!!!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ',end='', flush=True)
            sleep(0.2)
            cont = cont - c
        print('FIM!!!')

    
contagem(1, 10, 1)
contagem(10, 0, 2)
i = int(input('Agora é sua de de personalizar a contagem!!!\nInício: '))
t = int(input('Término: '))
p = int(input('Passo: '))
contagem(i, t , p)