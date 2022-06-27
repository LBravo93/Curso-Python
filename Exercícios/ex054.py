import datetime
atual = datetime.date.today().year
totalmenor = 0
totalmaior = 0
for c in range(1, 8):
    nasc = int(input(f'Em qual ano a {c} Pessoa nasceu : '))
    if atual - nasc < 18:
        totalmenor = totalmenor + 1
    else:
        totalmaior = totalmaior + 1
print(f'São {totalmaior} pessoas maiores de idade.')
print(f'São {totalmenor} pessoas menores de idade.')