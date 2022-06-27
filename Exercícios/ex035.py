a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a:.2f}, {b:.2f}, {c:.2f}, podem formar um triângulo.')
else:
    print(f'Os segmentos {a:.2f}, {b:.2f}, {c:.2f}, não podem formar um triângulo.')