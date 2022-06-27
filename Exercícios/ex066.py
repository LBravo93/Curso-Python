soma = 0
cont = 0
while True:
    numero = int(input('Digite um número (999 para encerrar): \n'))
    if numero == 999:
        break
    soma = soma + numero
    cont = cont + 1
print(f'Você digitou {cont} números e a soma entre eles é de {soma} !!!')