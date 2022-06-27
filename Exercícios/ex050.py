soma = 0
cont = 0
for c in range(1, 7):
    c = int(input(f'Digite o {c}° número que deseja somar:').strip())
    if c % 2 == 0:
        pares = c
        soma = c + soma
        cont = cont + 1
print (f'Você digitou {cont} números pares, e a soma deles é: {soma}.')