print('Escolha abaixo uma opção para converter o número desejado.')
escolha = int(input('[ 1 ] Converter para binário\n[ 2 ] Converter para octal\n[ 3 ] converter para hexadecimal\nDigite sua opção: '))
n1 = int(input('Digite um número: '))
if escolha == 1:
    print('Você escolheu a opção 1, o número {} convertida para binário é {}.'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('Você escolheu a opção 2, o número {} convertido para octal é {}'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('Você escolheu a opção 3, o número {} convertido para hexadecimal é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção inválida, tente novamente.')