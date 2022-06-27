idade = quantidade = maior =  homens = mulheresmenor = 0
sexo= ' '
continuar = 'S'
while True:
    if continuar == 'S':
        print('Cadastro de pessoas\n')
        while idade not in range (1, 101):
            idade = int(input('digite sua idade:\n').strip())
        while sexo not in 'MF':
            sexo = str(input('Digite seu sexo: [M/F]\n')).strip().upper()[0]
        quantidade += 1
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade <= 20:
            mulheresmenor += 1
        continuar = str(input('Deseja continuar cadastrando? [S/N]\n')).strip().upper()[0]
    elif continuar == 'N':
        break
    else:
        continuar = str(input('DIGITE APENAS "S" OU "N".\nDeseja continuar cadastrando? [S/N]\n')).strip().upper()[0]
print(f'{quantidade} pessoas foram cadastradas.\n{maior} pessoas tem 18 anos ou mais.\n{homens} são homens.\n{mulheresmenor} São mulheres com 20 anos ou menos.')
print('Programa de cadastro encerrado!!!')