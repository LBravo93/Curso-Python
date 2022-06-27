numero = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou o {numero}')
if 9 in numero:
    print(f'O Valor 9 apareceu {numero.count(9)} vezes.')
else:
    print('Não foi digitado o valor 9.')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}º posição.')
else:
    print('Não foi digitado o valor 3.')
print('Os valores pares digitados foram: ', end='')
for c in numero:
    if c % 2 ==0:
        print(c, end=', ')