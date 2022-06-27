dados = list()
aluno = {}
while True:
    aluno['Nome'] = str(input('Digite o nome do Aluno(a): ')).strip().capitalize()
    aluno['Média'] = float(input(f'Digite a média do {aluno["Nome"]}: ').strip().capitalize())
    if aluno['Média'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif aluno['Média'] <7 and aluno['Média'] >= 5:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    dados.append(aluno.copy())
    aluno.clear
    r = input('Deseja continuar?[S/N] ').upper().capitalize()
    if r in 'N':
        break
for e in dados:
    for i, a in e.items():
        
        print(f'{i} = {a}')
    print()