resposta = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
if resposta == 'S':
    while resposta == 'S':
        numero = int(input('Digite um número: \n').strip())
        soma = soma + numero
        contador = contador + 1
        if contador == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero
        resposta = str(input('Quer continuar?[S/N]\n')).strip().upper()[0]
    print(f'Você digitou {contador} números, a média deles é {soma/contador:.1f}. O maior número digitado foi {maior} e o menor foi {menor}.')
    print('ACABOU!!!')
else:
    print('Você digitou uma resposta inválida!! Por favor reinicie o programa, e responda com "S" ou "N".')