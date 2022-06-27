lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1º: '))
    nota2 = float(input('nota 2º: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar?[S/N]'))
    if r in 'nN':
        break
print(lista)
print(f'{"Num.":<4}{"Nome":<10}{"Média":>8}')
print('='*20)
for i, a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')