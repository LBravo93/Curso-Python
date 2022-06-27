lista = []
pessoas = []
mais = 0
menos = 0
while True:
    lista.append(input('Digite o nome: '))
    lista.append(input('Digite o peso: '))

    if len(pessoas) == 0:
        mais = lista[1]
        menos = lista[1]
    else:
        if lista[1] > menos:
            mais = lista[1]
        elif lista[1] < mais:
            menos = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    r = input('Deseja continuar?[S/N]').upper().capitalize()
    if r == 'N':
        break
    
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} Pessoas.')
print(f'As pessoas mais pesadas tem {mais} kg, e são: ',end='')
for p in pessoas:
    if p[1] == mais:
        print(f'{p[0]}, ',end='')
print()
print(f'As pessoas mais leves tem {menos} kg, e são: ',end='')
for p in pessoas:
    if p[1] == menos:
        print(f'{p[0]}, ',end='')