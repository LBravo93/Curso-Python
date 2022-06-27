expressao = str(input('Digite uma expressão: '))
lista=[]
for caractere in expressao:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida!!!')
else:
    print('Sua expressão é inválida!!!')