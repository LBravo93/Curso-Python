from time import sleep
from random import randint
numeros = []
ini = fim  = 0

def sorteia(a,b): 
    for c in range (0,5):
        rand = randint(a,b)
        sleep(0.2)
        print(f'{rand}, ',end='',flush=True)
        numeros.append(rand)
    numeros.sort()
    print()
    print('-='*30)
    

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor

    print(soma)

ini = int(input('Digite o início: '))
fim = int(input('Digite o Fim: '))
sorteia(ini,fim)
print('-='*30)

somaPar(numeros)
