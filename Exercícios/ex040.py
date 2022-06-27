nota_1 = float(input('Digite a primeira nota: ').strip())
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
if media < 5.0:
    print('Você tirou {} e está REPROVADO.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Você tirou {}, está de recuperação.'.format(media))
elif media > 7.0:
    print('Parabéns, você tirou {} e foi aprovado.'.format(media))
#elif nota_1 > 10.0 or nota_2 > 10.0:
#    print('Você digitou uma nota inválida. Por favor digite uma nota de 0 a 10.') mesmo problema do ex028.