sexo = str(input('Digite seu sexo: \n')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo: \n')).upper().strip()[0]
print(f'''Sexo {sexo} registrado com sucesso.
'fim do programa''')