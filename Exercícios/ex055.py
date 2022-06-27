pesomaior = 0
pesomenor = 0
for pessoas in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if pessoas == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        elif peso < pesomenor:
            pesomenor = peso
print(f'O Maior peso registrado é {pesomaior}')
print(f'O menor peso registrado é {pesomenor}')