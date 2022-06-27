cadastro = []
cadastro1 = 0
while True:
    cadastro1 = int(input('Digite o numero do cadastro que deseja Cadastrar: '))
    while cadastro1 in cadastro:
        print('Esse cadastro já foi digitado')
        cadastro1 = int(input('Digite o numero do cadastro que deseja pesquisar: '))
    else:
        cadastro.append(cadastro1)
    continuar = input('Deseja continuar cadastrando?[S/N]').upper().capitalize()
    if continuar == 'N':
        break
        

print('---'*50)
print(f'Os números cadastrados foram: {sorted(cadastro)}')