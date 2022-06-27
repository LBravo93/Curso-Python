import datetime
nasc = int(input('Digite o ano de seu nascimento: '))
data_atual = datetime.datetime.today()
data_ano = data_atual.year
idade = data_ano - nasc
if idade < 18:
    idade1 = 18 - idade
    print('Ainda não precisa se aliastar pois tem {} anos, terá que voltar daqui a {} anos.'.format(idade, idade1))
elif idade > 18 :
    idade1 = idade - 18
    print('Você tem {} anos, deveria ter ido a {} anos atras.'.format(idade, idade1))
else:
    print('Você terá que se alistar esse ano, pois ja tem {} anos'.format(idade))