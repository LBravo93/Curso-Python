a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro número: '))
menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número digitedo foi: {}.'.format(menor))
print('O maior número digitado foi: {}.'.format(maior))