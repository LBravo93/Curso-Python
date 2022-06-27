from operator import index
from textwrap import indent


time = ('Palmeiras' , 'Athletico' , 'Atlético - GO' , 'Atlético - MG' , 'Avaí' , 'Botafogo' , 'Ceará' , 'Cortinthian' , 'Coritiba' , 'Cuiabá' , 'Flamerda' , 'Fluminense' , 'Fortaleza' ,
'Goiás' , 'Internacional' , 'Juventude' , 'America' , 'Bragantino' , 'Santos' , 'São Paulo')
print('=-' *40)
print(f'A ordem atual do campeaonato é {time}')
print('=-' *40)
print(f'Os 5 primeiros são {time[:5]}')
print('=-' *40)
print(f'Os quatro ultimos são {time[-4:]}')
print('=-' *40)
print(f'Os time por ordem alfabética {sorted(time)}')
print('=-' *40)
print(f'O time do Bragantino está na posição {time.index("Bragantino")+1}')
print('=-' *40)