contador = 0
while True:
    numero = int(input('Quer ver a tabuada de qual número? \n').split())
    while contador < 10:
        contador = contador + 1
        tabuada = numero * contador
        print(f'{numero} x {contador} = {tabuada}')
    contador = 0
    if numero <= 0:
         break
print('\nPrograma encerrado!!!\n')