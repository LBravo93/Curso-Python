from time import sleep
print('Contador de PA (Progressão Aritimética): ')
sleep(1)
primeiro = int(input('Digite o primeiro termo: \n').strip())
razao = int(input('Digite a Razão: \n').strip())
contador = 1
contador_total = 0
if primeiro >= 0:
    while primeiro > 0:
        while contador <=  10:
            print(f'{primeiro}', end='')
            primeiro = primeiro + razao
            contador = contador + 1
            contador_total = contador_total + 1
            if contador == 11:
                print (' PAUSA ', end='')
            else:
                print(' -> ', end='')
        termo = int(input('\nQuantos termos você quer mostrar a mais? ').strip())
        contador = contador - termo
        if termo == 0:
            primeiro = -1
            print(f'Finalizando programa com {contador_total} termos mostrados.')