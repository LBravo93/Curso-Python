n = int(input('Digite um número com no máximo 4 dígitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {}: '.format(n))
print("A unidade é {}".format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))