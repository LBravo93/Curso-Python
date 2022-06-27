from glob import glob


n = 0
def leiaint(a):
    global n
    while True:
        if a.isalpha() or a == '':
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            a = input('Digite um número: ')
        elif a.isnumeric():
            return a


n = (leiaint(input('Digite um número: ')).strip())
print(f'Você acabou de digitar o numero {n}')