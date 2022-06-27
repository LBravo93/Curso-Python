import random
from time import sleep
aleatorio = random.randint(0, 5)
n1 = int(input('Qual número pensei? digite um número de 0 a 5: '))

if n1 == aleatorio:
    print('PROCESSANDO...')
    sleep(2)
    print('PARABÉNS! Você conseguiu advinhar o número e venceu essa!')
#elif n1 < 0 or n1 > 5:
#    print('PROCESSANDO...')
#   sleep(2)
#    print('Você não digitou um número de 1 a 5. Perdeu playboy!!')#  Não consigo fazer esse bloco funcionar
elif n1 != aleatorio:
    print('PROCESSANDO...')
    sleep(2)
    print('GANHEI!! O número que pensei foi {}'.format(aleatorio))