somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres = 0
for quant in range(1, 5):
    print ('-'*7, f'{quant}', '-' *7)
    nome = str(input('Digite seu nome: ').strip())
    sexo = str(input('Digite seu sexo [M/F]: ').upper().strip())
    idade = int(input('Digite sua idade: ').strip())
    somaidade = somaidade + idade
    if quant == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        mulheres = mulheres + 1

mediaidade = somaidade / 4
print(f'''A média de idade do grupo é {mediaidade}.
    O homem mais velho se chama {nomevelho} e tem {maioridadehomem}
    E tem {mulheres} Mulheres menor que 20 anos.''')