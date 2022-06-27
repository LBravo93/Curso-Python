a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print(f'Os segmentos {a}, {b} e {c} formam um triângulo. E ele é EQUILATERO.')
    elif a != b == c or a == b != c or c == a != b:
        print(f'Os segmentos {a}, {b} e {c} formam um triângulo. E ele é ISÓSCELES.')
    elif a != b != c != a:
        print(f'Os segmentos {a}, {b} e {c} formam um triângulo. E ele é ESCALENO.')
else:
    print(f'Os segmentos {a:.2f}, {b:.2f}, {c:.2f}, não podem formar um triângulo.')