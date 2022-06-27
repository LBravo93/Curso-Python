n = int(input('Digite um número: '))
n1 = n % 2
if n1 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))