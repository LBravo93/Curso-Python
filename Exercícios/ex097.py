def escreva(msg):
    print('-'*len(msg)+'----')
    print(f'  {msg}')
    print('-'*len(msg)+'----')
    print()
for c in range (0,3):
    escreva(str(input('Digite uma mensagem: ')))
