lista = []
pessoa = {}
r = ''
soma = 0
media = 0
mulheres = []
acima = []
while True:
    pessoa['nome'] = str(input('Dgite o nome: ')).capitalize().strip()
    pessoa['idade'] = int(input('Digite a idade: ').strip())
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0].strip()
    while  pessoa['sexo'] not in 'MF':
        print('Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0].strip()
    lista.append(pessoa.copy())
    r = str(input('Deseja continuar?[S/N]: ')).upper()[0].strip()
    while r not in 'SN':
        print('ERRO!! Responda apenas S ou N.')
        r = str(input('Deseja continuar?[S/N]: ')).upper()[0].strip()
    if r == 'N':
            break
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for c in lista:
    soma = soma + c['idade']
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m}; ', end='')
print()
print('D) A lista de pessoas acima da média:')
for p in lista:
    if p['idade'] >= media:
        print(f'    Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}.')
print('=-'*20)
print(f'PROGRAMA ENCERRADO!!!')
print('=-'*20)