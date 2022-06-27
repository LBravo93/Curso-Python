contador = 0
num = int(input('Digite um número: '))
for c in range(1 , num+1):
    if num % c == 0:
        print('\033[34m', end='')
        contador = contador + 1
    else:
        print('\033[31m', end='')
    print(f'{c}\033[m', end=' ')
if contador == 2:
    print(f'\nO número {num} foi divido {contador} vezes e é um número PRIMO.')
else:
    print(f'\nO número {num} foi divido {contador} vezes e não é um número PRIMO.')