casa = float(input('Digite o valor da casa: ').strip())
sal = float(input('Digite seu salário: ').strip())
num_parcelas = int(input('Digite a quantidade de parcelas: ').strip())
valor_parcelas = casa / num_parcelas
percentual = sal /100 * 30
if valor_parcelas > percentual:
    print('NEGADO')
else:
    print('APROVADO')
#print(valor_parcelas)
#print(percentual)