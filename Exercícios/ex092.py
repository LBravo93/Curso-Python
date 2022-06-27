from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de trabalho:(caso não tenha digite "0") '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano da contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['idade'] - (datetime.now().year - cadastro['contratação'])) + 35
for i, c in cadastro.items():
    print(f' - {i} tem o valor {c}')
