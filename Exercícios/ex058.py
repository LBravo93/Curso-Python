import random
from time import sleep
aleatorio = random.randint(0, 10)
contador = 1
n1 = int(input('''Sou seu computador!!! Tente advinhar qual número pensei. Digite um número de 0 a 10: ''').strip())

while n1 != aleatorio:
    contador = contador + 1
    if n1 != aleatorio:
        n1 = int(input('Não foi dessa vez, tente novamente: ').strip())

print('PROCESSANDO...')
sleep(2)
print(f'''PARABÉNS! Você conseguiu advinhar o número e venceu essa!
E precisou de {contador} tentativas''')