numero = int(input('Digite um número (PRESS 999 PARA SAIR): \n').strip())
contador =  soma = 0
while numero != 999:
    contador = contador + 1
    soma = soma + numero
    numero = int(input('Digite um número: \n').strip())
print(f'Você digitou {contador} números, e a soma deles é {soma}.')