from pickle import APPEND


lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input('digite um valor:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Os valores digitados foram {lista}!!\nO maior valor digitado foi {(maior)} e está na posição ', end='')
for posmax, lis in enumerate(lista):
    if lis == maior:
        print(f'{posmax+1}...',end='')
print(f'\nO menor valor digita foi {menor} e está na  posição ',end='')
for posmin , lis in enumerate(lista):
    if lis == menor:
        print(f'{posmin+1}...',end='')