from typing import Text


frase = str(input('Digite uma frase: ').strip().upper())
frase = frase.replace(' ', '')
contrario = Text(frase[::-1])
print (f'A frase {frase.capitalize()} ao contrário fica {contrario.capitalize()}')
if frase == contrario:
    print('E ela é um palíndromo.')
else:
    print('Ela não é um palíndromo')