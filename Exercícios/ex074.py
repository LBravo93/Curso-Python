from random import randint
#maior = 0
#menor = 999
numero = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
print(f'Eu sorteei os valores:', end='')
for c in numero:
    print(f' {c}', end='')
#   if c >= maior:
#       maior = c
#    if c <= menor:
#        menor = c
print(f'\no maior número foi {max(numero)}.\nO menor número foi {min(numero)}')
