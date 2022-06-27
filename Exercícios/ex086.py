matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}]'))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()