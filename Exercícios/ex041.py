from datetime import date, datetime
nasc = int(input('''Bom Dia atléta!!
Digite o ano de seu nascimento:
''').strip())
ano_atual = date.today().year
idade = ano_atual - nasc
if idade < 10:
    print(f'Você tem {idade} anos, portanto é um atléta MIRIM.')
elif idade < 15:
    print(f'Você tem {idade} ano, portanto é um atléta INFANTIL.')
elif idade < 20:
    print(f'Você tem {idade} ano, portanto é um atleta JUNIOR.')
elif idade < 26:
    print(f'Você tem {idade} ano, portanto é um atleta SENIOR.')
elif idade < 100:
    print(f'Você tem {idade}, portanto é um atléta MASTER.')
else:
    print(f'Você tem {idade} anos, e sinceramente deveria estar morto.')