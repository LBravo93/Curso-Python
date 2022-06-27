num = int(input('Digito o número no qual quer saber a tabuada: \n').strip())
for c in range(0 , 11):
    print(f'{num:.0f} x {c:.0f} = {num*c:.0f}')