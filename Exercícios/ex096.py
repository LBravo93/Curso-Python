def area(a,b):
    t= a * b
    print(f'A área de um terreno {a:.2f}x{b:.2f} é de {t:.2f}m²')
    print('---'*15)


print('CONTROLE DE TERRENOS')
print('---'*15)
c = float(input('comprimento (m): ').strip())
l = float(input('Largura (m): '))
area(c,l)