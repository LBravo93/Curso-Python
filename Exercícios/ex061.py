print('Contador de PA: ')
primeiro = int(input('Digite o primeiro termo: \n').strip())
razão = int(input('Digite a razão: \n').strip())
cont = 1
while cont <= 10:
    print(f'{primeiro}', end='')
    primeiro = primeiro + razão
    cont = cont + 1
    if cont < 11:
        print(' -> ', end='')
    else:
        print(' = ', end='')
print('FIM!!!')