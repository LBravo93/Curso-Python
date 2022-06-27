import modulo_cores

'---------------------NUMEROS---------------------'


def fatorial(n=0, cash=False):
    f = 1
    for c in range(1, n+1):
        f = f * c
    res = f
    return res if cash is False else moeda(res)


def dobro(n=0, cash=False):
    res = n * 2
    return res if cash is False else moeda(res)


def triplo(n=0, cash=False):
    res = n * 3
    return res if cash is False else moeda(res)


def metade(n=0, cash=False):
    res = n / 2
    return res if cash is False else moeda(res)


def centomais(n=0, percento=0, cash=False):
    res = ((n / 100) * percento) + n
    return res if cash is False else moeda(res)


def centomenos(n=0, percento=0, cash=False):
    res = n - ((n / 100) * percento)
    return res if cash is False else moeda(res)


def moeda(n=0):
    res = f'{n:.2f}'.replace('.', ',')
    return res


def resumonum(n=0, mais=0, menos=0):
    print(f'-'*30)
    print(f'{                 "RESUMO DO VALOR"}')
    print(f'-'*30)
    print(f'Preço analisado:    R${moeda(n)}')
    print(f'Dobro do preço:     R${dobro(n, True)}')
    print(f'Metade do preço:    R${metade(n, True)}')
    print(f'{mais}% de aumento:     R${centomais(n, mais, True)}')
    print(f'{menos}% de redução:     R${centomenos(n, menos, True)}')


def leiaint(msg=0):
    while True:
        try:
            n = int(input(msg).strip())
        except(TypeError, ValueError):
            print(modulo_cores.vermelho(f'ERRO: O valor digitado não é um número inteiro!!'))
            continue
        except(KeyboardInterrupt):
            print(modulo_cores.vermelho(
                '\nO usuário interrompeu o programa. \nTente Novamente!!'))
            continue

        else:
            return n


def leiafloat(msg=0):
    while True:
        try:
            n = float(input(msg).strip().replace(',', '.'))
        except(TypeError, ValueError):
            print(modulo_cores.vermelho(f'ERRO: O valor digitado não é um número inteiro!!'))
            continue
        except(KeyboardInterrupt):
            print(modulo_cores.vermelho('ERRO: Valor não informado.'))
            break
        else:
            return n
