numero = int(input('Quantos termos você quer ver? \n').strip())
contador = 3
primeiro = 0
segundo = 1
print(f'{primeiro} -> {segundo} -> ', end='')
while contador <= numero:
    terceiro = primeiro + segundo
    print(f'{terceiro}', end='')
    primeiro = segundo
    segundo = terceiro
    contador = contador + 1
    if contador == numero + 1:
        print('. FIM!!!', end='')
    else:
        print(' -> ', end='')