listatot = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um valor: '))
    listatot.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    res = input('Deseja continuar?[S/N]').upper().capitalize()
    if res == 'N':
        break
    elif 'S' not in res:
        print('Digite S para Sim, ou N para Não!!!')
        res = input('Deseja continuar?[S/N]').upper().capitalize()
print(f'A lista total de valores digitados é: {listatot}')
print(f'A lista de números pares digitados é: {listapar}')
print(f'A lista de mumeros ímpares digitados é: {listaimpar}')