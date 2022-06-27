termo = int(input('Primeiro termo: ').strip())
razao = int(input('Razão: '))
decimo = termo + 10 * razao
for c in range(termo, decimo, razao):
    print (c, end=' -> ')
print('Acabou!!!')