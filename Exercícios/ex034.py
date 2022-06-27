sal = float(input('Digite o salário atual do funcionário: '))
if sal > 1250.00:
    aumento = sal / 100 * 10
if sal <= 1250.00:
    aumento = sal / 100 * 15
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal, sal+aumento))