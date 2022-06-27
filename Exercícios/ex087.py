matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par = matriz[l][c] + par
        if c == 2:
            soma = matriz[l][c] + soma
        if l == 1:
            maior = matriz[l][c] + maior
print('-='*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
print(f'A soma dos números pares digitados é : {par}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')