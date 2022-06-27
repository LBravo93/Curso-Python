total = [[], []]
for n in range(0,7):
    parc = int(input('Digite um valor: '))
    if parc % 2 == 0:
        total[0].append(parc)
    elif parc % 1 == 0:
        total[1].append(parc)
print(f'Os valores pares digitados são: {sorted(total[0])}')
print(f'Os valores Ímpares digitados foram: {sorted(total[1])}')