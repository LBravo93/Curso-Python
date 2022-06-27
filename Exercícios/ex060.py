from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: \n').strip())
fatorial = numero
while fatorial > 0:
    print(fatorial, end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    fatorial -= 1
print(factorial(numero))