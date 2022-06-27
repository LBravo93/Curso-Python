from datetime import date
ano = int(input('Digite o ano que deseja analisar:\n(Digite 0 para analisar o ano atual)\n'))
if ano == 0:
    ano = date.today().timetuple
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))